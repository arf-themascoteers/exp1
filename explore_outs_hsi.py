import rasterio as rio

sat_src = r"data/out/merged/hsi.tif"
dem_src = "data/out/dem/dem.tif"
soc_src = "data/out/soc/000_005.tif"

with rio.open(sat_src,'r') as dataset:
    data = dataset.read(1)
    print(data.shape)
#
# with rio.open(dem_src,'r') as dataset:
#     data = dataset.read(1)
#     print(data.shape)

with rio.open(soc_src,'r') as dataset:
    data = dataset.read(1)
    print(data.shape)

