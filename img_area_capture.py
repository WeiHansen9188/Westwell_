import cv2

# 读取一帧图像
image_path = "frame_2.jpg"  # 替换为你的截图
image = cv2.imread(image_path)

# 鼠标点击回调函数
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: ({x}, {y})")

# 显示图像，等待点击
cv2.imshow("Click to get coordinates", image)
cv2.setMouseCallback("Click to get coordinates", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
