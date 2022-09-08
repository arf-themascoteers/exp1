import os

import numpy as np
import rasterio
from PIL import Image
import shutil

src_dir = "data/EO1H0940852016239110K1_1T"
dest_dir = "data/out/hsi_patches"
merged = "data/out/merged/hsi.tif"
soc = r'data/out/soc/000_005.tif'
csv_path = "data/out/csv.csv"

PATCH_WIDTH = 32
PATCH_HEIGHT = 32
STRIDE = 16


def patchify():
    with rasterio.open(merged, 'r') as dataset:
        data = dataset.read(1)
        with rasterio.open(soc, 'r') as soc_dataset:
            soc_data = soc_dataset.read(1)
            create_patches(data, soc_data)

def is_valid(image, top_left_y, bot_right_y, top_left_x, bot_right_x):
    image = image[top_left_y:bot_right_y, top_left_x:bot_right_x]
    if 0 in image:
        return False
    return True


def eval_soc(soc_data, soc_height_ratio, soc_width_ratio, top_left_y, bot_right_y, top_left_x, bot_right_x):
    soc_top_left_y = int(soc_height_ratio * top_left_y)
    soc_bot_right_y = int(soc_height_ratio * bot_right_y)
    soc_top_left_x = int(soc_width_ratio * top_left_x)
    soc_bot_right_x = int(soc_width_ratio * bot_right_x)
    soc_patch = soc_data[soc_top_left_y:soc_bot_right_y, soc_top_left_x:soc_bot_right_x]
    return np.mean(soc_patch)


def create_patches(merged, soc_data):
    soc_height = soc_data.shape[0]
    soc_width = soc_data.shape[1]

    soc_height_ratio = soc_height / merged.shape[0]
    soc_width_ratio = soc_width / merged.shape[1]

    csv_file = open(csv_path, "w")
    row = f"id,soc\n"
    csv_file.write(row)
    band = 0

    for file in os.listdir(src_dir):
        band = band + 1
        patch_number = 0
        src = os.path.join(src_dir, file)
        tokens = file.split(".")
        band_dir_name = tokens[0]
        band_dir = os.path.join(dest_dir, band_dir_name)

        if os.path.exists(band_dir):
            shutil.rmtree(band_dir)

        os.mkdir(band_dir)

        with rasterio.open(src, 'r') as dataset:
            data = dataset.read(1)
            top_left_x = 0
            top_left_y = 0
            bot_right_y = PATCH_HEIGHT
            height = data.shape[0]
            width = data.shape[1]
            while True:
                bot_right_x = top_left_x + PATCH_WIDTH
                if bot_right_x > width - 1:
                    top_left_x = 0
                    top_left_y = top_left_y + STRIDE
                    bot_right_y = top_left_y + PATCH_HEIGHT
                    continue
                if bot_right_y > height - 1:
                    break
                image = data[top_left_y:bot_right_y, top_left_x:bot_right_x]
                if is_valid(merged, top_left_y, bot_right_y, top_left_x, bot_right_x):
                    patch_number = patch_number + 1
                    dest_file = os.path.join(band_dir, str(patch_number)+".png")
                    im = Image.fromarray(image)
                    im.save(dest_file)
                    if band == 1:
                        soc = eval_soc(soc_data, soc_height_ratio, soc_width_ratio, top_left_y,bot_right_y, top_left_x,bot_right_x)
                        row = f"{patch_number},{soc}\n"
                        csv_file.write(row)

                top_left_x = top_left_x + STRIDE

        print(f"Done {file}")

    csv_file.close()

patchify()

