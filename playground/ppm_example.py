# This is the ppm-example from "Raytracing in one weekend"

import array

width = 256;
height = 256;

header = "P6 {} {} 255\n".format(width, height);

# Binary black
image = array.array('B', [0,0,0] * width * height)

for j in range(0,height):
    for i in range(0,width):
        index = j * 3 * width  + 3*i
        r = float(i) / (width-1)
        g = float(height-1-j) / (height-1)
        b = 0.25
        image[index] = int(255.999*r)
        image[index+1] = int(255.999*g)
        image[index+2] = int(255.999*b)

with open('image.ppm', 'wb') as f:
    f.write(bytearray(header, 'ascii'))
    image.tofile(f)
