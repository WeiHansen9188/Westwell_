#方法二 每隔 N 帧提取一张（减少存储）
#一帧是十二分之一秒。 每秒帧数指的就是“每秒播放的画面数”。 就是在1秒钟时间里传输的图片的帧数，也可以理解为图形处理器每秒钟能够刷新几次，通常用fps表示。

import cv2
import os



FRAME_INTERVAL = 10  # 每隔 10 帧提取一次
VIDEO_PATH = "1.mp4"
OUTPUT_FOLDER = "2_frames_output"  # 你希望保存帧的文件夹

# 创建输出文件夹（如果不存在）
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

cap = cv2.VideoCapture(VIDEO_PATH)
frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 视频结束

    if frame_count % FRAME_INTERVAL == 0:  # 每隔 N 帧保存一次
        frame_filename = os.path.join(OUTPUT_FOLDER, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_count += 1
        print(f"Saved: {frame_filename}")

    frame_count += 1

cap.release()
print(f"✅ 提取完成，共保存 {saved_count} 帧！")
