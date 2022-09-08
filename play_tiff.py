import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal

src = r"C:\Users\Administrator\Downloads\EO1H0940852016239110K1_1T\EO1H0940852016239110K1_B001_L1T.TIF"

with rio.open(src,'r') as f:
    for x in range(1, f.count+1):
        y = f.read(x)
        # plt.imshow(y, cmap='pink')
        # plt.show()
    # print("done")
    d = f.crs
    print(f.count)
    print(d)
    print("f.bounds.left/t", f.bounds.left)
    print("f.bounds.right/t", f.bounds.right)
    print("f.bounds.up/t", f.bounds.top)
    print("f.bounds.down/t", f.bounds.bottom)
    # print(f.transform)
