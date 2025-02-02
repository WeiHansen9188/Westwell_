from PIL import Image
import os

# 设置输入和输出文件夹路径
input_folder = "frames_output"  # 原始图片文件夹
output_folder = "90right_images"  # 处理后的图片存放位置

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 定义裁剪区域 (left, upper, right, lower)
crop_box = (100, 100, 500, 500)  # 这里是示例，根据需要修改

# 遍历文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg", ".bmp", ".tiff")):
        img_path = os.path.join(input_folder, filename)
        
        # 打开图片
        with Image.open(img_path) as img:
            # 旋转图片 90 度（顺时针）
            # rotated_img = img.rotate(45, expand=True)
            
            # 裁剪图片
            cropped_img = rotated_img.crop(crop_box)
            
            # 保存裁剪后的图片
            cropped_img.save(os.path.join(output_folder, filename))

print("批量旋转并裁剪完成！")
