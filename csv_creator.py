import os

import numpy
import rasterio

dim0 = 925
dim1 = 1275
PATCH_WIDTH = 16
PATCH_HEIGHT = 16


def patch_number_to_dims(patch_number):
    patch_number = patch_number - 1

    blocks_x = int(dim1/PATCH_WIDTH)

    row = int(patch_number / blocks_x)
    col = patch_number % blocks_x

    x = col * PATCH_WIDTH
    y = row * PATCH_HEIGHT

    return x,y


dem = r'data/out/dem/dem.tif'
soc = r'data/out/soc/000_005.tif'
patch_dir = "data/out/patches"
csv_path = "data/out/csv.csv"
file = open(csv_path, "w")

patches = len(os.listdir(os.path.join(patch_dir,"1")))
row = f"id,elevation,soc\n"
file.write(row)
with rasterio.open(dem, 'r') as dem_dataset:
    dem_data = dem_dataset.read(1)
    with rasterio.open(soc,'r') as soc_dataset:
        soc_data = soc_dataset.read(1)

        for patch in range(1, patches+1):
            x,y = patch_number_to_dims(patch)
            dem_window = dem_data[y:y+PATCH_HEIGHT, x:x+PATCH_WIDTH]
            soc_window = soc_data[y:y+PATCH_HEIGHT, x:x+PATCH_WIDTH]

            dem_avg = numpy.mean(dem_window)
            soc_avg = numpy.mean(soc_window)

            row = f"{patch},{dem_avg},{soc_avg}\n"
            file.write(row)
            print(f"Done patch {patch}")

print("Done all")
file.close()