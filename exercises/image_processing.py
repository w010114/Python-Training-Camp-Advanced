# exercises/image_processing.py
"""
练习：图像基本处理

描述：
使用 OpenCV 实现基本的图像读取、灰度转换、高斯滤波和边缘检测。

请补全下面的函数 `image_processing_pipeline`。
"""
import cv2
import numpy as np

def image_processing_pipeline(image_path):
    """
    使用 OpenCV 读取图像，进行高斯滤波和边缘检测。
    参数:
        image_path: 图像文件的路径 (字符串).
    返回:
        edges: Canny 边缘检测的结果 (NumPy 数组, 灰度图像).
               如果读取图像失败, 返回 None.
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取（img is None?）。
    # 3. 使用 cv2.cvtColor() 将图像转为灰度图 (cv2.COLOR_BGR2GRAY)。
    # 4. 使用 cv2.GaussianBlur() 进行高斯滤波。
    # 5. 使用 cv2.Canny() 进行边缘检测。
    # 6. 使用 try...except 包裹代码以处理可能的异常。
    try:
        # 使用 cv2.imread() 读取图像
        img = cv2.imread(image_path)
        if img is None:
            return None
        
        # 使用 cv2.cvtColor() 将图像转为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 使用 cv2.GaussianBlur() 进行高斯滤波
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 使用 cv2.Canny() 进行边缘检测
        edges = cv2.Canny(blurred, 50, 150)
        
        return edges
    
    except Exception as e:
        print(f"发生错误：{e}")
        return None

# 示例用法
if __name__ == "__main__":
    # 替换为你的测试图像路径
    test_image_path = "picture/7.png"
    edges = image_processing_pipeline(test_image_path)
    
    if edges is not None:
        cv2.imshow("Edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()