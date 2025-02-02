import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# 输入和输出文件夹
input_folder = "images_final_rotated/"  # 原始图片所在目录
output_folder = "processed_images/"  # 处理后图片保存目录

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 处理函数
def process_image(image_path):
    """ 处理单张图片 """
    img = cv2.imread(image_path)
    if img is None:
        print(f"无法读取文件: {image_path}")
        return None

    # 1️⃣ 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2️⃣ 进行对比度增强（直方图均衡化）
    equalized = cv2.equalizeHist(gray)

    # 3️⃣ 去雾（使用 Retinex 方法）
    def enhance_contrast(image):
        blur = cv2.GaussianBlur(image, (21, 21), 0)
        enhanced = cv2.addWeighted(image, 1.5, blur, -0.5, 0)
        return enhanced

    enhanced = enhance_contrast(equalized)

    return enhanced

# 读取文件夹中的所有图片
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# 遍历所有图片进行处理
for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)  # 输入图片路径
    output_path = os.path.join(output_folder, image_file)  # 输出图片路径

    processed_image = process_image(input_path)
    
    if processed_image is not None:
        cv2.imwrite(output_path, processed_image)  # 保存图片
        print(f"已处理: {image_file} -> {output_path}")

print("批量处理完成！🎉")
