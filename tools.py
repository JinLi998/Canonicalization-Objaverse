'''
#####图片的拼接
import os
from PIL import Image

def concatenate_images(image1_path, image2_path, output_path):
    # 打开两张图片
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
    # 确保两张图片的高度一致，可以选择是水平或垂直拼接，这里我们水平拼接
    if image1.height != image2.height:
        image2 = image2.resize((int(image2.width * image1.height / image2.height), image1.height))

    # 创建一个新的图片，宽度是两张图片宽度的总和，高度是两张图片的高度（这里相同）
    new_image = Image.new('RGB', (image1.width + image2.width, image1.height))
    
    # 将两张图片粘贴到新图片上
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    
    # 保存新图片
    new_image.save(output_path)

def process_images(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.png') and 'semantic' not in filename:
            base_name = os.path.splitext(filename)[0]
            semantic_filename = f"{base_name}_semantic.png"
            semantic_filepath = os.path.join(input_dir, semantic_filename)
            
            # 检查是否存在相应的 '_semantic' 文件
            if os.path.exists(semantic_filepath):
                original_filepath = os.path.join(input_dir, filename)
                output_filepath = os.path.join(output_dir, f"{base_name}_combined.png")
                
                # 拼接图片并保存到输出目录
                concatenate_images(original_filepath, semantic_filepath, output_filepath)
                print(f"Created: {output_filepath}")

# 使用示例
# ['bicycle', 'chair', 'giraffe', 'rifle', 'shoulder_bag']
input_directory = "C:/Users/12147/Desktop/objaverse/vis_alignCourse/shoulder_bag"  # 输入目录
output_directory = "imgs/vis_alignCourse/shoulder_bag"  # 输出目录

process_images(input_directory, output_directory)
'''


'''# 视频的拼接
import os
from moviepy.editor import VideoFileClip, clips_array

def concatenate_videos_side_by_side(video1_path, video2_path, output_path):
    # 打开两个视频文件
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)
    
    # 确保两个视频的高度一致，如果不一致，可以选择缩放较小的视频
    if video1.size[1] != video2.size[1]:
        video2 = video2.resize(height=video1.size[1])

    # 将两个视频水平拼接在一起（一个在左边，一个在右边）
    final_video = clips_array([[video1, video2]])
    
    # 将拼接后的新视频保存
    final_video.write_videofile(output_path, codec="libx264", fps=24)

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

process_videos(input_directory, output_directory)'''



import os
import re

import os
import re

def remap_filenames(directory):
    # 获取目录下所有文件名
    files = os.listdir(directory)
    # 过滤掉包含'temp_ins'的
    files = [filename for filename in files if 'temp_ins_' not in filename]
    # 用于存储新的文件名与数字的映射
    number_mapping = {}
    counter = 0

    # 遍历所有文件
    for filename in files:
        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        
        # 查找所有包含 _数字 的部分
        matches = re.findall(r'_(\d+)', name)
        
        # 如果有匹配项，进行映射
        if matches:
            for match in matches:
                if match not in number_mapping:
                    number_mapping[match] = counter
                    counter += 1
                
                # 替换原文件名中的 _数字_ 为新的数字
                name = name.replace(f'_{match}', f'_{number_mapping[match]}')
        
        # 创建新的文件名
        new_name = name + ext
        
        # 修改文件的名称
        original_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        if original_path != new_path:  # 避免重命名为相同的文件名
            os.rename(original_path, new_path)
            print(f'Renamed: {original_path} -> {new_path}')
    
    return

# 使用示例
cates = ['bicycle', 'chair', 'giraffe', 'rifle', 'shoulder_bag']
for cate in cates:
    directory_path = 'imgs/vis_alignCourse/' + cate  # 替换为要处理的目录路径
    remap_filenames(directory_path)


