import cv2
import os

# 第一步（方法一）：读取并且导出视频的每一帧
#方法二就是读取特定视频帧 详见1.1.py 更加节省资源

# 设置视频路径
VIDEO_PATH = "your_video.mp4"  # 修改为你的本地视频路径
OUTPUT_FOLDER = "try_frames_output"  # 你希望保存帧的文件夹

# 创建输出文件夹（如果不存在）
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# 读取视频
cap = cv2.VideoCapture(VIDEO_PATH)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 读取完毕，退出循环

    # 保存当前帧
    frame_filename = os.path.join(OUTPUT_FOLDER, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"Saved: {frame_filename}")

    frame_count += 1

cap.release()
print(f"✅ 提取完成，共提取 {frame_count} 帧！")
