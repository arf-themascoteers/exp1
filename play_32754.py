import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal
import sat_utils

src = r"C:\Users\Administrator\Downloads\EO1H0940852016239110K1_1T\EO1H0940852016239110K1_B145_L1T.TIF"
dest = "data/work/tes3.tif"
#
# sat_utils.resize(src, dest)
# src = dest
# with rio.open(src,'r') as dataset:
#     left, bottom, right, top = sat_utils.to_wgs84(dataset)
#     print("left, bottom, right, top", left, bottom, right, top)
    # data = dataset.read(1)
    # print(data.shape)

with rio.open(src,'r') as dataset:
    data = dataset.read(1)
    print(data.shape)