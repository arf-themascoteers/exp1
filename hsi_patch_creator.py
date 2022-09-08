import os

import numpy as np
import rasterio
from PIL import Image
import shutil

src_dir = "data/EO1H0940852016239110K1_1T"
dest_dir = "data/out/hsi_patches"
merged = "data/out/merged/hsi.tif"
soc_file = r'data/out/soc/000_005.tif'
csv_path = "data/out/hsi_csv.csv"

PATCH_WIDTH = 3
PATCH_HEIGHT = 3
STRIDE = 3

def create_csv():
    patch_number = 0
    with rasterio.open(soc_file, 'r') as soc_dataset:
        with rasterio.open(merged, 'r') as merged_hsi_dataset:
            merged_hsi_data = merged_hsi_dataset.read(1)
            soc_data = soc_dataset.read(1)
            soc_height = soc_data.shape[0]
            soc_width = soc_data.shape[1]

            soc_height_ratio = soc_height / merged_hsi_data.shape[0]
            soc_width_ratio = soc_width / merged_hsi_data.shape[1]

            csv_file = open(csv_path, "w")
            row = f"id,soc\n"
            csv_file.write(row)

            windows = []

            top_left_x = 0
            top_left_y = 0
            bot_right_y = PATCH_HEIGHT
            height = merged_hsi_data.shape[0]
            width = merged_hsi_data.shape[1]
            while True:
                bot_right_x = top_left_x + PATCH_WIDTH
                if bot_right_x > width - 1:
                    top_left_x = 0
                    top_left_y = top_left_y + STRIDE
                    bot_right_y = top_left_y + PATCH_HEIGHT
                    continue
                if bot_right_y > height - 1:
                    break
                image = merged_hsi_data[top_left_y:bot_right_y, top_left_x:bot_right_x]
                if is_valid(image):
                    windows.append((top_left_y, bot_right_y, top_left_x, bot_right_x))
                    soc = eval_soc(soc_data, soc_height_ratio, soc_width_ratio, top_left_y, bot_right_y, top_left_x, bot_right_x)
                    row = f"{patch_number},{soc}\n"
                    csv_file.write(row)
                    patch_number = patch_number + 1
                top_left_x = top_left_x + STRIDE

    csv_file.close()
    print("CSV done")
    return windows

def patchify():
        windows = create_csv()
        create_patches(windows)
        print("All Done")

def is_valid(image):
    if 0 in image:
        return False
    return True


def eval_soc(soc_data, soc_height_ratio, soc_width_ratio, top_left_y, bot_right_y, top_left_x, bot_right_x):
    soc_top_left_y = round(soc_height_ratio * top_left_y)
    soc_bot_right_y = round(soc_height_ratio * bot_right_y)
    soc_top_left_x = round(soc_width_ratio * top_left_x)
    soc_bot_right_x = round(soc_width_ratio * bot_right_x)
    if soc_top_left_x == soc_bot_right_x:
        soc_bot_right_x = soc_bot_right_x + 1
    if soc_top_left_y == soc_bot_right_y:
        soc_bot_right_y = soc_bot_right_y + 1
    soc_patch = soc_data[soc_top_left_y:soc_bot_right_y, soc_top_left_x:soc_bot_right_x]
    return np.mean(soc_patch)


def create_patches(windows):
    for file in os.listdir(src_dir):
        patch_number = 0
        src = os.path.join(src_dir, file)
        tokens = file.split("_")
        a_token = tokens[1]
        band_dir_name = str(int(a_token[1:]))
        band_dir = os.path.join(dest_dir, band_dir_name)

        if os.path.exists(band_dir):
            shutil.rmtree(band_dir)

        os.mkdir(band_dir)

        with rasterio.open(src, 'r') as dataset:
            data = dataset.read(1)
            for window in windows:
                image = data[window[0]:window[1], window[2]:window[3]]
                dest_file = os.path.join(band_dir, str(patch_number)+".png")
                im = Image.fromarray(image)
                im.save(dest_file)
                patch_number = patch_number + 1

        print(f"Done {file}")



patchify()

