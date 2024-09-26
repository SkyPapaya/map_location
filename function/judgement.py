from PIL import Image
import numpy as np  # 导入 numpy 库
from skimage import metrics
from skimage.transform import resize


def judgement(pre_path, part_path):
    # 打开并调整图像大小
    image1 = Image.open(pre_path)
    image2 = Image.open(part_path)
    image1 = image1.resize((500, 500))  # 调整图像1的大小为500x500
    image2 = image2.resize((500, 500))  # 调整图像2的大小为500x500

    # 将图像转换为灰度图像
    image1_gray = image1.convert("L")
    image2_gray = image2.convert("L")

    # 将图像转换为NumPy数组
    image1_array = np.array(image1_gray)
    image2_array = np.array(image2_gray)

    # 计算结构相似性指数（SSIM）
    similarity = metrics.structural_similarity(image1_array, image2_array)

    # 将相似性指数转换为相似度（范围0到1，值越大表示相似度越高）
    similarity = (similarity + 1) / 2
    return similarity


def loop_judgement(part_path, rows, cols):
    result = {}
    for row in range(rows):
        for col in range(cols):
            # 循环比较每个分割块的相似度
            tile_path = f"./image/output/tile_r{row}_c{col}.png"
            similarity = judgement(part_path, tile_path)
            result[(row, col)] = similarity

    similarity = max(result.values())
    print("最有可能的位置：", [k for k, v in result.items() if v == similarity])
