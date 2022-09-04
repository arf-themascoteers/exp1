import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal
import os
import sat_utils

dir = r'data/out/soc'

for path in os.listdir(dir):
    file = os.path.join(dir, path)
    sat_processor.print_bbox(file)
    sat_processor.plot_tiff(file)
    print("Done",file)

