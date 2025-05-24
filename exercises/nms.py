# exercises/nms.py
"""
练习：非极大值抑制 (Non-Maximum Suppression, NMS)

描述：
实现目标检测中常用的 NMS 算法，用于去除重叠度高的冗余边界框。

请补全下面的函数 `calculate_iou` 和 `nms`。
"""
import numpy as np

def calculate_iou(box1, box2):
    """
    计算两个边界框的交并比 (IoU)。
    边界框格式：[x_min, y_min, x_max, y_max]

    Args:
        box1 (np.array): 第一个边界框 [x1_min, y1_min, x1_max, y1_max]。
        box2 (np.array): 第二个边界框 [x2_min, y2_min, x2_max, y2_max]。

    Return:
        float: IoU 值。
    """
    # 请在此处编写代码
    # (与 iou.py 中的练习相同，可以复用代码或导入)
    # 提示：计算交集面积和并集面积，然后相除。
     # 将输入转换为 NumPy 数组以方便计算
    box1 = np.array(box1)
    box2 = np.array(box2)

    # 确定两个框相交区域的左上角坐标
    x_left = max(box1[0], box2[0])
    y_top = max(box1[1], box2[1])

    # 确定两个框相交区域的右下角坐标
    x_right = min(box1[2], box2[2])
    y_bottom = min(box1[3], box2[3])

    # 计算相交区域的面积
    intersection_area = max(0, x_right - x_left) * max(0, y_bottom - y_top)

    # 计算 box1 和 box2 的面积
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    # 计算并集面积
    union_area = box1_area + box2_area - intersection_area

    # 计算 IoU，处理 union_area 为 0 的情况
    iou = intersection_area / union_area if union_area != 0 else 0

    return iou

def nms(boxes, scores, iou_threshold):
    """
    执行非极大值抑制 (NMS)。

    Args:
        boxes (np.array): 边界框数组，形状 (N, 4)，格式 [x_min, y_min, x_max, y_max]。
        scores (np.array): 每个边界框对应的置信度分数，形状 (N,)。
        iou_threshold (float): IoU 阈值，用于判断是否抑制。

    Return:
        list: 保留下来（未被抑制）的边界框的索引列表。
    """
    # 请在此处编写代码
    # 提示：
    # 1. 如果 boxes 为空，直接返回空列表。
    # 2. 将 boxes 和 scores 转换为 NumPy 数组。
    # 3. 计算所有边界框的面积 areas。
    # 4. 根据 scores 对边界框索引进行降序排序 (order = np.argsort(scores)[::-1])。
    # 5. 初始化一个空列表 keep 用于存储保留的索引。
    # 6. 当 order 列表不为空时循环：
    #    a. 取出 order 中的第一个索引 i (当前分数最高的框)，加入 keep。
    #    b. 计算框 i 与 order 中剩余所有框的 IoU。
    #       (需要计算交集区域坐标 xx1, yy1, xx2, yy2 和交集面积 intersection)
    #    c. 找到 IoU 小于等于 iou_threshold 的索引 inds。
    #    d. 更新 order，只保留那些 IoU <= threshold 的框的索引 (order = order[inds + 1])。
    # 7. 返回 keep 列表。
    # 如果 boxes 为空，直接返回空列表
    if len(boxes) == 0:
        return []

    # 将 boxes 和 scores 转换为 NumPy 数组
    boxes = np.array(boxes)
    scores = np.array(scores)

    # 计算所有边界框的面积
    areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

    # 根据 scores 对边界框索引进行降序排序
    order = np.argsort(scores)[::-1]

    # 初始化一个空列表 keep 用于存储保留的索引
    keep = []

    while order.size > 0:
        # 取出 order 中的第一个索引 i (当前分数最高的框)，加入 keep
        i = order[0]
        keep.append(i)

        # 计算框 i 与 order 中剩余所有框的 IoU
        xx1 = np.maximum(boxes[i, 0], boxes[order[1:], 0])
        yy1 = np.maximum(boxes[i, 1], boxes[order[1:], 1])
        xx2 = np.minimum(boxes[i, 2], boxes[order[1:], 2])
        yy2 = np.minimum(boxes[i, 3], boxes[order[1:], 3])

        # 计算交集面积
        intersection = np.maximum(0, xx2 - xx1) * np.maximum(0, yy2 - yy1)

        # 计算 IoU
        iou = intersection / (areas[i] + areas[order[1:]] - intersection)

        # 找到 IoU 小于等于 iou_threshold 的索引
        inds = np.where(iou <= iou_threshold)[0]

        # 更新 order，只保留那些 IoU <= threshold 的框的索引
        order = order[inds + 1]

    return keep

# 示例用法
if __name__ == "__main__":
    # 测试样例
    boxes = np.array([
        [100, 100, 200, 200],
        [150, 150, 250, 250],
        [50, 50, 100, 100],
        [120, 120, 220, 220]
    ])
    scores = np.array([0.9, 0.8, 0.7, 0.6])
    iou_threshold = 0.5

    keep_indices = nms(boxes, scores, iou_threshold)
    print("保留的边界框索引：", keep_indices)