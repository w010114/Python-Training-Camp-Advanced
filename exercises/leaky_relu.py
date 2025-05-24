# exercises/leaky_relu.py
"""
练习：Leaky ReLU 激活函数

描述：
实现 Leaky ReLU 激活函数。
Leaky ReLU 是 ReLU 的一个变种，允许负输入值有一个小的正斜率。

请补全下面的函数 `leaky_relu`。
"""
import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    计算 Leaky ReLU 激活函数。
    公式: max(alpha * x, x)

    Args:
        x (np.array): 输入数组，任意形状。
        alpha (float): 负斜率系数，默认为 0.01。

    Return:
        np.array: Leaky ReLU 激活后的数组，形状与输入相同。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 可以使用 np.maximum() 函数。
    # 2. 计算 alpha * x。
    # 3. 计算 max(alpha * x, x)。
    # 示例用法
 # 使用 np.where 来实现 Leaky ReLU 激活函数
    return np.where(x >= 0, x, alpha * x)

# 示例用法
if __name__ == "__main__":
    # 测试样例1
    x1 = np.array([-1.0, 0.0, 1.0, 2.0])
    alpha1 = 0.01
    output1 = leaky_relu(x1, alpha1)
    print(f"输入: {x1}")
    print(f"输出: {output1}")

    # 测试样例2 (默认 alpha)
    x2 = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
    output2 = leaky_relu(x2)
    print(f"输入: {x2}")
    print(f"输出: {output2}")