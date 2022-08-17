import rasterio as rio
import matplotlib.pyplot as plt
from osgeo import gdal


with rio.open(r'data/sample/tiff/out.tif','r') as f:
    for x in range(1, f.count+1):
        y = f.read(x)
        plt.imshow(y, cmap='pink')
        plt.show()
    # print("done")
    d = f.crs
    # print(d)
    print("f.bounds.left\t", f.bounds.left)
    print("f.bounds.right\t", f.bounds.right)
    print("f.bounds.up\t", f.bounds.top)
    print("f.bounds.down\t", f.bounds.bottom)
    # print(f.transform)


ds = gdal.Open(r'data/sample/tiff/out.tif')
band = ds.GetRasterBand(1)
im = band.ReadAsArray()
# plt.imshow(im)
# plt.show()
width = im.shape[0]
height = im.shape[1]

xoff, xres, xsq, yoff, ysq, yres = ds.GetGeoTransform()

right = xoff + (ds.RasterXSize * xres)
down = yoff + (ds.RasterYSize * yres)
print("Calculated Right", right)
print("Calculated Down", down)

print("ds.RasterXSize",ds.RasterXSize)
print("ds.RasterYSize",ds.RasterYSize)

print("xoff", xoff)
print("yoff", yoff)
print("xres", xres)
print("yres", yres)

geo_width = (right-xoff)
geo_height = (yoff-down)

val_pix_width = geo_width/xres
val_pix_height = geo_height/yres

print("geo_width", geo_width)
print("geo_height", geo_height)
print("im.shape", im.shape)
print("val_pix_width",val_pix_width)
print("val_pix_height",val_pix_height)

