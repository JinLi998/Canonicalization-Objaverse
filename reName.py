import os

# 定义根路径
root_dir = r"E:/projects/Canonicalization-Objaverse/videos"
# print('111111111111')
# asdf
# 遍历根路径下的每个子文件夹
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    
    # 确保是一个文件夹
    if os.path.isdir(folder_path):
        # 获取文件夹中的所有mp4文件
        video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
        
        # 对文件列表进行排序，以确保重命名时顺序一致
        video_files.sort()

        # 确保文件夹中有5个视频文件
        if len(video_files) == 5:
            for i, video_file in enumerate(video_files):
                old_file_path = os.path.join(folder_path, video_file)
                new_file_name = f"{i}.mp4"
                new_file_path = os.path.join(folder_path, new_file_name)
                
                # 重命名文件
                os.rename(old_file_path, new_file_path)
                
                # 打印出相对路径
                relative_path = os.path.relpath(new_file_path, start=os.path.join(root_dir, ".."))
                print(relative_path)
        else:
            print(f"Warning: The folder '{folder_name}' does not contain exactly 5 MP4 files.")
