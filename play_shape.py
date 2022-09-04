import geopandas as gpd
#import gdal
import shapely
from osgeo import gdal

print(gdal)

gdf = gpd.read_file("D:/Dataset/DEM/1_Second_DEM_4305716/Ancillary/DEMS_TileIndex.shp")
print(gdf.head())