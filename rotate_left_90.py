from PIL import Image
import os

# 设置输入和输出文件夹路径
input_folder = "images_pre_processed_1"   # 原始图片文件夹
output_folder = "images_final_rotated" # 旋转后图片存放位置

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp", ".tiff")):  # 只处理图片文件
        img_path = os.path.join(input_folder, filename)
        
        with Image.open(img_path) as img:
            # 270°（逆时针 90°）旋转：
            rotated_img = img.rotate(270, expand=True)
            
            # 保存旋转后的图片
            rotated_img.save(os.path.join(output_folder, filename))

print("所有图片已成功旋转 90 度！")
