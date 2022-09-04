import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal

src = "data/out/soc/000_005.tif"

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
