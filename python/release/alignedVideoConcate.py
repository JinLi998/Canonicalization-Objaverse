import os
from tqdm import tqdm
from glob import glob

from python.utils.pics_utils import add_videos_in_row
from python.release.resizeVideo import resize_videos_in_directory

if __name__ == "__main__":
    data_root = "E:/projects/Canonicalization-Objaverse/videos/alignedObjs"
    '''# 用glob获得包括子文件夹中所有的mp4文件
    files = glob(os.path.join(data_root, "**", "*.mp4"), recursive=True)
    print(files)
    asdf'''

    # cates = os.listdir(data_root)

    cates = ['rabbit','race_car', 'raincoat', 'record_player', 'ring', 'shears', 'shepherd_dog', 'shield', 'shoe', 'shopping_cart', 'sink', 'skateboard', 'squirrel', 'tapestry', 'trailer_truck', 'vodka']
    cates = [cates[0]]
    print(cates)
    for cate in tqdm(cates,total=len(data_root)):
        tqdm.write(cate)
        cate_dir = os.path.join(data_root, cates[0])

        # if os.path.exists(os.path.join(cate_dir, "resized_concat.mp4")) is False:
        # 获得路径下以MP4结尾的文件
        video_files = [f for f in os.listdir(cate_dir) if f.endswith('.mp4')]
        videos_paths = [os.path.join(cate_dir, f) for f in video_files]

        add_videos_in_row(videos_paths, space=10, output_path=os.path.join(cate_dir, "concat.mp4"))
        resize_videos_in_directory(os.path.join(cate_dir, "concat.mp4"), target_width=4880)

        # 删除原来的视频
        for video_path in videos_paths:
            os.remove(video_path)
        # os.remove(os.path.join(cate_dir, "concat.mp4"))
        # else:
        #     continue