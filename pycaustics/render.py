import array
from tqdm import tqdm
from core.camera import Camera
from core.ray import Ray
from core.vec3 import *
from shapes.sphere import *
from util.image import *

# Create camera
camera = Camera()

# Sphere object
sphere = Sphere(Point3(0,0,-1), 0.5)

# Dummy method for now
def pixel_color(r:Ray):
    if sphere.hit(r):
        return sphere.color()
    dir = normalize(r.direction)
    t = 0.5*(dir.y + 1.0)
    return (1.0-t)*Color(1.0,1.0,1.0) + t*Color(0.5,0.7,1.0)

# Binary black
image = array.array('B', [0,0,0] * camera.screen_width * camera.screen_height)

print("Render image...")

for j in tqdm (range(0,camera.screen_height), desc="Render..."):
    for i in range(0,camera.screen_width):
        index = j * 3 * camera.screen_width  + 3*i

        u = float(i) / (camera.screen_width-1.0)
        v = float(camera.screen_height - 1 - j) / (camera.screen_height-1.0)

        r = Ray(camera.origin, camera.lower_left_corner + camera.right*u + camera.up*v - camera.origin)
        pc = pixel_color(r)
        image[index] = int(255.999*pc[0])
        image[index+1] = int(255.999*pc[1])
        image[index+2] = int(255.999*pc[2])

create_image_ppm(image, camera.screen_width, camera.screen_height, "image.ppm")