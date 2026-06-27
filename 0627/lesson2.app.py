import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# ====================================
# 設定中文字型（微軟正黑體）
# ====================================
matplotlib.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
matplotlib.rcParams["axes.unicode_minus"] = False

# ====================================
# 準備資料：X 軸範圍 0 ~ 4π
# ====================================
x = np.linspace(0, 4 * np.pi, 1000)
A_init = 1.0      # 初始振幅
omega_init = 1.0  # 初始頻率
phi_init = 0.0    # 初始相位

y_sin = A_init * np.sin(omega_init * x + phi_init)
y_cos = A_init * np.cos(omega_init * x + phi_init)

# ====================================
# 建立圖表
# ====================================
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.3)

# 繪製兩條曲線
(sin_line,) = ax.plot(x, y_sin, label="y = A·sin(ω·x + φ)", color="#1f77b4")
(cos_line,) = ax.plot(x, y_cos, label="y = A·cos(ω·x + φ)", color="#ff7f0e")

# 圖表設定
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-5.5, 5.5)
ax.set_title("正弦（sin）與餘弦（cos）波形", fontsize=14)
ax.set_xlabel("x（弧度）", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(fontsize=11)

# ====================================
# 建立滑桿
# ====================================
slider_color = "lightgoldenrodyellow"

# 振幅滑桿
ax_amp = plt.axes([0.15, 0.18, 0.65, 0.03])
slider_amp = Slider(
    ax=ax_amp, label="振幅 (A)", valmin=0.1, valmax=5.0,
    valinit=A_init, valstep=0.05, color="#1f77b4",
)

# 頻率滑桿
ax_freq = plt.axes([0.15, 0.12, 0.65, 0.03])
slider_freq = Slider(
    ax=ax_freq, label="頻率 (ω)", valmin=0.1, valmax=10.0,
    valinit=omega_init, valstep=0.05, color="#ff7f0e",
)

# 相位偏移滑桿
ax_phase = plt.axes([0.15, 0.06, 0.65, 0.03])
slider_phase = Slider(
    ax=ax_phase, label="相位偏移 (φ)", valmin=0, valmax=2 * np.pi,
    valinit=phi_init, valstep=0.01, color="#2ca02c",
)


# ====================================
# 滑桿更新回呼函式
# ====================================
def update(val):
    A = slider_amp.val
    omega = slider_freq.val
    phi = slider_phase.val

    sin_line.set_ydata(A * np.sin(omega * x + phi))
    cos_line.set_ydata(A * np.cos(omega * x + phi))

    fig.canvas.draw_idle()


slider_amp.on_changed(update)
slider_freq.on_changed(update)
slider_phase.on_changed(update)

plt.show()
