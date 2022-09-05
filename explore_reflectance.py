import os
import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
from PIL import Image
import numpy


def explore_sat():
    array = np.zeros((9,16))
    for band in range(1,10):
        src = f"C:/Users/Administrator/Desktop/exp1/data/out/patches/{band}/100.png"
        x = Image.open(src)
        ar = numpy.asarray(x)
        array[band-1,:] =  ar[0, :]
    plt.plot(array)
    plt.show()


explore_sat()
print("done")