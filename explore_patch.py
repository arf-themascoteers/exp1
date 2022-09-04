import os
import rasterio as rio
from PIL import Image
import numpy


def explore_sat(src):
    x = Image.open(src)
    ar = numpy.asarray(x)
    print(ar.shape)

src = "C:/Users/Administrator/Desktop/exp1/data/out/patches/10/200.png"
explore_sat(src)



