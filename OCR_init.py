import cv2

# 视频文件路径
video_path = "20250130-140429.mp4"

# 读取视频基本信息
cap = cv2.VideoCapture(video_path)  #video path

# 获取视频的帧率、总帧数和分辨率
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 释放视频对象
cap.release()

# 打印视频基本信息
print(f"帧率 (FPS): {fps}")
print(f"总帧数 (Frame Count): {frame_count}")
print(f"分辨率 (Width x Height): {width} x {height}")
