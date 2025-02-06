import numpy as np
import matplotlib.pyplot as plt

# x축 레이블 설정
x_labels = ['0.3', '0.6', '0.9', '1.2', '1.5', '1.8', '2.1', '2.4', '2.7', '3.0',
            '3.3', '3.6', '3.9', '4.2', '4.5', '4.8', '5.1', '5.4', '5.7', '6.0']

# 첫 번째 y값 (Depth 값)
y_values = [680, 560, 530, 474, 440, 428, 450, 470, 485, 496, 496, 497, 494, 497, 494, 498, 496, 487, 482, 476]

# 두 번째 그래프의 이론 값 설정 (주황색 선)
x_values = np.arange(0.3, 6.3, 0.3)
y_intercept = 1  # 1로 설정
theoretical_values = [y_intercept * np.exp(-0.36 * i) for i in x_values]

# 그래프 크기 설정
fig, ax1 = plt.subplots(figsize=(14, 6))

# 첫 번째 y축 (왼쪽 y축, Depth 값에 대한 그래프)
ax1.set_xlabel('Thickness(mm)', fontsize=20)
ax1.set_ylabel('Depth (mm)', fontsize=20, color='b')
ax1.plot(x_labels, y_values, marker='o', linestyle='-', color='b', label='Depth')
ax1.tick_params(axis='y', labelcolor='b', labelsize=16)  # y축 눈금 폰트 크기 설정
ax1.tick_params(axis='x', labelsize=16)  # x축 눈금 폰트 크기 설정
ax1.grid(True)

# 두 번째 y축 (오른쪽 y축, 이론적 투과율 그래프)
ax2 = ax1.twinx()  # 두 번째 y축을 공유하는 새 축 생성
ax2.set_ylabel('Theoretical', fontsize=20, color='orange')
ax2.plot(x_labels, theoretical_values, marker='o', linestyle='-', color='orange', label='Theoretical')
ax2.tick_params(axis='y', labelcolor='orange', labelsize=16)  # y축 눈금 폰트 크기 설정
ax2.set_ylim(0, 1)  # y축을 1부터 0까지 설정

# 수식 추가
equation_text = r'$I = I_0 \cdot e^{-\alpha x}$'
ax2.text(15, theoretical_values[10] + 0.2, equation_text, color='orange', fontsize=24)

# 범례 추가
fig.legend(loc='upper right', fontsize=16)

# 그래프 레이아웃 조정 및 표시
fig.tight_layout()
plt.show()
