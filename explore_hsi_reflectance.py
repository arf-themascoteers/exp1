import os
import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
from PIL import Image
import numpy

src_dir = f"data/out/hsi_patches"

def explore_sat():
    for patch in range(1200, 1400, 50):
        array = np.zeros(len(os.listdir(src_dir)))
        i = 0
        for file in os.listdir(src_dir):
            path = os.path.join(src_dir, file, f"{patch}.png")
            with rio.open(path, 'r') as dataset:
                y = dataset.read(1)
                array[i] = np.mean(y)
                i = i + 1

        plt.plot(array)
        plt.show()


explore_sat()
print("done")