from PIL import Image
import os

def split(image_path, output_dir, rows, cols):
    # 打开原始图像
    img = Image.open(image_path)
    img_width, img_height = img.size

    # 计算每块的宽度和高度
    tile_width = img_width // cols
    tile_height = img_height // rows

    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 分割图像
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            top = row * tile_height
            right = (col + 1) * tile_width
            bottom = (row + 1) * tile_height

            # 裁剪图像
            tile = img.crop((left, top, right, bottom))

            # 保存分割后的图像
            tile_filename = f"tile_r{row}_c{col}.png"
            tile.save(os.path.join(output_dir, tile_filename))

    print(f"图像已成功分割为 {rows} 行 {cols} 列并保存在 {output_dir} 目录下。")


