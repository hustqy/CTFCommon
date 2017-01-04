import  math
# import numpy
# import array
from numpy import *
from PIL import Image

with open("F:\CTF\\1120\qr.data",'rb') as f:
    data = f.read()
    arr = "".join(["{:08b}".format(ord(x) ) for x in data])
    arr = [[int(i) for i in arr]]

    arr = array(arr)
    # arr = array.array.fromlist(arr)

    a = math.sqrt(len(arr))
    # print  a

    arr.reshape((300,300)).astype('uint8')*255
    im = Image.fromarray(arr)
    im.save("out.png")
    im.show()