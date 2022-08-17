import rasterio as rio
import matplotlib.pyplot as plt

with rio.open(r'data/sample/tiff/1_Second_DEM.tif','r') as f:
    for x in range(1, f.count+1):
        y = f.read(x)
        plt.imshow(y, cmap='pink')
        plt.show()
    print("done")
    d = f.crs
    print(d)
