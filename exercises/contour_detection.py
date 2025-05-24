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
            return None, None
        
        # 转为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 二值化处理
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        
        # 检测轮廓
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # 绘制轮廓
        result_img = img.copy()
        cv2.drawContours(result_img, contours, -1, (0, 255, 0), 2)
        
        return result_img, contours
    
    except Exception as e:
        print(f"发生错误：{e}")
        return None, None

# 示例用法
if __name__ == "__main__":
    # 替换为你的测试图像路径
    test_image_path = "picture/7.png"
    result, contours = contour_detection(test_image_path)
    
    if result is not None:
        cv2.imshow("Contours", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()