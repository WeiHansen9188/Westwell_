import cv2

# 这个脚本有点问题 暂时不要用

# 视频文件路径
video_path = "your_video.mp4"

# 读取视频
cap = cv2.VideoCapture(video_path)

# 获取视频基本信息
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ROI窗口参数 (你可以修改)
x, y, w, h = 100, 100, 300, 300  # ROI 窗口 (左上角 x, y, 宽 w, 高 h)

# 播放视频
while cap.isOpened():
    ret, frame = cap.read()  # 读取视频帧
    if not ret:
        break  # 视频播放完毕，退出循环

    # 显示原视频
    cv2.imshow("Video", frame)

    # 截取 ROI (感兴趣区域)
    roi = frame[y:y+h, x:x+w]
    cv2.imshow("ROI", roi)  # 显示ROI窗口

    # 按 'q' 退出
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()

# 打印视频基本信息和 ROI
print(f"帧率 (FPS): {fps}")
print(f"总帧数 (Frame Count): {frame_count}")
print(f"视频分辨率 (Width x Height): {width} x {height}")
print(f"ROI 窗口: x={x}, y={y}, w={w}, h={h}")
