import os
from moviepy.editor import VideoFileClip
from glob import glob

def resize_videos_in_directory(directory, output_path, target_width=4880):
    # 如果directory是mp4文件，直接处理
    if directory.endswith('.mp4'):
        video_files = [directory]
    else:
        # 使用 glob 递归查找所有 .mp4 文件
        video_files = glob.glob(os.path.join(directory, '**', '*.mp4'), recursive=True)

    # 遍历所有找到的 .mp4 文件
    for file_path in video_files:
        try:
            # 读取视频文件
            clip = VideoFileClip(file_path)

            # 计算目标高度，保持长宽比
            aspect_ratio = clip.size[1] / clip.size[0]  # 高度/宽度
            new_height = int(target_width * aspect_ratio)

            # 调整视频大小
            resized_clip = clip.resize(width=target_width)

            # 保存调整后的视频
            resized_clip.write_videofile(output_path, codec="libx264")

            # 关闭clip以释放资源
            clip.close()
            resized_clip.close()

            print(f"Processed: {file_path} -> {output_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    # 使用方法，指定文件夹路径
    # directory_path = "E:/projects/Canonicalization-Objaverse/result/alignedCourse/secondBatch_video"
    # resize_videos_in_directory(directory_path)
    data_root = 'videos/alignedCourse'
    # 用glob获得包括子文件夹中所有的mp4文件
    files = glob(os.path.join(data_root, "**", "*.mp4"), recursive=True)
    # resized_objBeforeAfter  resized_semanticBeforeAfter
    files = [f for f in files if "resized_objBeforeAfter" in f or "resized_semanticBeforeAfter" in f]
    # 遍历文件
    for file in files:
        # 获取文件名
        file_name = os.path.basename(file)
        # 获取文件夹名
        folder_name = os.path.basename(os.path.dirname(file))

        # 调用函数
        file = file.replace("\\", "/")
        # 生成输出文件路径，在当前文件夹中以 'resized_' 为前缀保存
        output_path = os.path.join(os.path.dirname(file), f"high350_{os.path.basename(file)}")
        resize_videos_in_directory(file, output_path, target_width=1772)
