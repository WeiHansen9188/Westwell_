import cv2
import pytesseract
import numpy as np

# 配置 Tesseract 路径（如果本地未自动识别，请修改为自己的路径）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 截图路径
IMAGE_PATH = "processed_images/frame_1120.jpg"  # 替换为你的截图路径

def select_roi(image_path):
    """ 交互式选择 ROI（感兴趣区域），返回 (x, y, w, h) """
    image = cv2.imread(image_path)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 向右旋转90°
    roi = cv2.selectROI("Select Speed Area", image, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    return roi

# 选择窗口区域
x, y, w, h = select_roi(IMAGE_PATH)
print(f"选定区域: x={x}, y={y}, w={w}, h={h}")

# 读取视频
VIDEO_PATH = "20250130-140429.mp4"  # 修改为你的本地视频路径
cap = cv2.VideoCapture(VIDEO_PATH)

# 记录最高和最低速度
max_speed, min_speed = float('-inf'), float('inf')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 结束视频读取
    
    # 旋转帧
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
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
        print(f"Detected Speed: {speed} km/h")
    except Exception as e:
        print("OCR 识别失败：", text)
    
cap.release()
print(f"最高速度: {max_speed} km/h")
print(f"最低速度: {min_speed} km/h")

# 识别成功率
detection_accuracy = (successful_detections / total_frames) * 100 if total_frames > 0 else 0
print(f"最高速度: {max_speed} km/h")
print(f"最低速度: {min_speed} km/h")
print(f"OCR 识别成功率: {detection_accuracy:.2f}%")


# 生成速度曲线
plt.figure(figsize=(10, 5))
plt.plot(time_stamps, speed_values, marker='o', linestyle='-')
plt.xlabel("时间 (秒)")
plt.ylabel("速度 (km/h)")
plt.title("Speed 识别曲线")
plt.grid()
plt.show()
