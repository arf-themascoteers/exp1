import os
import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
from PIL import Image
import numpy

src_dir = f"data/out/hsi_patches"
bands = list(range(77,79))
def explore_sat():
    for patch in range(20, 21, 1):
        array = np.zeros(len(bands))
        i = 0
        for band in bands:
            path = os.path.join(src_dir, str(band), f"{patch}.png")
            with rio.open(path, 'r') as dataset:
                y = dataset.read(1)
                array[i] = np.mean(y)
                i = i + 1

        plt.plot(array)
        plt.show()


explore_sat()
print("done")