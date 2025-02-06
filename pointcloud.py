import pyrealsense2 as rs
import numpy as np
import cv2
import open3d as o3d
import matplotlib.pyplot as plt

#############
# 카메라 설정 및 스트리밍 시작
# RealSense 카메라 설정
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 스트리밍 시작
pipeline.start(config)
####################

try:
    while True:
        ########
        # 실시간 프레임 캡쳐
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue
        ##########

        ##########
        # 프레임 데이터를 numpy 배열로 변환
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        ##########


        # 깊이 데이터 확인
        print(f"Depth image shape: {depth_image.shape}, min: {depth_image.min()}, max: {depth_image.max()}")

        # 깊이 이미지 시각화
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        cv2.imshow('Depth Image', depth_colormap)

        ###########
        # 포인트 클라우드 생성
        pc = rs.pointcloud()
        points = pc.calculate(depth_frame)
        ###########

        # 포인트와 텍스처 좌표를 numpy 배열로 변환
        vtx = np.asanyarray(points.get_vertices()).view(np.float32).reshape(-1, 3)
        tex_coords = np.asanyarray(points.get_texture_coordinates()).view(np.float32).reshape(-1, 2)

        # 포인트와 텍스처 좌표 크기 확인
        print(f"vtx size: {vtx.shape}, tex_coords size: {tex_coords.shape}")

        # 유효한 텍스처 좌표 필터링
        colors = np.asarray(color_image, dtype=np.float32) / 255.0
        uvs = tex_coords[:, :2]  # 텍스처 좌표의 u와 v 부분만 사용
        uvs[:, 0] *= color_image.shape[1]  # u 좌표를 이미지 너비로 스케일링
        uvs[:, 1] *= color_image.shape[0]  # v 좌표를 이미지 높이로 스케일링
        uvs = np.round(uvs).astype(int)  # 정수로 변환

        valid_mask = (uvs[:, 0] >= 0) & (uvs[:, 0] < color_image.shape[1]) & (uvs[:, 1] >= 0) & (uvs[:, 1] < color_image.shape[0])
        valid_uvs = uvs[valid_mask]
        valid_vtx = vtx[valid_mask]

        # 깊이 필터링 (예: 특정 깊이 범위 내의 포인트 선택)
        min_depth = 0.3  # 최소 깊이 (미터 단위)
        max_depth = 3.0 # 최대 깊이 (미터 단위)
        depth_mask = (valid_vtx[:, 2] > min_depth) & (valid_vtx[:, 2] < max_depth)
        filtered_vtx = valid_vtx[depth_mask]
        filtered_uvs = valid_uvs[depth_mask]

        if filtered_vtx.size > 0:
            valid_colors = colors[filtered_uvs[:, 1], filtered_uvs[:, 0]]

            # 포인트 클라우드 시각화
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(filtered_vtx)
            pcd.colors = o3d.utility.Vector3dVector(valid_colors)

            # 포인트 클라우드 밀도 높이기 위해 다운샘플링
            pcd = pcd.voxel_down_sample(voxel_size=0.005)

            # 클러스터링 수행
            eps = 0.03  # 거리 임계값
            min_points = 50  # 최소 포인트 수

            labels = np.array(pcd.cluster_dbscan(eps=eps, min_points=min_points))
            max_label = labels.max()
            print(f"point cloud has {max_label + 1} clusters")

            # 클러스터 시각화
            colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
            colors[labels < 0] = 0
            pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

            o3d.visualization.draw_geometries([pcd])

            # 가장 큰 클러스터 선택
            if max_label >= 0:
                counts = np.bincount(labels[labels >= 0])
                max_cluster_idx = np.argmax(counts)
                face_cluster = np.where(labels == max_cluster_idx)[0]

                # 얼굴 클러스터 시각화
                pcd_face_cluster = pcd.select_by_index(face_cluster)
                o3d.visualization.draw_geometries([pcd_face_cluster])
            else:
                print("No clusters found within the specified depth range.")
        else:
            print("No valid points found within the specified depth range.")



        # OpenCV로 컬러 이미지 표시
        cv2.imshow('Color Image', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
