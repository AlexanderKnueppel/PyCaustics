from vec3 import *

class Ray:
    def __init__(self, origin = Point3(), direction = Vec3()):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + t*self.direction
