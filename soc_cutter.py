import os
import sat_utils

src = "D:/Dataset/SOC-CSIRO/000-005cm/SOC_000_005_EV_N_P_AU_NAT_C_20140801.tif"
out = r'data/out/soc/000_005.tif'

sat_utils.crop_tiff(src, out, 142.15147294609447, -36.158194444674116,
                143.21430555608072, -36.92885610612682)
print("Done")

