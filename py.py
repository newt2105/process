import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho đồ thị sin và cos
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Khởi tạo hình vẽ
fig, ax = plt.subplots()

# Vẽ đồ thị sin và lưu trạng thái của hình vẽ
for i in range(len(x)):
    ax.clear()
    ax.plot(x[:i], y_sin[:i], label='sin(x)')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.legend()
    plt.pause(0.01)  # Hiển thị trong một khoảng thời gian ngắn

# Vẽ đồ thị cos và lưu trạng thái của hình vẽ
for i in range(len(x)):
    ax.clear()
    ax.plot(x, y_sin, label='sin(x)')
    ax.plot(x[:i], y_cos[:i], label='cos(x)')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)
    ax.legend()
    plt.pause(0.01)  # Hiển thị trong một khoảng thời gian ngắn

plt.show()
