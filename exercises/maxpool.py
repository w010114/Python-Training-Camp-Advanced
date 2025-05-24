# exercises/maxpool.py
"""
练习：最大池化 (Max Pooling)

描述：
实现一个简单的二维最大池化操作。

请补全下面的函数 `maxpool`。
"""
import numpy as np

def maxpool(x, kernel_size, stride):
    """
    执行二维最大池化操作。

    Args:
        x (np.array): 输入二维数组，形状 (H, W)。
        kernel_size (int): 池化窗口的大小 (假设为正方形 k x k)。
        stride (int): 池化窗口移动的步幅。

    Return:
        np.array: 最大池化结果，形状 (out_H, out_W)。
                  out_H = (H - kernel_size) // stride + 1
                  out_W = (W - kernel_size) // stride + 1
    """
    # 请在此处编写代码
    # 提示：
    # 1. 计算输出的高度和宽度。
    # 2. 初始化输出数组。
    # 3. 使用嵌套循环遍历输出数组的每个位置 (i, j)。
    # 4. 计算当前池化窗口在输入数组 x 中的起始位置 (h_start, w_start)。
    # 5. 提取当前池化窗口 window = x[h_start:h_start+kernel_size, w_start:w_start+kernel_size]。
    # 6. 找到窗口中的最大值 np.max(window)。
    # 7. 将最大值存入输出数组 out[i, j]。
    # 获取输入数组的形状
    H, W = x.shape
    
    # 计算输出的高度和宽度
    out_H = (H - kernel_size) // stride + 1
    out_W = (W - kernel_size) // stride + 1
    
    # 初始化输出数组
    out = np.zeros((out_H, out_W))
    
    # 使用嵌套循环遍历输出数组的每个位置 (i, j)
    for i in range(out_H):
        for j in range(out_W):
            # 计算当前池化窗口在输入数组 x 中的起始位置
            h_start = i * stride
            w_start = j * stride
            
            # 提取当前池化窗口
            window = x[h_start:h_start + kernel_size, w_start:w_start + kernel_size]
            
            # 找到窗口中的最大值
            out[i, j] = np.max(window)
    
    return out

# 示例用法
if __name__ == "__main__":
    # 测试样例1
    x1 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    kernel_size1 = 2
    stride1 = 2
    output1 = maxpool(x1, kernel_size1, stride1)
    print("测试样例1的输出：")
    print(output1)

    # 测试样例2
    x2 = np.array([
        [10, 20, 30, 40, 50],
        [60, 70, 80, 90, 100],
        [110, 120, 130, 140, 150],
        [160, 170, 180, 190, 200],
        [210, 220, 230, 240, 250]
    ])
    kernel_size2 = 3
    stride2 = 2
    output2 = maxpool(x2, kernel_size2, stride2)
    print("测试样例2的输出：")
    print(output2)