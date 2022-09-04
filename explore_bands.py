from PIL import Image
import numpy

src1 = r'data/out/patches/8/1.png'
src2 = r'data/out/patches/9/1.png'
src3 = r'data/out/patches/10/1.png'
src4 = r'data/out/patches/11/1.png'
src5 = r'data/out/patches/12/1.png'

def explore(src):
    print(src)
    x = Image.open(src)
    ar = numpy.asarray(x)
    ar = ar[0:5,0:5]
    print(ar)

explore(src1)
explore(src2)
explore(src3)
explore(src4)
explore(src5)
