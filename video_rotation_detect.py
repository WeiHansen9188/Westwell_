from pymediainfo import MediaInfo

#第二步 检测视频的旋转方向

# 因为导出的图片都有旋转90度 所以要写一个脚本检测
# 该脚本为正确脚本 用于检测视频的旋转方向

def check_video_rotation(video_path):
    """ 使用 MediaInfo 检测视频旋转角度 """
    media_info = MediaInfo.parse(video_path)
    
    rotation = None
    for track in media_info.tracks:
        if track.track_type == "Video" and hasattr(track, "rotation"):
            rotation = float(track.rotation)  # 确保是浮点数
            break  # 只需要第一个 Video track 的旋转角度
    
    # 处理旋转角度
    if rotation is None:
        print("✅ 视频 **没有旋转信息**（可能未旋转）")
    elif rotation == 90:
        print("🔄 视频 **顺时针旋转 90°**")
    elif rotation == 180:
        print("🔄 视频 **旋转 180°**（倒置）")
    elif rotation == 270:
        print("🔄 视频 **逆时针旋转 90°**")
    else:
        print(f"⚠️ 未知旋转角度: {rotation}°，请检查视频元数据")

# 测试
video_file = "your_video.mp4"  # 修改为你的视频路径
check_video_rotation(video_file)
