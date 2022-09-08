import os

import rasterio
from rasterio.enums import Resampling


def resize(src, dest):
    target_dim0 = 1654
    target_dim1 = 611
    with rasterio.open(src) as dataset:
        matrix = dataset.read(1)
        data = dataset.read(
            out_shape=(
                dataset.count,
                int(target_dim0),
                int(target_dim1)
            ),
            resampling=Resampling.bilinear
        )
        profile = dataset.profile
        profile.update(height=data.shape[1], width=data.shape[2], driver="GTiff")
        with rasterio.open(dest, 'w', **profile) as dst:
            dst.write(data)
    print(f"Done resize {src}")


def resize_dem():
    src = "data/out/dem/dem.tif"
    dest = "data/out/resized/dem/dem.tif"
    resize(src, dest)


def resize_soc():
    src = "data/out/soc/000_005.tif"
    dest = "data/out/resized/soc/000_005.tif"
    resize(src, dest)


def resize_sat():
    src_dir = "data/EO1H0940852016239110K1_1T"
    dest_dir = "data/out/resized/hsi"
    for file in os.listdir(src_dir):
        src = os.path.join(src_dir, file)
        tokens = file.split("_")
        a_token = tokens[1]
        band_file_name = str(int(a_token[1:]))
        dest = os.path.join(dest_dir, band_file_name+".tif")
        resize(src, dest)

# resize_dem()
# resize_soc()
resize_sat()