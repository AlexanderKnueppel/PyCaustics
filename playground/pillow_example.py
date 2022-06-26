from PIL import Image

im = Image.open("image.ppm")
print(im.format, im.size, im.mode)

im.show()