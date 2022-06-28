from core.ray import Ray
from core.vec3 import *

class Sphere:
    def __init__(self, center, radius) -> None:
        self.center = center
        self.radius = radius

    def hit(self, ray:Ray) -> float:
        OC = ray.origin - self.center
        a = dot(ray.direction,ray.direction)
        b = 2.0*dot(ray.direction, OC)
        c = dot(OC,OC) - self.radius**2
        d = b*b - 4*a*c # based on PQ-Formula; has discremenant a real solution? 
        if d < 0: 
            return -1

        return (-b-math.sqrt(d)) / (2*a)

    def color(self) -> Color:
        return Color(1,0,0)
        




