'''import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams



def ShowtJittrLagValue():
    colors = [(np.float64(0.17254901960784313), np.float64(0.6274509803921569), np.float64(0.17254901960784313), np.float64(1.0)), (np.float64(0.8392156862745098), np.float64(0.15294117647058825), np.float64(0.1568627450980392), np.float64(1.0)), (np.float64(0.5803921568627451), np.float64(0.403921568627451), np.float64(0.7411764705882353), np.float64(1.0)), (np.float64(0.7686274509803922), np.float64(0.611764705882353), np.float64(0.5803921568627451), np.float64(1.0)),'y','b','c','g', 'r', 'gray', 'm']
    labels = ['ShapeNet','ModelNet','3D-Future','ABO','Toys4K','CO3D','ScanObjectNN', 'GSO', 'AKB-48', 'OmniObject3D', 'Ours']
    #  gt, tr, exp, kalman, sg, oe, nice,
    tSmt = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]
    tLag = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]
    

    config = {
    "font.family":'Times New Roman',
    "font.size": 12,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
    }
    rcParams.update(config)
    
    for i in range (0,len(tSmt)):
        ax = plt.gca()
        plt.scatter(tSmt[i], tLag[i], color = colors[i], label = labels[i])
        plt.xlabel('Classes', fontsize = 16)
        plt.ylabel('Objects (w)',  fontsize = 16)
        plt.xticks(fontsize = 14)
        plt.yticks(fontsize = 14)

    plt.legend()
    plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# def ShowtJittrLagValue():
#     colors = [(np.float64(0.17254901960784313), np.float64(0.6274509803921569), np.float64(0.17254901960784313), np.float64(1.0)), 
#               (np.float64(0.8392156862745098), np.float64(0.15294117647058825), np.float64(0.1568627450980392), np.float64(1.0)), 
#               (np.float64(0.5803921568627451), np.float64(0.403921568627451), np.float64(0.7411764705882353), np.float64(1.0)), 
#               (np.float64(0.7686274509803922), np.float64(0.611764705882353), np.float64(0.5803921568627451), np.float64(1.0)),
#               'y', 'b', 'c', 'g', 'r', 'gray', 'm']
    
#     labels = ['ShapeNet', 'ModelNet', '3D-Future', 'ABO', 'Toys4K', 'CO3D', 'ScanObjectNN', 'GSO', 'AKB-48', 'OmniObject3D', 'Ours']
#     tSmt = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]
#     tLag = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]

#     # 更新配置
#     config = {
#         "font.family": 'Times New Roman',
#         "font.size": 12,
#         "mathtext.fontset": 'stix',
#         "font.serif": ['SimSun'],
#     }
#     rcParams.update(config)
    
#     # 设置替代红色的颜色
#     alternate_color = 'purple'
    
#     for i in range(len(tSmt)):
#         ax = plt.gca()
#         # 如果是 "Ours"，使用红色五角星
#         if labels[i] == 'Ours':
#             plt.scatter(tSmt[i], tLag[i], color='r', marker='*', s=200, label=labels[i])
#         else:
#             # 如果颜色是红色，则替换为 alternate_color
#             current_color = colors[i]
#             if current_color == 'r' or (isinstance(current_color, tuple) and current_color[0] > 0.8 and current_color[1] < 0.2 and current_color[2] < 0.2):
#                 current_color = alternate_color
#             plt.scatter(tSmt[i], tLag[i], color=current_color, label=labels[i])
        
#         plt.xlabel('Classes', fontsize=16)
#         plt.ylabel('Objects (w)', fontsize=16)
#         plt.xticks(fontsize=14)
#         plt.yticks(fontsize=14)

#     plt.legend()
#     plt.grid(True)
#     plt.show()

'''def ShowtJittrLagValue():
    colors = ['gray', 
              (np.float64(0.8392156862745098), np.float64(0.15294117647058825), np.float64(0.1568627450980392), np.float64(1.0)), 
              (np.float64(0.5803921568627451), np.float64(0.403921568627451), np.float64(0.7411764705882353), np.float64(1.0)), 
              (np.float64(0.7686274509803922), np.float64(0.611764705882353), np.float64(0.5803921568627451), np.float64(1.0)),
              'y', 'b', 'c', 'g', 'r', (1.0, 0.647, 0.0), 'm']
    
    labels = ['ShapeNet', 'ModelNet', '3D-Future', 'ABO', 'Toys4K', 'CO3D', 'ScanObjectNN', 'GSO', 'AKB-48', 'OmniObject3D', 'Ours']
    # tSmt = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]
    # tLag = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]
    tLag = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]
    tSmt = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]

    # 更新配置
    config = {
        "font.family": 'Times New Roman',
        "font.size": 14,  # 字体变大
        "mathtext.fontset": 'stix',
        "font.serif": ['SimSun'],
    }
    rcParams.update(config)
    
    # 设置替代红色的颜色
    alternate_color = 'purple'
    
    # 调整图片尺寸，宽度增加一倍
    plt.figure(figsize=(12, 6))  # 原始比例为(6, 6)，这里宽度加倍
    
    for i in range(len(tSmt)):
        ax = plt.gca()
        # 如果是 "Ours"，使用红色五角星，并在下面加上标签
        if labels[i] == 'Ours':
            plt.scatter(tSmt[i], tLag[i], color='r', marker='*', s=300, label=labels[i])  # 点大小增加
            plt.text(tSmt[i], tLag[i] - 90, labels[i], fontsize=16, color='r', weight='bold', ha='center')  # 显示"Ours"在星星下面，增加空隙
        else:
            # 如果颜色是红色，则替换为 alternate_color
            current_color = colors[i]
            if current_color == 'r' or (isinstance(current_color, tuple) and current_color[0] > 0.8 and current_color[1] < 0.2 and current_color[2] < 0.2):
                current_color = alternate_color
            plt.scatter(tSmt[i], tLag[i], color=current_color, s=180, label=labels[i])  # 点大小增加
            # plt.text(tSmt[i], tLag[i] - 0.2, labels[i], fontsize=16, ha='center')  # 显示"Ours"在星星下面，增加空隙
        
        plt.ylabel('Classes', fontsize=18)
        plt.xlabel('Objects (w)', fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

    # 调整图例栏，排成多行，并调整图例字体大小
    plt.legend(ncol=3, fontsize=14, scatterpoints=1)  # 设置为三列，字体更大，图例中点大小变小
    
    plt.grid(True)
    plt.show()
'''


def ShowtJittrLagValue():
    colors = ['gray', 
              (np.float64(0.8392156862745098), np.float64(0.15294117647058825), np.float64(0.1568627450980392), np.float64(1.0)), 
              (np.float64(0.5803921568627451), np.float64(0.403921568627451), np.float64(0.7411764705882353), np.float64(1.0)), 
              (np.float64(0.7686274509803922), np.float64(0.611764705882353), np.float64(0.5803921568627451), np.float64(1.0)),
              'y', 'b', 'c', 'g', 'r', (1.0, 0.647, 0.0), 'm']
    
    labels = ['ShapeNet', 'ModelNet', '3D-Future', 'ABO', 'Toys4K', 'CO3D', 'ScanObjectNN', 'GSO', 'AKB-48', 'OmniObject3D', 'Ours']
    tLag = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]
    tSmt = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]

    # 更新配置
    config = {
        "font.family": 'Times New Roman',
        "font.size": 14,  # 字体变大
        "mathtext.fontset": 'stix',
        "font.serif": ['SimSun'],
    }
    rcParams.update(config)
    
    # 设置替代红色的颜色
    alternate_color = 'purple'
    
    # 调整图片尺寸，适当增加高度给图例留出空间
    plt.figure(figsize=(12, 8))  # 宽度12，高度8，适当增加高度
    
    for i in range(len(tSmt)):
        ax = plt.gca()
        # 如果是 "Ours"，使用红色五角星，并在下面加上标签
        if labels[i] == 'Ours':
            plt.scatter(tSmt[i], tLag[i], color='r', marker='*', s=300, label=labels[i])  # 点大小增加
            plt.text(tSmt[i], tLag[i] - 90, labels[i], fontsize=16, color='r', weight='bold', ha='center')  # 显示"Ours"在星星下面，增加空隙
        else:
            # 如果颜色是红色，则替换为 alternate_color
            current_color = colors[i]
            if current_color == 'r' or (isinstance(current_color, tuple) and current_color[0] > 0.8 and current_color[1] < 0.2 and current_color[2] < 0.2):
                current_color = alternate_color
            plt.scatter(tSmt[i], tLag[i], color=current_color, s=180, label=labels[i])  # 点大小增加
        
        plt.ylabel('Classes', fontsize=18)
        plt.xlabel('Objects (w)', fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

    # 调整图例栏，放到图外的正下方，变成两行，并且宽度和图对齐
    plt.legend(
        ncol=6,  # 设置为三列
        fontsize=14,  # 字体大小
        scatterpoints=1,  # 图例中的点大小
        loc='upper center',  # 图例放在图的下方中央
        bbox_to_anchor=(0.5, -0.15),  # 调整到图外的正下方
        frameon=False  # 去掉图例的边框
    )
    
    plt.grid(True)
    plt.tight_layout(rect=[0, 0, 1, 0.9])  # 调整图形布局，给图例留出空间
    plt.show()


if __name__ == "__main__":
    ShowtJittrLagValue()
    '''# 使用 colormap 生成新的颜色
    num_new_colors = 10  # 生成 7 到 11 个新颜色，这里我们选择生成10个
    cmap = plt.get_cmap('tab20')  # 'tab20' 是一种分布较好的颜色映射
    new_colors = [cmap(i) for i in np.linspace(0, 1, num_new_colors)]
    print(new_colors)'''

'''# 表格A和表格B的数据
datasets = ['ShapeNet', 'ModelNet', '3D-Future', 'ABO', 'Toys4K', 'CO3D', 'ScanObjectNN', 'GSO', 'AKB-48', 'OmniObject3D', 'Ours']
classes = [55, 40, 34, 63, 105, 50, 15, 17, 48, 190, 1156]  # 表格A数据 (X轴)
objects = [5.1, 1.2, 1.6, 0.8, 0.4, 1.9, 1.5, 0.1, 0.2, 0.6, 4.6]  # 表格B数据 (Y轴)

# 创建散点图
plt.figure(figsize=(8, 6))
plt.scatter(classes, objects, color=['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta', 'yellow'], s=100)

# 添加数据标签
for i, dataset in enumerate(datasets):
    plt.text(classes[i], objects[i], dataset, fontsize=12, ha='right')

# 设置坐标轴标签和标题
plt.xlabel('Classes', fontsize=14)
plt.ylabel('Objects (w)', fontsize=14)
plt.title('Scatter Plot of Classes vs Objects (w)', fontsize=16)

# 显示网格
plt.grid(True)

# 保存图像到指定路径
output_path = "result/test/scatter_plot.png"  # 你可以更改路径到你希望的位置
plt.savefig(output_path)

# 显示图像
plt.show()'''
