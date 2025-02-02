import cv2
import pytesseract
import numpy as np
import os

# 交互式ROI选择
# 这个和manual的区别在于 每次在开始的时候可以选择区域 manual的那个需要输入

# 配置 Tesseract 路径（请修改为本地路径）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 图片文件夹路径（替换为你的路径）
IMAGE_FOLDER = "processed_images/"

# 读取一张图片进行 ROI 选择
sample_image_path = os.path.join(IMAGE_FOLDER, sorted(os.listdir(IMAGE_FOLDER))[0])
sample_image = cv2.imread(sample_image_path)
roi = cv2.selectROI("Select Speed Area", sample_image, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

# ROI 坐标
x, y, w, h = roi
print(f"选定区域: x={x}, y={y}, w={w}, h={h}")

# 记录最高和最低速度
max_speed, min_speed = float('-inf'), float('inf')

# 获取所有图片文件
image_files = sorted([f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))])

for image_file in image_files:
    image_path = os.path.join(IMAGE_FOLDER, image_file)
    
    # 读取图片
    frame = cv2.imread(image_path)
    
    # 裁剪 Speed 数值区域
    speed_region = frame[y:y+h, x:x+w]
    
    # 预处理图像（灰度化 + 二值化增强）
    gray = cv2.cvtColor(speed_region, cv2.COLOR_BGR2GRAY)
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # OCR 识别
    text = pytesseract.image_to_string(binary, config="--psm 7 -c tessedit_char_whitelist=.0123456789kmhKMH/").strip()
    
    # 提取数值部分
    try:
        speed = float(text.split()[0])  # 仅提取数值部分
        max_speed = max(max_speed, speed)
        min_speed = min(min_speed, speed)
        print(f"{image_file}: Detected Speed: {speed} km/h")
    except Exception as e:
        print(f"{image_file}: OCR 识别失败：", text)

print(f"最高速度: {max_speed} km/h")
print(f"最低速度: {min_speed} km/h")
