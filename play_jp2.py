import rasterio as rio
import matplotlib.pyplot as plt
import sat_utils

src = r'D:/Dataset/Sentinel/S2/T54HXE_20151228T001732_B02.jp2'

with rio.open(src) as f:
    for x in range(1, f.count+1):
        y = f.read(x)
        # plt.imshow(y, cmap='pink')
        # plt.show()
    bounds = sat_utils.to_wgs84(f)
    print(bounds)


