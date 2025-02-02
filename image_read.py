import cv2

# 解决路径问题
image_path = r"C:\Users\Hansen Wei\Documents\GitHub\Westwell_\processed_images\frame_1070.jpg"

# 读取图片
image = cv2.imread(image_path)

# 检查是否成功读取
if image is None:
    print("无法读取图片，请检查路径是否正确！")
else:
    # 显示图片
    cv2.imshow("Image", image)

    # 等待按键关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
