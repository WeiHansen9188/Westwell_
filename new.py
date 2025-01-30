import cv2
import os

# 1️⃣ 设置视频路径
VIDEO_PATH = "20250130-140429.mp4"  # 修改为你本地的视频路径
OUTPUT_FOLDER = "frames_output"  # 保存帧的文件夹

# 2️⃣ 创建输出文件夹（如果不存在）
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# 3️⃣ 读取视频
cap = cv2.VideoCapture(VIDEO_PATH)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 视频读取完毕

    # 4️⃣ 保存当前帧
    frame_filename = os.path.join(OUTPUT_FOLDER, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"Saved: {frame_filename}")

    frame_count += 1  # 帧计数 +1

cap.release()
print(f"✅ 提取完成，共提取 {frame_count} 帧！")
