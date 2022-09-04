import os
import sat_utils
import rasterio as rio

src = "D:/Dataset/Sentinel/S2A_MSIL1C_20151228T001732_N0201_R116_T54HXE_20151228T002528/S2A_MSIL1C_20151228T001732_N0201_R116_T54HXE_20151228T002528.SAFE/GRANULE/L1C_T54HXE_A002687_20151228T002528/IMG_DATA"
out = r'data/out/sat'

for file in os.listdir(src):
    path = os.path.join(src, file)
    dest = os.path.join(out, file)
    sat_utils.crop_jp2(path, dest, 142.11147294609447, -36.158194444674116,
                143.21430555608072, -37.12885610612682)
    print(f"Done {file}")
print("Done")

