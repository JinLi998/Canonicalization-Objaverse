### 给原视频加上进度条
from glob import glob
import os
from tqdm import tqdm

from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips
from moviepy.video.fx.all import speedx


# 作用：将视频第一帧和最后一帧定格为4秒
def add_videoRelay(cropped_clip):
    # 获取第一帧和最后一帧的图片
    first_frame_image = cropped_clip.get_frame(0)  # 第一帧
    last_frame_image = cropped_clip.get_frame(cropped_clip.duration - 0.1)  # 最后一帧

    # 将第一帧和最后一帧定格为4秒
    first_frame_clip = ImageClip(first_frame_image).set_duration(4)  # 第一帧定格4秒
    last_frame_clip = ImageClip(last_frame_image).set_duration(4)  # 最后一帧定格4秒

    # 合并视频
    final_clip = concatenate_videoclips([first_frame_clip, cropped_clip, last_frame_clip])
    return final_clip

# 视频拼接函数：空间上将 B 放在 A 的上方
def combine_videos_with_space(video_a_path, video_b_path, output_path, space=5):
    # 加载视频 A 和 B
    video_a = VideoFileClip(video_a_path)
    video_b = VideoFileClip(video_b_path)

    # # 将 B 视频时长设置为与 A 视频相同
    # video_b = video_b.set_duration(video_a.duration)  # -8
    # 将 B 视频的时长调整为与 A 视频相同，通过压缩或拉伸
    duration_a = video_a.duration
    duration_b = video_b.duration
    if duration_b != duration_a:
        video_b = speedx(video_b, final_duration=duration_a-8)

    # 加延时
    video_b = add_videoRelay(video_b)



    # 获取视频 A 和 B 的宽度和高度
    width_a, height_a = video_a.size
    width_b, height_b = video_b.size

    # 如果 B 视频的宽度和 A 不同，将 B 调整为与 A 一样宽
    if width_b != width_a:
        video_b = video_b.resize(width=width_a)

    # 合并两个视频，B 视频在上面，A 视频在下面，中间间隔 5 像素
    final_clip = CompositeVideoClip([
        video_b.set_position(('center', 0)),  # B 放在顶部
        video_a.set_position(('center', height_b + space))  # A 放在下面，并加上 5 像素间隔
    ], size=(width_a, height_a + height_b + space))  # 新视频的总高度是两者高度之和再加上间隔

    # 导出最终合成视频
    final_clip.write_videofile(output_path, codec="libx264", fps=video_a.fps)

if __name__ == "__main__":
    # 处理路径下所有的high350_resized_resized_obj_semantic_clip.mp4
    data_root = 'videos/alignedCourse'
    files = glob(os.path.join(data_root, "**", "high350_resized_resized_obj_semantic_clip.mp4"), recursive=True)
    print(files)
    
    for file in tqdm(files, total=len(files)):
        # 示例调用
        org_path = file # 'result/test/high350_resized_resized_obj_semantic_clip.mp4'
        bar_path = 'result/test/progress_bar_moviepy_pil.mp4'
        # 将file文件名替换为bar_obj_semantic
        save_path = file.replace("high350_resized_resized_obj_semantic_clip.mp4", "bar_obj_semantic.mp4")
        # save_path =  # 'result/test/progress_bar_moviepy_pil_with_space.mp4'
        combine_videos_with_space(org_path, bar_path, save_path, space=5)






# 生成视频进度条
'''from moviepy.editor import VideoClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 颜色渐变函数
def interpolate_color(color1, color2, factor):
    return tuple([int(color1[i] * (1 - factor) + color2[i] * factor) for i in range(3)])

# 生成帧的函数
def make_frame(t, total_duration, width, height):
    # 定义颜色
    red_color = (250, 219, 223)  # 红色
    blue_color = (212, 244, 242)  # 蓝色

    # 计算进度百分比
    progress = t / total_duration

    # 创建图像，初始化为红色
    img = np.full((height, width, 3), red_color, dtype=np.uint8)

    # 计算进度条部分
    progress_width = int(width * progress)
    
    # 生成左侧蓝色进度条部分
    img[:, :progress_width] = blue_color
    
    return img

# 使用 PIL 生成带有文本的 ImageClip
def generate_text_image(text, size, font_size):
    img = Image.new("RGB", size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    try:
        # 尝试使用系统中的 Arial 字体
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # 如果找不到字体，则使用默认字体
        font = ImageFont.load_default()
    
    text_size = draw.textsize(text, font=font)
    text_position = ((size[0] - text_size[0]) // 2, (size[1] - text_size[1]) // 2)
    draw.text(text_position, text, font=font, fill="black")
    
    return np.array(img)

# 视频生成函数
def generate_progress_bar_video(width, height, video_name='progress_bar.mp4', fps=30, duration=10):
    total_duration = duration  # 视频总时长（秒）

    # 创建视频剪辑
    video = VideoClip(lambda t: make_frame(t, total_duration, width, height), duration=total_duration)

    # 使用 PIL 生成文本图片
    # text_img = generate_text_image("Progress Bar", (width, 50), font_size=40)
    # text_clip = ImageClip(text_img).set_duration(total_duration).set_position(('center', 'top'))

    # 合成视频
    final_clip = CompositeVideoClip([video])  # , text_clip

    # 输出为视频文件
    final_clip.write_videofile(video_name, fps=fps)
    print(f"视频已保存为: {video_name}")

# 示例调用
generate_progress_bar_video(640, 40, video_name='result/test/progress_bar_moviepy_pil.mp4', fps=30, duration=10)'''
