import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List, Tuple

def f(x):
    return x ** 2 - 4 * x + 3

def golden_section_search(
    f: Callable[[float], float], 
    a: float, 
    b: float, 
    tol: float = 1e-6
) -> Tuple[float, int, List[Tuple[float, float]]]:
    """
    黄金分割法（0.618法）求单峰函数极小值
    增加返回值：history (记录每次迭代的区间 a, b)
    """
    phi = (np.sqrt(5) - 1) / 2  # 黄金比例 ≈ 0.618
    
    # 记录初始区间
    history = [(a, b)]
    
    # 初始化试点
    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)
    f1, f2 = f(x1), f(x2)
    
    iteration = 0
    while (b - a) > tol:
        iteration += 1
        
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + phi * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - phi * (b - a)
            f1 = f(x1)
            
        # 记录每一步收缩后的区间
        history.append((a, b))
    
    return (a + b) / 2, iteration, history

if __name__ == "__main__":
    # 1. 运行算法并获取历史数据
    a_init, b_init = 0, 5  # 初始搜索区间
    optimal_x, iter_count, history = golden_section_search(f, a_init, b_init)
    optimal_y = f(optimal_x)
    
    print("=" * 50)
    print(f"Optimized Result:")
    print(f"Minimum Point    x* = {optimal_x:.8f}")
    print(f"Minimum Value f(x*) = {optimal_y:.8f}")
    print(f"Iteration Count     = {iter_count}")
    print("=" * 50)
    
    # 2. 可视化设置
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- 子图1：函数曲线 ---
    x_vals = np.linspace(a_init - 1, b_init + 1, 500)
    y_vals = f(np.array(x_vals))
    
    # 绘制函数
    ax1.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = x² - 4x + 3')
    
    # 绘制最终的最优解点
    ax1.plot(optimal_x, optimal_y, 'ro', markersize=10, label='Optimal Point', zorder=5)
    ax1.axvline(x=optimal_x, color='r', linestyle='--', alpha=0.6)
    
    # 用阴影区域表示初始搜索范围（比之前的黄色矩形更符合数学含义）
    ax1.axvspan(a_init, b_init, color='gold', alpha=0.15, label='Initial Interval')
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Optimization Result')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # --- 子图2：区间收缩过程 (瀑布图) ---
    # 我们只取前10-15次迭代演示，以免图表过于拥挤，或者全部显示
    display_steps = min(len(history), 15) 
    
    for i in range(display_steps):
        current_a, current_b = history[i]
        mid = (current_a + current_b) / 2
        
        # 颜色渐变：从深蓝到浅蓝
        color = plt.get_cmap('viridis')(i / display_steps)
        
        # 绘制水平线段表示区间
        ax2.hlines(y=i, xmin=current_a, xmax=current_b, linewidth=6, color=color, alpha=0.8)
        
        # 在线段中间标记区间长度
        width = current_b - current_a
        ax2.text(mid, i - 0.15, f'L={width:.2f}', ha='center', fontsize=8, color='gray')

    # 设置右图坐标轴
    ax2.set_xlabel('Search Interval (x)')
    ax2.set_ylabel('Iteration Step')
    ax2.set_title(f'Interval Contraction Process (First {display_steps} Steps)')
    
    # 反转Y轴，让Step 0在最上面，符合"向下搜索"的直觉
    ax2.set_ylim(display_steps + 0.5, -1) 
    ax2.set_yticks(range(display_steps))
    ax2.set_xlim(a_init - 0.5, b_init + 0.5)
    
    # 添加一条竖线表示最终收敛的x值
    ax2.axvline(x=optimal_x, color='red', linestyle='--', alpha=0.4, linewidth=1)
    
    ax2.grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    plt.show()