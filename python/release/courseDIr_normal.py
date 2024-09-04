"""
将对齐过程文件夹下的物体名字重新映射， 乱序的名字变成顺序的。
course dir下面是物体对齐过程中的相关信息，包括，unaligned pic ; unaligned semantic pic ; align pic ; align semantic pic ; to align video ; to align semantic video

"""

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
data_root = 'result/alignedCourse/secondBatch/'
# 获得文件夹下所有文件夹名称
cates = os.listdir(data_root)
for cate in cates:
    directory_path = data_root + cate  # 替换为要处理的目录路径
    remap_filenames(directory_path)