"""将视频拼接成一行
"""

import os
from moviepy.editor import VideoFileClip, clips_array

from python.utils.pics_utils import concatenate_videos_side_by_side

def process_videos(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4') and 'semantic' not in filename:
            base_name = os.path.splitext(filename)[0]
            semantic_filename = f"{base_name}_semantic.mp4"
            semantic_filepath = os.path.join(input_dir, semantic_filename)
            
            # 检查是否存在相应的 '_semantic' 文件
            if os.path.exists(semantic_filepath):
                original_filepath = os.path.join(input_dir, filename)
                output_filepath = os.path.join(output_dir, f"{base_name}_combined.mp4")
                
                # 拼接视频并保存到输出目录
                concatenate_videos_side_by_side(original_filepath, semantic_filepath, output_filepath)
                print(f"Created: {output_filepath}")

# 使用示例
# ['bicycle', 'chair', 'giraffe', 'rifle', 'shoulder_bag']
input_directory = "C:/Users/12147/Desktop/objaverse/vis_alignCourse/shoulder_bag"  # 输入目录
output_directory = "imgs/vis_alignCourse/shoulder_bag"  # 输出目录

process_videos(input_directory, output_directory)