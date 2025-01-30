import os
import cv2
import OCR_init


video_path = "20250130-140429.mp4"


# 读取视频
cap = cv2.VideoCapture(video_path)

# 选取几帧进行预览（均匀分布）
sample_frames = [0, frame_count // 4, frame_count // 2, 3 * frame_count // 4, frame_count - 1]
frames = []

for i, frame_idx in enumerate(sample_frames):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        frame_path = f"/mnt/data/frame_{i}.jpg"
        cv2.imwrite(frame_path, frame)  # 保存帧图片以便后续查看
        frames.append(frame_path)

cap.release()

# 返回提取的帧路径
frames
