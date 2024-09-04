"""
# 大量图片的拼接
# 1. unaligned pics 拼接成矩形
# 2. aligned pics 拼接成矩形
# unaligned pics 和 aligned pics 拼成一行
# 头上加进度条，拼成一列
"""

from python.utils.pics_utils import merge_images2Row, merge_images2matrix, create_gradient_bar
from python.utils.vis_utils import visualize_image


if __name__=="__main__":
    # 1. 要拼接的图片的paths
    org_pics_paths = ['imgs/vis_alignCourse/bicycle/aligned_newObj_ins_0_combined.png',
        'imgs/vis_alignCourse/bicycle/aligned_newObj_ins_1_combined.png',
        'imgs/vis_alignCourse/bicycle/aligned_newObj_ins_2_combined.png',
        'imgs/vis_alignCourse/bicycle/aligned_newObj_ins_3_combined.png']
    
    aligned_pics_paths = ['imgs/vis_alignCourse/shoulder_bag/temp_ins_0000_combined.png',
        'imgs/vis_alignCourse/shoulder_bag/temp_ins_0000_combined.png',
        'imgs/vis_alignCourse/shoulder_bag/temp_ins_0000_combined.png',
        'imgs/vis_alignCourse/shoulder_bag/temp_ins_0000_combined.png']
    
    save_dir = 'result/test'

    # 2. 将图片拼接成矩形
    org_merged_image = merge_images2matrix(org_pics_paths, output_pic_path='result/test/aligned_newObj_ins_combined.png')
    aligned_merged_image = merge_images2matrix(aligned_pics_paths, output_pic_path='result/test/temp_ins_0000_combined.png')
    
    # 3. 将拼接后的图片拼接成一行
    org_aligned_image = merge_images2Row([org_merged_image, aligned_merged_image], output_pic_path='result/test/org_aligned_combined.png')

    # 3. 加上title bar and name concate
    create_gradient_bar('result/test/temp_ins_0000_combined.png', 'unaligned', 'result/test/title_red.png', spacing=15)
    create_gradient_bar('result/test/aligned_newObj_ins_combined.png', 'aligned', 'result/test/title_blue.png', start_color=(255, 255, 255), end_color=(214, 244, 242), spacing=15)


