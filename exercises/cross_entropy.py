"""
练习：交叉熵损失 (Cross Entropy Loss)

描述：
实现分类问题中常用的交叉熵损失函数。

请补全下面的函数 `cross_entropy_loss`。
"""
import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    计算交叉熵损失。

    Args:
        y_true (np.array): 真实标签 (独热编码或类别索引)。
                           如果 y_true 是类别索引, 它将被转换为独热编码。
                           形状: (N,) 或 (N, C)，N 是样本数, C 是类别数。
        y_pred (np.array): 模型预测概率，形状 (N, C)。
                           每个元素范围在 [0, 1]，每行的和应接近 1。

    Return:
        float: 平均交叉熵损失。
    """
    # 获取样本数量 N 和类别数量 C
    N = y_pred.shape[0]
    C = y_pred.shape[1]
    
    # 如果 y_true 是类别索引 (形状为 (N,)), 将其转换为独热编码
    if y_true.ndim == 1:
        y_true = np.eye(C)[y_true]
    
    # 为防止 log(0) 错误，将 y_pred 中非常小的值替换为 1e-12
    y_pred = np.clip(y_pred, 1e-12, 1.0)
    
    # 计算交叉熵损失
    loss = -np.sum(y_true * np.log(y_pred)) / N
    
    return loss

# 示例用法
if __name__ == "__main__":
    # 测试样例1：独热编码输入
    y_true1 = np.array([[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])
    y_pred1 = np.array([[0.7, 0.2, 0.1],
                        [0.1, 0.8, 0.1],
                        [0.2, 0.2, 0.6]])
    loss1 = cross_entropy_loss(y_true1, y_pred1)
    print("测试样例1（独热编码输入）损失：", loss1)

    # 测试样例2：类别索引输入
    y_true2 = np.array([0, 1, 2])
    y_pred2 = np.array([[0.7, 0.2, 0.1],
                        [0.1, 0.8, 0.1],
                        [0.2, 0.2, 0.6]])
    loss2 = cross_entropy_loss(y_true2, y_pred2)
    print("测试样例2（类别索引输入）损失：", loss2)