import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal
import os
import sat_utils

path = "D:/Dataset/DEM/1_Second_DEM_Smoothed_4306080/1_Second_DEM_Smoothed.tif"
outfile = r'data/out/dem/dem.tif'

sat_utils.crop_tiff(path, outfile, 142.11147294609447, -36.158194444674116,
                    143.21430555608072, -37.12885610612682)
print("Done")

