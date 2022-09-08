import os
import rasterio
from PIL import Image
import shutil
import rasterio as rio
import numpy as np

src_dir = "data/EO1H0940852016239110K1_1T"
dest = "data/out/merged/hsi.tif"

ar = np.zeros((5071, 1431))
count_bands = len(os.listdir(src_dir))
i = 1
for file in os.listdir(src_dir):
    src = os.path.join(src_dir, file)
    with rio.open(src, 'r') as dataset:
        data = dataset.read(1)
        ar = ar + (data/count_bands)
    print(f"done {i}")
    i = i+1

ar = ar.astype(int)
file = os.listdir(src_dir)[0]
src = os.path.join(src_dir, file)
with rio.open(src, 'r') as dataset:
    profile = dataset.profile
    ar = ar.reshape(1, ar.shape[0], ar.shape[1])
    #profile = {"height":ar.shape[0], "width":ar.shape[1], "driver":"GTiff", "count" : 1, "dtype" : "int16"}
    with rasterio.open(dest, 'w', **profile) as dst:
        dst.write(ar)
print("done")