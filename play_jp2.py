import rasterio as rio
import matplotlib.pyplot as plt
import sat_utils
import numpy

src1 = r'D:/Dataset/Sentinel/S2/T54HXE_20151022T002722_B09.jp2'
src2 = r'D:/Dataset/Sentinel/S2/T54HXE_20151022T002722_B10.jp2'
src3 = r'D:/Dataset/Sentinel/S2/T54HXE_20151022T002722_B11.jp2'

print(src1)
with rio.open(src1) as f:
    y = f.read(1)
    print(y[100:105,100:105])

# print(src2)
# with rio.open(src2) as f:
#     y = f.read(1)
#     print(y[100:105,100:105])

print(src3)
with rio.open(src3) as f:
    y = f.read(1)
    print(y[100:105,100:105])


