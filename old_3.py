import cv2
import pytesseract
import numpy as np
import time

# 这个是最原始的OCR识别，但是是基于视频的，识别率反而高，很困惑
# 这个脚本没啥问题 微调一下 只需要选择窗口区域
# 目前 这个脚本会交互式选择ROI感兴趣区域然后自动进行识别 但是我们手动做

#对比这个脚本的参数和manual_image_ocr和selection_image_ocr的

# 配置 Tesseract 路径（如果本地未自动识别，请修改为自己的路径）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 截图路径
IMAGE_PATH = "frame_0761.jpg"  # 替换为你的截图路径

def select_roi(image_path):
    """ 交互式选择 ROI（感兴趣区域），返回 (x, y, w, h) """
    image = cv2.imread(image_path)
    # image = cv2.rotate(image, cv2.ROTATE_90_ANTICLOCKWISE)  # 向右旋转90°
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

total_frames = 0
successful_detections = 0
speed_zero_start_time = None

def detect_popup_window(frame):
    """ 检测是否有新的弹出窗口（可以根据颜色或形状变化） """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours) > 10  # 如果检测到大量轮廓，可能有新窗口

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 结束视频读取
    
    total_frames += 1
    
    # 旋转帧
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
    # 检测弹出窗口
    if detect_popup_window(frame):
        print("检测到新弹出窗口，结束 OCR 识别。")
        break
    
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
        successful_detections += 1
        print(f"Detected Speed: {speed} km/h")
        
        # 记录 Speed 归零的时间
        if speed == 0:
            if speed_zero_start_time is None:
                speed_zero_start_time = time.time()
            elif time.time() - speed_zero_start_time >= 3:
                print("Speed 归零 3 秒，结束 OCR 识别。")
                break
        else:
            speed_zero_start_time = None  # 如果速度不为零，重置计时器
    except Exception as e:
        print("OCR 识别失败：", text)
    
cap.release()

detection_accuracy = (successful_detections / total_frames) * 100 if total_frames > 0 else 0
print(f"最高速度: {max_speed} km/h")
print(f"最低速度: {min_speed} km/h")
print(f"OCR 识别成功率: {detection_accuracy:.2f}%")
