import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal
import os
import sat_utils

path = "D:/Dataset/DEM/1_Second_DEM_Smoothed_4306080/1_Second_DEM_Smoothed.tif"
outfile = r'data/out/dem/dem.tif'

sat_utils.crop_tiff(path, outfile, 142.6622699954712, -35.36579150024378,
                143.17160703041947, -36.743931294099966)
print("Done")

