from osgeo import gdal
import matplotlib.pyplot as plt
from rasterio.crs import CRS
from rasterio import warp
import rasterio


def within_box(left, up, right, bottom, target_left, target_up, target_right, target_bottom):
    x_diff = right - left
    y_diff = bottom - up
    if x_diff < 0:
        temp = left
        left = right
        right = temp
    if y_diff < 0:
        temp = up
        up = bottom
        bottom = temp

    if left > target_left or right < target_right or up > target_up or bottom < target_bottom:
        return False

    return True


def crop_tiff(file, outfile, left, up, right, bottom):
    xoff, xmax, yoff, ymax = get_bbox(file)
    if not within_box(xoff, yoff, xmax, ymax, left, up, right, bottom):
        raise Exception("Bounding box outside image")

    bbox = (left,up,right,bottom)
    gdal.Translate(outfile, file, projWin=bbox)


def crop_jp2(file, outfile, left, up, right, bottom):
    with rasterio.open(file) as dataset:
        xoff, ymax, xmax, yoff = to_wgs84(dataset)
        if not within_box(xoff, yoff, xmax, ymax, left, up, right, bottom):
            raise Exception("Bounding box outside image")
        left, bottom, right, up = to_32754(left, bottom, right, up)
        bbox = (left,up,right,bottom)
        gdal.Translate(outfile, file, projWin=bbox)


def get_bbox(file):
    ds = gdal.Open(file)
    xoff, xres, xsq, yoff, ysq, yres = ds.GetGeoTransform()
    xmax = xoff + (ds.RasterXSize * xres)
    ymax = yoff + (ds.RasterYSize * yres)
    return xoff, xmax, yoff, ymax


def print_bbox(file):
    xoff, xmax, yoff, ymax = get_bbox(file)
    print("xoff, xmax, yoff, ymax", xoff, xmax, yoff, ymax)


def plot_tiff(file, band=1):
    ds = gdal.Open(file)
    band1 = ds.GetRasterBand(band)
    b1 = band1.ReadAsArray()
    plt.imshow(b1)
    plt.show()
    print(f"Plot done. Height {b1.shape[0]}, Width {b1.shape[1]}")

def to_wgs84(dataset):
    crs_src = CRS.from_epsg(32754)
    crs_dest = CRS.from_epsg(4326)
    return warp.transform_bounds(crs_src, crs_dest, dataset.bounds.left,
                                   dataset.bounds.bottom, dataset.bounds.right, dataset.bounds.top)


def to_32754(left, bottom, right, top):
    crs_src = CRS.from_epsg(4326)
    crs_dest = CRS.from_epsg(32754)
    return warp.transform_bounds(crs_src, crs_dest, left, bottom, right, top)

if __name__ == "__main__":
    infile = r'data/sample/tiff/1_Second_DEM.tif'
    outfile = r'data/sample/tiff/out.tif'
    crop_tiff(infile, outfile, 141.80513888934237, -36.297916666898224, 142.704861111556, -36.901527778034456)
    print("Done")
