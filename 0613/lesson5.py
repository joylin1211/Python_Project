import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# ======================
# 1️⃣ 解決中文顯示問題（Windows）
# ======================
matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 微軟正黑體
matplotlib.rcParams['axes.unicode_minus'] = False  # 負號正常顯示

# ======================
# 2️⃣ 讀取 CSV
# ======================
df = pd.read_csv("考試分數_3年6班.csv")

# ======================
# 3️⃣ 篩選學生
# ======================
zhao = df[df["學生姓名"] == "趙冠宇"]

# ======================
# 4️⃣ 取出各科成績
# ======================
scores = zhao.iloc[0].loc[["語文", "數學", "英語", "物理", "化學"]]

# ======================
# 5️⃣ 畫長條圖
# ======================
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(1, 1, 1)

ax.bar(scores.index, scores.values)

# ======================
# 6️⃣ 標題與標籤
# ======================
ax.set_title("趙冠宇成績")
ax.set_xlabel("科目")
ax.set_ylabel("分數")

# ======================
# 7️⃣ Y 軸範圍
# ======================
ax.set_ylim(0, 100)

# ======================
# 8️⃣ 顯示圖表
# ======================
plt.tight_layout()
plt.show()