from core.ray import Ray
from core.vec3 import *
from numpy import array

class Cuboid:
    """ Very unoptimized class for cuboids from the top of my head (will bre replaced) 
    
        For instance, I store all 8 points and compute heigth, width, length, and center
        each call...
    """
    def __init__(self, center = Point3(), width = 1, length = 1, height = 1) -> None:
        self.center = center
        self.ulf = center - width/2.0 + height/2.0 + length/2.0    # upper-left-front
        self.urf = center + width/2.0 + height/2.0 + length/2.0    # upper-right-front
        self.lrf = center + width/2.0 - height/2.0 + length/2.0    # lower-right-front
        self.llf = center - width/2.0 - height/2.0 + length/2.0    # lower-left-front
        self.ulb = center - width/2.0 + height/2.0 - length/2.0    # upper-left-back
        self.urb = center + width/2.0 + height/2.0 - length/2.0    # upper-right-back
        self.lrb = center + width/2.0 - height/2.0 - length/2.0    # lower-right-back
        self.llb = center - width/2.0 - height/2.0 - length/2.0    # lower-left-back

    def height(self):
        return (self.ulf-self.llf).length()

    def width(self):
        return (self.ulf-self.urf).length()

    def length(self):
        return (self.ulf-self.ulb).length()

    def center(self):
        dir = self.ulf-self.lrb;
        t = (dir).length()/2.0
        return self.lrb + t*normalize(dir) 


    def hit(self, ray:Ray) -> float:
        """ AABB test? """
        #ndir = normalize(ray.direction)
        #dirfrac = Vec3(1.0/ndir.x, 1.0/ndir.y, 1.0/ndir.z)
        #t1 = ()
        pass

    def color(self, hit_point) -> Color:
        N = normalize(hit_point - self.center)
        return 0.5*Color(N.x+1,N.y+1,N.z+1)