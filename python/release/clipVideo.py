import os
from glob import glob

from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips

def process_video(input_path, output_path):
    # 读取输入视频
    clip = VideoFileClip(input_path)

    # 计算裁剪的结束位置
    width, height = clip.size
    space = 5
    crop_x_end = (width // 2) - space  # 裁剪的右边界位置

    # 裁剪视频，保留左半部分
    cropped_clip = clip.crop(x1=0, y1=0, x2=crop_x_end, y2=height)

    # 获取第一帧和最后一帧的图片
    first_frame_image = cropped_clip.get_frame(0)  # 第一帧
    last_frame_image = cropped_clip.get_frame(cropped_clip.duration - 0.1)  # 最后一帧

    # 将第一帧和最后一帧定格为4秒
    first_frame_clip = ImageClip(first_frame_image).set_duration(4)  # 第一帧定格4秒
    last_frame_clip = ImageClip(last_frame_image).set_duration(4)  # 最后一帧定格4秒

    # 合并视频
    final_clip = concatenate_videoclips([first_frame_clip, cropped_clip, last_frame_clip]) # 

    # 导出处理后的视频
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__=="__main__":
    data_root = 'videos/alignedCourse'
    # 用glob获得包括子文件夹中所有的mp4文件
    files = glob(os.path.join(data_root, "**", "*.mp4"), recursive=True)
    # 选出包含resized_obj_semantic的文件
    files = [f for f in files if "resized_obj_semantic" in f]
    # 遍历文件
    for file in files:
        # 获取文件名
        file_name = os.path.basename(file)
        # 获取文件夹名
        folder_name = os.path.basename(os.path.dirname(file))
        # 输出路径
        output_path = os.path.join(os.path.dirname(file), file_name.replace("resized_obj_semantic", "resized_obj_semantic_clip"))
        # 调用函数
        file = file.replace("\\", "/")
        output_path = output_path.replace("\\", "/")
        process_video(file, output_path)


