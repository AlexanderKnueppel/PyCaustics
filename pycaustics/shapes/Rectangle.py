from core.ray import Ray
from core.vec3 import *
from numpy import array

class RectangleAA:
    """ Start with Axis-Aligned Rectangle (prob. super-slow) """
    def __init__(self, lowerleft = Point3(-0.5,-0.5,-1), upperright = Point3(0.5,0.5,-1)) -> None:
        self.lowerleft = lowerleft
        self.upperright = upperright
        self.normal = Vec3(0,0,1)
        self.scale = Vec3(1.0,1.0,1.0)
        self.translate = Vec3(0.0,0.0,0.0)
        self.rotate = Vec3(0.0,0.0,0.0)

    def hit(self, ray:Ray) -> float:
        # test1 = dot(normalize(ray.direction), self.normal)
        # test2 = dot((self.p1-ray.origin), self.normal)
        
        # if test1 == 0:
        #     return -1

        # t =  test2 / test1
        # hit_point = ray.origin + normalize(ray.direction)*t

        # P1P2 = self.p2-self.p1
        # P2P3 = self.p3-self.p2

        # if dot(P1P2, self.p1-hit_point) >= 0 and dot(P1P2, self.p1-hit_point) <= dot(P1P2, P1P2):
        #     if dot(P2P3, self.p2-hit_point) >= 0 and dot(P2P3, self.p2-hit_point) <= dot(P2P3, P2P3):
        #         print(f"{hit_point}")
        #         return t

        #apply scale/translate
        minPoint = Vec3(self.scale.x*self.lowerleft + self.translate.x, 
                        self.scale.y*self.lowerleft + self.translate.y, 
                        self.scale.y*self.lowerleft + self.translate.y)

        maxPoint = Vec3(self.scale.x*self.upperright + self.translate.x, 
                        self.scale.y*self.upperright + self.translate.y, 
                        self.scale.y*self.upperright + self.translate.y)

        rectZ = minPoint.z
        rayDir = normalize(ray.direction)
        rayOrigin = ray.origin
        
        # Apply rotation

        t = (rectZ - ray.origin.z) / dir.z
        hit_point = ray.origin + t*dir

        hit = hit_point.x <= maxPoint.x and hit_point.x >= minPoint.x and hit_point.y <= maxPoint.y and hit_point.y >= minPoint.y

        if hit:
            return t
        else:
            return -1

    def scale(self, x = 1.0, y = 1.0, z = 1.0):
        self.scale = Vec3(x,y,z)

    def translate(self, x = 0.0, y = 0.0, z = 0.0):
        self.translate = Vec3(x,y,z)

    def rotate(self, x = 0.0, y = 0.0, z = 0.0):
        self.rotate = Vec3(x,y,z)


    def color(self, hit_point) -> Color:
        N = normalize(hit_point - self.lowerleft)
        return 0.5*Color(N.x+1,N.y+1,N.z+1)