import cv2
import numpy as np

# 截图路径
IMAGE_PATH = "processed_images/frame_0920.jpg"  # 替换为你的截图路径

def select_roi(image_path):
   
    image = cv2.imread(image_path)
    clone = image.copy()
    roi = cv2.selectROI("Select Speed Area", image, fromCenter=False, showCrosshair=True)
    
    while True:
        temp = clone.copy()
        cv2.rectangle(temp, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), (0, 255, 0), 2)
        cv2.imshow("Confirm Selection", temp)
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('r'):  # 重新选择
            roi = cv2.selectROI("Select Speed Area", image, fromCenter=False, showCrosshair=True)
        elif key == ord('c'):  # 确认选择
            break
    
    cv2.destroyAllWindows()
    return roi

# 选择窗口区域
x, y, w, h = select_roi(IMAGE_PATH)
print(f"选定区域: x={x}, y={y}, w={w}, h={h}")
