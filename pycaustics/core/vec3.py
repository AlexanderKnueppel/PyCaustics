import math
from re import X

class Vec3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        """Addition v3 = v1+v2"""
        return Vec3(self.x+v.x, self.y+v.y, self.z+v.z)

    def __iadd__(self, v):
        """Inplace addition"""
        self.x+=v.x
        self.y+=v.y
        self.z+=v.z

    def __sub__(self, v):
        """Substraction v3 = v1-v2"""
        return Vec3(self.x-v.x, self.y-v.y, self.z-v.z)

    def __isub__(self, v):
        """Inplace substraction"""
        self.x-=v.x
        self.y-=v.y
        self.z-=v.z

    def __neg__(self):
        """Negation"""
        return Vec3(-self.x, -self.y, -self.z)

    def __eq__(self, v):
        """Equality (v2 == v1?)"""
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __mul__(self, s):
        """Scalar multiplication (v2 = v1 * s)"""
        return Vec3(self.x*s, self.y*s, self.z*s)

    def __imul__(self, s):
        """Inplace multiplication"""
        self.x+=s
        self.y+=s
        self.z+=s

    def __div__(self, s):
        """Scalar division (v2 = v1 / s)"""
        return Vec3(float(self.x)/s, float(self.y)/s, float(self.z)/s)

    def __idiv__(self, s):
        """Inplace division"""
        self.x/=s
        self.y/=s
        self.z/=s

    def __len__(self):
        """Returns the length of this vector"""
        return math.sqrt(self.lengthSq())

    def __str__(self):
        """Returns a comprehensible string"""
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def lengthSq(self):
        """Returns the squared length of this vector"""
        return self.x*self.x + self.y * self.y + self.z*self.z

    def __getitem__(self, index):
        """Accesses the elements with an index (0,1,2)"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise ValueError(f'{index} is not a valid index (only 0, 1, or 2 are allowed).')
