import cv2
import os
import numpy as np

# 定义输入文件夹（待处理图片）和输出文件夹（处理后的图片）
input_folder = "images"  # 替换成你的文件夹路径
output_folder = "processed_images"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 预处理函数
def preprocess_image(image_path, output_path):
    # 读取图像
    img = cv2.imread(image_path)
    if img is None:
        print(f"无法读取图像: {image_path}")
        return
    
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二值化处理（Adaptive Thresholding）
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 降噪处理（使用中值滤波）
    denoised = cv2.medianBlur(binary, 3)

    # 透视变换（如果有畸变）
    # 这里可以添加透视校正代码，如检测边缘后进行 cv2.getPerspectiveTransform

    # 保存预处理后的图像
    cv2.imwrite(output_path, denoised)

# 遍历文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        preprocess_image(input_path, output_path)
        print(f"已处理: {filename}")

print("✅ 批量处理完成！")
