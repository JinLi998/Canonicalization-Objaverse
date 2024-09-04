
import os
from PIL import Image, ImageDraw, ImageFont
# from moviepy.editor import VideoFileClip, clips_array
from moviepy.editor import VideoFileClip, clips_array, CompositeVideoClip
import moviepy.editor as mp
import math
import imageio
import numpy as np
from moviepy.video.VideoClip import ColorClip
import cv2


####################图片处理###################
# 给图片上生成渐变条和文字
def create_gradient_bar(image_path, title, save_path, font_size=40, start_color=(250, 219, 223), end_color=(255, 255, 255), spacing=10):
    # 打开原始图像
    image = Image.open(image_path)
    width, height = image.size
    
    # 创建渐变颜色条的图像
    gradient_bar_height = 100  # 你可以根据需要调整高度
    gradient_bar = Image.new("RGB", (width, gradient_bar_height))
    
    # 绘制渐变颜色
    draw = ImageDraw.Draw(gradient_bar)
    for x in range(width):
        # 计算当前x位置的颜色
        r = int(start_color[0] + (end_color[0] - start_color[0]) * x / width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * x / width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * x / width)
        draw.line([(x, 0), (x, gradient_bar_height)], fill=(r, g, b))
    
    # 加载字体
    try:
        font = ImageFont.truetype("times.ttf", font_size)
    except IOError:
        print("Font file not found. Please ensure you have the Times New Roman font installed.")
        return
    
    # 在渐变颜色条上写上标题
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_position = ((width - text_width) // 2, (gradient_bar_height - text_height) // 2)
    
    draw.text(text_position, title, font=font, fill="black", stroke_width=2, stroke_fill="white")
    
    # 将颜色条和原图像进行拼接
    new_image = Image.new("RGB", (width, height + gradient_bar_height + spacing), "white")
    new_image.paste(gradient_bar, (0, 0))
    new_image.paste(image, (0, gradient_bar_height + spacing))
    
    # 保存或显示新图像
    # new_image.show()
    new_image.save(save_path)

# 拼接多张图片 拼成一行
def merge_images2Row(*images_or_paths, spacing=10, output_pic_path=None):
    """
    将多张图片拼接成一张图片。可以接受图片路径或Image对象。

    :param images_or_paths: 要拼接的图片路径或Image对象
    :param spacing: 图片之间的间隔
    :param output_pic_path: 输出图片的路径
    """
    images = []

    # 处理输入，判断是图像路径还是Image对象
    for item in images_or_paths[0]:
        if isinstance(item, str) and os.path.exists(item):  # 如果是路径且文件存在
            images.append(Image.open(item))
        elif isinstance(item, Image.Image):  # 如果是Image对象
            images.append(item)
        else:
            raise ValueError(f"Unsupported input: {item}")

    # 获取所有图片的宽度和高度
    widths, heights = zip(*(img.size for img in images))

    # 计算合并后的图片宽度和高度
    total_width = sum(widths) + spacing * (len(images) - 1)
    max_height = max(heights)
    
    # 创建一个新的空白图片
    merged_image = Image.new('RGB', (total_width, max_height), (255, 255, 255))

    # 将所有图片拼接到新图片上
    x_offset = 0
    for img in images:
        y_offset = (max_height - img.size[1]) // 2  # 垂直居中
        merged_image.paste(img, (x_offset, y_offset))
        x_offset += img.size[0] + spacing

    # 如果指定了输出路径，则保存图片
    if output_pic_path:
        merged_image.save(output_pic_path)

    # # 使用matplotlib显示合并后的图片
    # plt.imshow(merged_image)
    # plt.axis('off')  # 不显示坐标轴
    # plt.show()

    '''# 创建一个窗口，用于显示图片并支持按 ESC 退出
    fig, ax = plt.subplots()
    ax.imshow(merged_image)
    ax.axis('off')  # 不显示坐标轴

    def on_key(event):
        if event.key == 'escape':
            plt.close(fig)

    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()'''
    return merged_image

# 拼成一个矩阵
def merge_images2matrix(images_or_paths, spacing=10, output_pic_path=None):
    """
    Merge multiple images into a single image arranged in a grid. Accepts image paths or Image objects.

    :param images_or_paths: The paths of images or Image objects to be merged
    :param spacing: The spacing between images
    :param output_pic_path: The output path for the merged image
    """
    images = []

    # Handle input, checking if it's an image path or an Image object
    for item in images_or_paths:
        if isinstance(item, str) and os.path.exists(item):  # If it's a valid path
            images.append(Image.open(item))
        elif isinstance(item, Image.Image):  # If it's an Image object
            images.append(item)
        else:
            raise ValueError(f"Unsupported input: {item}")

    # Get the width and height of all images
    widths, heights = zip(*(img.size for img in images))

    # Calculate the number of images
    num_images = len(images)

    # Calculate the number of rows and columns for the best fit grid layout
    cols = math.ceil(math.sqrt(num_images))
    rows = math.ceil(num_images / cols)

    # Calculate the maximum width and height of a single grid cell
    max_width = max(widths)
    max_height = max(heights)

    # Calculate the total width and height of the merged image
    total_width = cols * max_width + (cols - 1) * spacing
    total_height = rows * max_height + (rows - 1) * spacing

    # Create a new blank image
    merged_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

    # Place all images into the new image according to the grid layout
    for i, img in enumerate(images):
        row = i // cols
        col = i % cols

        x_offset = col * (max_width + spacing)
        y_offset = row * (max_height + spacing)

        # 打印出每个图片的位置 和对应的图片名字
        # print(f"Image {os.path.basename(images_or_paths[i])} at row {row+1}, column {col+1}")

        merged_image.paste(img, (x_offset, y_offset))

    # Save the image if an output path is specified
    if output_pic_path:
        merged_image.save(output_pic_path)

    return merged_image


####################视频处理###################
'''def concatenate_videos_side_by_side(video1_path, video2_path, output_path):  # 拼接两个
    # 打开两个视频文件
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)
    
    # 确保两个视频的高度一致，如果不一致，可以选择缩放较小的视频
    if video1.size[1] != video2.size[1]:
        video2 = video2.resize(height=video1.size[1])

    # 将两个视频水平拼接在一起（一个在左边，一个在右边）
    final_video = clips_array([[video1, video2]])
    
    # 将拼接后的新视频保存
    final_video.write_videofile(output_path, codec="libx264", fps=24)'''
def add_videos_in_row(video_paths, space=10, output_path="output_video.mp4"):
    clips = [VideoFileClip(video_path) for video_path in video_paths]
    
    # 获取单个视频的宽度和高度
    width, height = clips[0].size
    
    # 创建带间隔的剪辑数组
    spaced_clips = []
    for clip in clips:
        spaced_clips.append(clip)
        # 添加空白间隔
        if clip != clips[-1]:
            white_space = ColorClip(size=(space, height), color=(255, 255, 255), duration=clip.duration)
            spaced_clips.append(white_space)
    
    # 将所有视频水平排列
    final_clip = clips_array([spaced_clips])
    
    # 输出视频
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

def merge_videos_to_matrix(videos_or_paths, spacing=10, output_video_path=None):
    """
    Merge multiple MP4 videos into a single video arranged in a grid.

    :param videos_or_paths: The paths of videos to be merged
    :param spacing: The spacing between videos
    :param output_video_path: The output path for the merged video
    """
    video_clips = []

    # Handle input, checking if it's a valid video path
    for item in videos_or_paths:
        if isinstance(item, str) and os.path.exists(item):  # If it's a valid path
            video_clips.append(mp.VideoFileClip(item))
        else:
            raise ValueError(f"Unsupported input: {item}")

    # Get the dimensions of all videos
    widths, heights = zip(*(video.size for video in video_clips))

    # Calculate the number of videos
    num_videos = len(video_clips)

    # Calculate the number of rows and columns for the best fit grid layout
    cols = math.ceil(math.sqrt(num_videos))
    rows = math.ceil(num_videos / cols)

    # Calculate the maximum width and height for uniformity
    max_width = max(widths)
    max_height = max(heights)

    # Total dimensions of the merged video
    total_width = cols * max_width + (cols - 1) * spacing
    total_height = rows * max_height + (rows - 1) * spacing

    # Create a blank canvas for the output video
    final_video = mp.VideoFileClip(0, size=(total_width, total_height), duration=1)

    # Place all videos into the new video according to the grid layout
    for i, clip in enumerate(video_clips):
        row = i // cols
        col = i % cols

        x_offset = col * (max_width + spacing)
        y_offset = row * (max_height + spacing)

        # Resize clip to fit the maximum width and height
        resized_clip = clip.resize(newsize=(max_width, max_height))
        final_video = mp.concatenate_videoclips([final_video, resized_clip.set_position((x_offset, y_offset))])

    # Set duration of the final video to the maximum duration of clips
    final_video = final_video.set_duration(max(clip.duration for clip in video_clips))

    # Write the result to the specified output path
    if output_video_path:
        final_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    return final_video
'''# 使用示例
videos = ['video1.mp4', 'video2.mp4', 'video3.mp4']  # 输入视频路径
output_video_path = 'merged_output.mp4'  # 输出视频文件名
merge_videos_to_matrix(videos, output_video_path=output_video_path)'''

# 单张图片转成视频
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

# 给视频生成进度条和文字
from moviepy.editor import ImageClip
from moviepy.editor import TextClip
def create_gradient_bar_video(video_path, title, save_path, font_size=40, start_color=(250, 219, 223), end_color=(255, 255, 255)):
    # 打开原视频
    video = VideoFileClip(video_path)
    width, height = video.size
    
    # 创建渐变颜色条的图像
    gradient_bar_height = 100  # 可以根据需要调整高度
    gradient_bar = Image.new("RGB", (width, gradient_bar_height))
    
    # 绘制渐变颜色
    draw = ImageDraw.Draw(gradient_bar)
    for x in range(width):
        # 计算当前x位置的颜色
        r = int(start_color[0] + (end_color[0] - start_color[0]) * x / width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * x / width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * x / width)
        draw.line([(x, 0), (x, gradient_bar_height)], fill=(r, g, b))
    
    # 将渐变条转换为 NumPy 数组以便与视频合并
    gradient_bar_np = np.array(gradient_bar)
    
    # 创建新的渐变条视频Clip
    gradient_bar_clip = ImageClip(gradient_bar_np).set_duration(video.duration).set_position(("center", height - gradient_bar_height))
    
    # 加载文字Clip
    text_clip = TextClip(title, fontsize=font_size, color='black', size=(width, gradient_bar_height))
    text_clip = text_clip.set_position(("center", height - gradient_bar_height // 2)).set_duration(video.duration)
    
    # 合成视频
    final_video = CompositeVideoClip([video, gradient_bar_clip, text_clip])
    
    # 保存新视频
    final_video.write_videofile(save_path, codec='libx264', fps=video.fps)