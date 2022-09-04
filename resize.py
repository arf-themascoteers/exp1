import os

import rasterio
from rasterio.enums import Resampling


def resize(src, dest):
    target_dim0 = 1165
    target_dim1 = 1323
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
    src_dir = "data/out/sat"
    dest_dir = "data/out/resized/sat"
    for file in os.listdir(src_dir):
        src = os.path.join(src_dir, file)
        dest = os.path.join(dest_dir, file)
        resize(src, dest)

resize_sat()