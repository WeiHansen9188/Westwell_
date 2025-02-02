import cv2
import numpy as np
from matplotlib import pyplot as plt

#正确脚本：灰度处理 对比度增强 去雾 显示增强后的图片


# 读取图像
image_path = "newbestrotatedleft90/frame_0947.jpg"
img = cv2.imread(image_path)

# 1️⃣ 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2️⃣ 进行对比度增强（直方图均衡化）
equalized = cv2.equalizeHist(gray)

# 3️⃣ 去雾（使用 Retinex 方法）
def enhance_contrast(image):
    # 使用高斯模糊创建模糊版
    blur = cv2.GaussianBlur(image, (21, 21), 0)
    # 计算细节增强
    enhanced = cv2.addWeighted(image, 1.5, blur, -0.5, 0)
    return enhanced

enhanced = enhance_contrast(equalized)

# 4️⃣ 显示增强后的图片
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title("原始图片")
plt.subplot(1, 2, 2), plt.imshow(enhanced, cmap='gray'), plt.title("增强后图片")
plt.show()

# 5️⃣ 保存处理后的图片
output_path = "/123123123123123123123/enhanced_image0029.png"
cv2.imwrite(output_path, enhanced)
print(f"增强后的图片已保存：{output_path}")
