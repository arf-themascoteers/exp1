import os
import sat_utils

src = "D:/Dataset/SOC-CSIRO/000-005cm/SOC_000_005_EV_N_P_AU_NAT_C_20140801.tif"
out = r'data/out/soc/000_005.tif'

sat_utils.crop_tiff(src, out, 142.6622699954712, -35.36579150024378,
                143.17160703041947, -36.743931294099966)
print("Done")

