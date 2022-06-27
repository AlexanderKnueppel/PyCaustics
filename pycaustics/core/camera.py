from core.vec3 import *

class Camera:
    def __init__(self, origin = Point3(), screen_width=600, screen_height=400):
        self.origin = origin
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.aspect_ratio = float(screen_width)/screen_height
        self.viewport_height = 2.0
        self.viewport_width = self.aspect_ratio*self.viewport_height
        self.focal_length = 1.0
        self.up = Vec3(0,self.viewport_height,0)
        self.right = Vec3(self.viewport_width,0,0)
        self.lower_left_corner = origin - (self.right*0.5) - (self.up*0.5)-Vec3(0,0,self.focal_length)