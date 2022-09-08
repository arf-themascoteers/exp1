import os
import rasterio as rio
from PIL import Image
import numpy

src_dir = "data/out/hsi_patches"

def count_avg_value(dir):
    total = len(os.listdir(dir))
    avg_value = 0
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        x = Image.open(path)
        ar = numpy.asarray(x)
        cells = ar.shape[0] * ar.shape[1]
        count = ar.sum()/total
        avg_value = avg_value + count

    return avg_value


for file in os.listdir(src_dir):
    path = os.path.join(src_dir, file)
    print(file, count_avg_value(path))
    print("Done all")



