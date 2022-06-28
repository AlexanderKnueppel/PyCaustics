from core.ray import Ray
from core.vec3 import *

class Sphere:
    def __init__(self, center, radius) -> None:
        self.center = center
        self.radius = radius

    def hit(self, ray:Ray) -> bool:
        OC = ray.origin - self.center
        a = dot(ray.direction,ray.direction)
        b = 2.0*dot(ray.direction, OC)
        c = dot(OC,OC) - self.radius**2
        d = b*b - 4*a*c # based on PQ-Formula; has discremenant a real solution? 
        return d>=0

    def color(self) -> Color:
        return Color(1,0,0)
        




