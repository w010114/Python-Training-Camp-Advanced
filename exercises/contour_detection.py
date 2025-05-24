# exercises/contour_detection.py
"""
练习：轮廓检测

描述：
使用 OpenCV 检测图像中的轮廓并将其绘制出来。

请补全下面的函数 `contour_detection`。
"""
import cv2
import numpy as np

def contour_detection(image_path):
    """
    使用 OpenCV 检测图像中的轮廓
    参数:
        image_path: 图像路径
    返回:
        tuple: (绘制轮廓的图像, 轮廓列表) 或 (None, None) 失败时
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取。
    # 3. 使用 cv2.cvtColor() 转为灰度图。
    # 4. 使用 cv2.threshold() 进行二值化处理。
    # 5. 使用 cv2.findContours() 检测轮廓 (注意不同 OpenCV 版本的返回值)。
    # 6. 创建图像副本 img.copy() 用于绘制。
    # 7. 使用 cv2.drawContours() 在副本上绘制轮廓。
    # 8. 返回绘制后的图像和轮廓列表。
    # 9. 使用 try...except 处理异常。
    try:
        # 读取图像
        img = cv2.imread(image_path)
        if img is None:
            print(f"无法读取图像: {image_path}")
            return None, None
            
        print(f"成功读取图像，尺寸: {img.shape}")
            
        # 转为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("灰度转换完成")
        
        # 二值化处理
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        print("二值化完成")
        
        # 检测轮廓(OpenCV 4.x版本)
        contours_tuple, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = list(contours_tuple)

        # 详细类型检查
        print(f"轮廓类型: {type(contours)}")
        if isinstance(contours, tuple):
            print(f"检测到元组结构，包含{len(contours)}个元素")
            contours = contours[0]  # 取第一个元素作为轮廓列表
        elif isinstance(contours, list):
            print(f"检测到列表结构，包含{len(contours)}个轮廓")
        else:
            print("未知的轮廓类型")
            return None, None
            
        if len(contours) == 0:
            print("警告: 未检测到任何轮廓")
            return img.copy(), []  # 返回原始图像和空列表
        
        # 创建副本并绘制轮廓
        img_contours = img.copy()
        cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
        print(f"成功绘制{len(contours)}个轮廓")
        if isinstance(contours, list):
            print(f"轮廓列表长度: {len(contours)}")
        return img_contours, list(contours)
        
    except Exception as e:
        print(f"Error in contour detection: {e}")
        return None, None