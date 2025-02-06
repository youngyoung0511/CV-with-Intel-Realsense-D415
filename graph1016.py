import numpy as np
import matplotlib.pyplot as plt

# x축과 y축 값 설정
x_values = [0.3, 1.5, 3.0, 4.5, 6.0]  # X축 두께(mm)
y_values = [680, 440, 496, 494, 476]  # Y축 distance(mm)

# 그래프 크기 설정
plt.figure(figsize=(10, 6))

# 바 그래프 그리기
plt.bar(x_values, y_values, color='blue', width=1.0)

# 축 레이블 및 제목 추가
plt.xlabel('Thickness (mm)', fontsize=16)
plt.ylabel('Distance (mm)', fontsize=16)
plt.title('Depth result over thickness', fontsize=20)
# 500mm 레드 선 추가
plt.axhline(y=500, color='red', linewidth=1.5, linestyle='-')

# 축 눈금 설정
plt.xticks(x_values, fontsize=15)
plt.yticks(fontsize=15)

# 그리드 추가
plt.grid(True, which='both', linestyle='--', linewidth=0.3)

# 그래프 표시
plt.tight_layout()
plt.show()
