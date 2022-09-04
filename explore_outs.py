import os
import rasterio as rio


def explore(file):
    print(file)
    with rio.open(file, 'r') as f:
        for x in range(1, f.count + 1):
            y = f.read(x)
            print(y.shape)
        print(f.count)
        print(f.bounds)


def explore_sat():
    for file in os.listdir(sat):
        path = os.path.join(sat, file)
        explore(path)


dem = r'data/out/dem/dem.tif'
soc = r'data/out/soc/000_005.tif'
sat = r'data/out/sat'

explore(dem)
explore(soc)


