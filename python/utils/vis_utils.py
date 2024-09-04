

from PIL import Image
import matplotlib.pyplot as plt


# 可视化图片
def visualize_image(img:Image):
     # 创建一个窗口，用于显示图片并支持按 ESC 退出
    fig, ax = plt.subplots()
    ax.imshow(img)
    # 设置窗口大小
    fig.set_size_inches(22, 9)
    ax.axis('off')  # 不显示坐标轴

    # 初始化 cate_annotation
    cate_annotation = None
    def on_key(event):
        nonlocal cate_annotation  # 声明使用外部变量 cate_annotation
        if event.key == 'escape':
            plt.close(fig)
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
