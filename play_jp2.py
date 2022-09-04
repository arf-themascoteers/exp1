import rasterio as rio
import matplotlib.pyplot as plt
import sat_utils

src = r'D:/Dataset/Sentinel/S2A_MSIL1C_20151228T001732_N0201_R116_T54HXE_20151228T002528/S2A_MSIL1C_20151228T001732_N0201_R116_T54HXE_20151228T002528.SAFE/GRANULE/L1C_T54HXE_A002687_20151228T002528/IMG_DATA/T54HXE_20151228T001732_B01.jp2'

with rio.open(src) as f:
    for x in range(1, f.count+1):
        y = f.read(x)
        # plt.imshow(y, cmap='pink')
        # plt.show()
    bounds = sat_utils.to_wgs84(f)
    print(bounds)


