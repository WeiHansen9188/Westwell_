from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

def get_image_metadata(image_path):
    """ 读取图片的元数据 """
    metadata = {}

    # 打开图片
    try:
        img = Image.open(image_path)
        metadata["文件名"] = os.path.basename(image_path)
        metadata["格式"] = img.format
        metadata["分辨率"] = img.size  # (宽, 高)
        metadata["颜色模式"] = img.mode

        # 获取 EXIF 数据
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value

        return metadata
    except Exception as e:
        print(f"读取图片失败: {e}")
        return None

# 测试
image_file = "2_frames_output/frame_2120.jpg"  # 替换为你的图片路径
metadata = get_image_metadata(image_file)

if metadata:
    for key, value in metadata.items():
        print(f"{key}: {value}")
