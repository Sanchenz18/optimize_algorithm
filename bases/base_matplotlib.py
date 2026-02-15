import numpy as np
import matplotlib.pyplot as plt

# Step 0: Preparing Data
# 生成 0 到 10 之间的 100 个点
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Step 1: Create Canvas
# figsize=(宽, 高)，单位是英寸
plt.figure(figsize=(10, 6))

# Step 2: Plotting
# label 参数用于后续显示图例 (Legend)
# 注意：你代码中的 'lable' 是错别字，必须是 'label'
plt.plot(x, y, label='y = sin(x)', color='blue', linewidth=2)

# Step 3: Decoration
# 包括：图例、标题、坐标轴标签、网格
plt.legend()             # 显示左上角的图例
plt.title("Sin Function Plot") # 标题
plt.xlabel("X Axis")     # X轴标签
plt.ylabel("Y Axis")     # Y轴标签
plt.grid(True, alpha=0.3) # 打开网格，alpha控制透明度

# Step 4: Show
plt.show()
