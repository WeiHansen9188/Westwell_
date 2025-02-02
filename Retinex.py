import cv2
import numpy as np
import os

# 输入和输出文件夹
input_folder = "images_final_rotated/"  # 原始图片所在目录
output_folder = "processed_images/"  # 处理后图片保存目录

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 只进行去雾处理的函数
def remove_haze(image):
    """ 只执行去雾处理 """
    if image is None:
        return None

    # 使用 Retinex 方法进行去雾
    blur = cv2.GaussianBlur(image, (21, 21), 0)  # 高斯模糊
    dehazed = cv2.addWeighted(image, 1.5, blur, -0.5, 0)  # 细节增强
    return dehazed

# 读取文件夹中的所有图片
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png'))]

# 遍历所有图片进行处理
for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)  # 输入图片路径
    output_path = os.path.join(output_folder, image_file)  # 输出图片路径

    img = cv2.imread(input_path)  # 读取原始彩色图像
    dehazed_image = remove_haze(img)  # 仅去雾处理

    if dehazed_image is not None:
        cv2.imwrite(output_path, dehazed_image)  # 保存处理后的图片
        print(f"已处理: {image_file} -> {output_path}")

print("批量去雾处理完成！🎉")
