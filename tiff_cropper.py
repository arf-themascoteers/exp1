from osgeo import gdal


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


def crop(file, outfile, left, up, right, bottom):
    ds = gdal.Open(file)
    xoff, xres, xsq, yoff, ysq, yres = ds.GetGeoTransform()
    xmax = xoff + (ds.RasterXSize * xres)
    ymax = yoff + (ds.RasterYSize * yres)

    print("xoff", xoff)
    print("yoff", yoff)

    print("target_left", left)
    print("target_right", right)
    print("target_up", up)
    print("target_bottom",bottom)

    print("xmax", xmax)
    print("ymax", ymax)

    if not within_box(xoff, yoff, xmax, ymax, left, up, right, bottom):
        raise Exception("Bounding box outside image")

    bbox = (xoff,yoff,xmax,ymax)
    bbox = (xoff,yoff,500,500)
    gdal.Translate(outfile, file, srcWin=bbox)


if __name__ == "__main__":
    infile = r'data/sample/tiff/1_Second_DEM.tif'
    outfile = r'data/sample/tiff/out.tif'
    crop(infile, outfile, 142.0, -36.4, 142.5, -36.7)
    print("Done")

    # left, up, right, bottom = 141.80513,  -36.29791, 142.70486, -36.901527
    # target_left, target_up, target_right, target_bottom = 142.0, -36.4, 142.5, -36.7
    #
    # result = check_box(left, up, right, bottom, target_left, target_up, target_right, target_bottom)
    # print(result)