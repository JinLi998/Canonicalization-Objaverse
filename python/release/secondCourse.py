"""对第二次处理的结果进行素材的制作
"""

import os

from python.utils.pics_utils import merge_images2Row, create_gradient_bar
from python.utils.pics_utils import image_to_video, create_gradient_bar_video, add_videos_in_row

def pics2video(before_pics_paths, after_pics_paths, save_path, red_title='', blue_title='', use_num=None):
    before_pics_paths.sort()
    after_pics_paths.sort()
    if use_num:
        before_pics_paths = before_pics_paths[:use_num]
        after_pics_paths = after_pics_paths[:use_num]
    # 1. 分别拼成了行
    before_merged_image = merge_images2Row(before_pics_paths, output_pic_path=os.path.join(os.path.dirname(save_path), 'before_combined.png'))
    after_merged_image = merge_images2Row(after_pics_paths, output_pic_path=os.path.join(os.path.dirname(save_path), 'after_combined.png'))

    # 2. 加上不同颜色的title
    create_gradient_bar(os.path.join(os.path.dirname(save_path), 'before_combined.png'), red_title, os.path.join(os.path.dirname(save_path), 'title_red.png'), spacing=15, font_size=50)
    create_gradient_bar(os.path.join(os.path.dirname(save_path), 'after_combined.png'), blue_title, os.path.join(os.path.dirname(save_path), 'title_blue.png'), start_color=(255, 255, 255), end_color=(214, 244, 242), spacing=15, font_size=50)

    # 3. 两行合并成一行
    merge_images2Row([os.path.join(os.path.dirname(save_path), 'title_red.png'), os.path.join(os.path.dirname(save_path), 'title_blue.png')], output_pic_path=os.path.join(os.path.dirname(save_path), 'beforeAfter_combined.png'))

    # 4. 图片转视频
    image_to_video(os.path.join(os.path.dirname(save_path), 'beforeAfter_combined.png'), save_path)

    # 5. 删除中间文件
    os.remove(os.path.join(os.path.dirname(save_path), 'before_combined.png'))
    os.remove(os.path.join(os.path.dirname(save_path), 'after_combined.png'))
    os.remove(os.path.join(os.path.dirname(save_path), 'title_red.png'))
    os.remove(os.path.join(os.path.dirname(save_path), 'title_blue.png'))
    os.remove(os.path.join(os.path.dirname(save_path), 'beforeAfter_combined.png'))

def video2video(obj_video_paths, semantic_video_paths, save_path, red_title='', blue_title='', use_num=None):
    # 排序
    obj_video_paths.sort()
    semantic_video_paths.sort()
    if use_num:
        obj_video_paths = obj_video_paths[:use_num]
        semantic_video_paths = semantic_video_paths[:use_num]
    # 1. 分别拼成了行
    add_videos_in_row(obj_video_paths, output_path=os.path.join(os.path.dirname(save_path), 'obj_course.mp4'))
    add_videos_in_row(semantic_video_paths, output_path=os.path.join(os.path.dirname(save_path), 'semantic_course.mp4'))
    '''# 2. 加上不同颜色的title
    create_gradient_bar_video(os.path.join(os.path.dirname(save_path), 'obj_course.mp4'), red_title, os.path.join(os.path.dirname(save_path), 'title_red.mp4'), font_size=50)  # , spacing=15
    asdf'''
    # 3. 两行合并成一行
    add_videos_in_row([os.path.join(os.path.dirname(save_path), 'obj_course.mp4'), os.path.join(os.path.dirname(save_path), 'semantic_course.mp4')], output_path=save_path)

    # 4. 删除中间文件
    os.remove(os.path.join(os.path.dirname(save_path), 'obj_course.mp4'))
    os.remove(os.path.join(os.path.dirname(save_path), 'semantic_course.mp4'))




# 对图片拼接的处理
def main(cate_root, save_dir):
    files = os.listdir(cate_root)
    # 1. pics to video
    # 1.1 读取路径下的所有以'.png'结尾的文件，根据是否存在字符'_semantic'分为两个list，并排序
    obj_pics = [f for f in files if f.endswith('.png') and '_semantic' not in f and 'temp' not in f]
    semantic_pics = [f for f in files if f.endswith('.png') and '_semantic' in f and 'temp' not in f]
    # print('org_pics:', org_pics)
    # print('semantic_pics:', semantic_pics)
    
    # 2. org 和 align的obj
    org_obj_pics_paths = [os.path.join(cate_root, f) for f in obj_pics if 'org_' in f]
    align_obj_pics_paths = [os.path.join(cate_root, f) for f in obj_pics if 'aligned_' in f]
    # 如果超过5个，只取前5个
    pics2video(org_obj_pics_paths, align_obj_pics_paths, os.path.join(save_dir, 'objBeforeAfter.mp4'), \
               red_title='Initial Objects', blue_title='Canonical Objects', use_num=5)
    # 3. org 和 align的semantic
    org_semantic_pics_paths = [os.path.join(cate_root, f) for f in semantic_pics if 'org_' in f]
    align_semantic_pics_paths = [os.path.join(cate_root, f) for f in semantic_pics if 'aligned_' in f]
    # 如果超过5个，只取前5个
    pics2video(org_semantic_pics_paths, align_semantic_pics_paths, os.path.join(save_dir, 'semanticBeforeAfter.mp4'), \
               red_title='Initial Semantic', blue_title='Canonical Semantic', use_num=5)
    
    # 4. org 和 align的obj和semantic 的mp4视频
    obj_mp4s = [f for f in files if f.endswith('.mp4') and 'temp' not in f and '_semantic' not in f]
    semantic_mp4s = [f for f in files if f.endswith('.mp4') and 'temp' not in f and '_semantic' in f]
    obj_mp4s = [os.path.join(cate_root, f).replace('\\', '/') for f in obj_mp4s]
    semantic_mp4s = [os.path.join(cate_root, f).replace('\\', '/') for f in semantic_mp4s]
 
    video2video(obj_mp4s, semantic_mp4s, os.path.join(save_dir, 'obj_semantic.mp4'), \
                red_title='Object Canonical Transformation', blue_title='Semantic Canonical Transformation', use_num=5)



    

    


if __name__ == '__main__':
    data_root = 'result/alignedCourse/secondBatch/'
    save_root = 'result/alignedCourse/secondBatch_video'
    cates = os.listdir(data_root)
    

    for cate in cates:  # 每个类别拼成一个，如果需要在拼成一个大的就行了
        cate_root = os.path.join(data_root, cate)
        save_cate_root = os.path.join(save_root, cate)
        if not os.path.exists(save_cate_root):
            os.makedirs(save_cate_root)
        main(cate_root, save_cate_root)

        