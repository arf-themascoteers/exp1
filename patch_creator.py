import os
import rasterio
from PIL import Image

src_dir = "C:/Users/Administrator/Desktop/exp1/data/out/resized/sat"
dest_dir = "C:/Users/Administrator/Desktop/exp1/data/out/patches"

PATH_WIDTH = 64
PATH_HEIGHT = 64

for file in os.listdir(src_dir):
    patch_number = 1
    src = os.path.join(src_dir, file)
    tokens = file.split(".")
    band_dir_name = tokens[0]
    band_dir = os.path.join(dest_dir, band_dir_name)

    with rasterio.open(src, 'r') as dataset:
        data = dataset.read(1)
        top_left_x = 0
        top_left_y = 0
        bot_right_y = PATH_HEIGHT
        height = data.shape[0]
        width = data.shape[1]
        while True:
            bot_right_x = top_left_x + PATH_WIDTH
            if bot_right_x > width - 1:
                top_left_x = 0
                top_left_y = top_left_y + PATH_HEIGHT
                bot_right_y = top_left_y + PATH_HEIGHT
                continue
            if bot_right_y > height - 1:
                break
            image = data[top_left_y:bot_right_y, top_left_x:bot_right_x]
            dest_file = os.path.join(band_dir, str(patch_number)+".png")

            im = Image.fromarray(image)
            im.save(dest_file)

            print(f"Done creating band {band_dir_name} - patch {patch_number}")
            patch_number = patch_number + 1
            top_left_x = bot_right_x

print("Done all")
