import pyrealsense2 as rs
import numpy as np
import cv2

# NumPy 배열 출력 설정 변경
np.set_printoptions(threshold=np.inf)  # 모든 요소가 출력되도록 설정

# 카메라 설정 및 스트리밍 시작
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)

# 첫 프레임에서 관심 영역의 깊이 값 추출 및 출력
try:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    if depth_frame and color_frame:
        # 깊이 이미지와 컬러 이미지를 numpy 배열로 변환
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # 관심 영역 설정
        x_min, y_min, x_max, y_max = 150, 150, 400, 350  # 관심 영역의 좌표 설정

        # 지정된 영역의 깊이 값만 추출
        region_depth = depth_image[y_min:y_max, x_min:x_max]

        # 평균과 표준편차 계산
        mean_depth = np.mean(region_depth)
        std_depth = np.std(region_depth)

        # 평균과 표준편차 출력
        print(f"평균: {mean_depth}")
        print(f"표준편차: {std_depth}")

        # 모든 깊이 값 출력 (생략 없이)
        #print("Depth values in the region:")
        #print(region_depth.flatten())  # 1차원 배열로 변환하여 출력

        # 관심 영역을 표시
        cv2.rectangle(color_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # 첫 프레임의 결과 이미지 표시 (한번만 출력)
        cv2.imshow('Color Image with ROI', color_image)
        cv2.waitKey(1)  # 첫 프레임을 잠시 표시

    # 실시간 프레임을 계속해서 받아오는 루프
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())

        # 실시간 컬러 이미지를 표시
        cv2.imshow('Color Image', color_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
