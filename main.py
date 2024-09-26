from function.judgement import loop_judgement  # 引入图片比较算法
from function.split import split  # 引入图片分割算法

if __name__ == '__main__':
    # 示例用法
    image_path = "./image/source/pre/123.png"  # 原始图像路径
    output_dir = "./image/output"  # 存储分割块的目录
    rows = 20  # 分割行数
    cols = 20  # 分割列数

    split(image_path, output_dir, rows, cols)
    # 在输出结果中和现在的图片进行循环比较，并输出最有可能的位置
    # 输入局部图片的位置
    loop_judgement("./image/source/part/img.png", rows, cols)
