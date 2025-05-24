# exercises/smooth_l1.py
"""
练习：Smooth L1 损失函数

描述：
实现 Smooth L1 损失函数，常用于目标检测中的边界框回归。

请补全下面的函数 `smooth_l1`。
"""
import numpy as np

def smooth_l1(x, sigma=1.0):
    """
    计算 Smooth L1 损失。
    公式:
        0.5 * (sigma * x)**2   if |x| < 1 / sigma**2
        |x| - 0.5 / sigma**2   otherwise

    Args:
        x (np.array): 输入差值数组，任意形状。
        sigma (float): 控制平滑区域的参数，默认为 1.0。

    Return:
        np.array: 计算得到的 Smooth L1 损失数组，形状与输入相同。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 计算 sigma 的平方 sigma2。
    # 2. 找到满足条件 |x| < 1 / sigma2 的元素索引 (可以使用 np.abs 和比较运算符)。
    # 3. 对满足条件的元素应用第一个公式 (0.5 * (sigma * x)**2)。
    # 4. 对不满足条件的元素应用第二个公式 (|x| - 0.5 / sigma2)。
    # 5. 可以使用 np.where() 来根据条件选择应用哪个公式。
    # 计算 sigma 的平方
    sigma2 = sigma ** 2

    # 找到满足条件 |x| < 1 / sigma2 的元素
    cond = np.abs(x) < 1.0 / sigma2

    # 使用 np.where() 根据条件选择应用哪个公式
    loss = np.where(cond, 0.5 * (sigma * x)**2, np.abs(x) - 0.5 / sigma2)

    return loss

# 示例用法
if __name__ == "__main__":
    # 测试样例1
    x1 = np.array([-0.5, 0.2, 0.8, -1.2])
    sigma1 = 1.0
    loss1 = smooth_l1(x1, sigma1)
    print(f"输入: {x1}")
    print(f"Smooth L1 损失: {loss1}")

    # 测试样例2
    x2 = np.array([-0.1, 0.1, 0.3, -0.2])
    sigma2 = 2.0
    loss2 = smooth_l1(x2, sigma2)
    print(f"输入: {x2}")
    print(f"Smooth L1 损失: {loss2}")