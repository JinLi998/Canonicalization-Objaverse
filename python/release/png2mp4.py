"""功能，将单张的图片转换成mp4
"""

from PIL import Image
import imageio
import numpy as np

def image_to_video(image_path, save_video_path, duration=5, fps=24):
    # 读取图像
    image = Image.open(image_path)

    # 调整图像大小，使其宽度和高度都是16的倍数
    new_width = (image.width // 16) * 16
    new_height = (image.height // 16) * 16
    image = image.resize((new_width, new_height), Image.LANCZOS)

    # 确定每一帧的持续时间（以秒为单位）
    total_frames = duration * fps

    # 将 PIL 图像转为 NumPy 数组
    image_array = np.array(image.convert("RGB"))

    # 创建视频写入器
    writer = imageio.get_writer(save_video_path, fps=fps)

    # 将图像写入视频文件
    for _ in range(total_frames):
        writer.append_data(image_array)

    writer.close()
    print(f"Video saved successfully as {save_video_path}")

if __name__=="__main__":
    # 使用示例
    image_path = 'result/test/title_blue.png'  # 输入图片路径
    video_name = 'result/test/title_blue.mp4'  # 输出视频文件名
    image_to_video(image_path, video_name, duration=5, fps=24)

