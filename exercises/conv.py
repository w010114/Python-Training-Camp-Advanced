# exercises/conv.py
"""
练习：二维卷积 (Convolution)

描述：
实现一个简单的二维卷积操作。

请补全下面的函数 `conv2d`。
"""
import numpy as np

def conv2d(x, kernel):
    """
    执行二维卷积操作 (无填充, 步幅为 1)。

    Args:
        x (np.array): 输入二维数组, 形状 (H, W)。
        kernel (np.array): 卷积核二维数组, 形状 (kH, kW)。

    Return:
        np.array: 卷积结果, 形状 (out_H, out_W)。
                  out_H = H - kH + 1
                  out_W = W - kW + 1
    """
    # 请在此处编写代码
    # 提示：
    # 1. 获取输入 x 和卷积核 kernel 的形状。
    # 2. 计算输出的高度和宽度。
    # 3. 初始化输出数组。
    # 4. 使用嵌套循环遍历输出数组的每个位置 (i, j)。
    # 5. 提取输入 x 中与当前卷积核对应的区域 (patch)。
    # 6. 计算 patch 和 kernel 的元素乘积之和 (np.sum(patch * kernel))。
    # 7. 将结果存入输出数组 out[i, j]。
    # 获取输入 x 和卷积核 kernel 的形状
    H, W = x.shape
    kH, kW = kernel.shape
    
    # 计算输出的高度和宽度
    out_H = H - kH + 1
    out_W = W - kW + 1
    
    # 初始化输出数组
    out = np.zeros((out_H, out_W))
    
    # 使用嵌套循环遍历输出数组的每个位置 (i, j)
    for i in range(out_H):
        for j in range(out_W):
            # 提取输入 x 中与当前卷积核对应的区域 (patch)
            patch = x[i:i + kH, j:j + kW]
            
            # 计算 patch 和 kernel 的元素乘积之和
            out[i, j] = np.sum(patch * kernel)
    
    return out

# 示例用法
if __name__ == "__main__":
    # 测试样例1：全零测试
    img1 = np.zeros((5, 5))
    kernel1 = np.random.rand(3, 3)
    result1 = conv2d(img1, kernel1)
    print("测试样例1（全零输入）结果：\n", result1)

    # 测试样例2：对角核测试
    img2 = np.eye(5)
    kernel2 = np.array([[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])
    result2 = conv2d(img2, kernel2)
    print("测试样例2（对角检测）结果：\n", result2)

    # 测试样例3：求和核测试
    img3 = np.arange(25).reshape(5, 5)
    kernel3 = np.ones((3, 3))
    result3 = conv2d(img3, kernel3)
    print("测试样例3（区域求和）结果：\n", result3)