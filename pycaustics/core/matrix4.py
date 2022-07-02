import math
 
import core.vec3

class Vec4:
    def __init__(self, x = 0, y = 0, z = 0, w = 1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    def fromVec3(v):
        return Vec4(v.x,v.y,v.z,1.0)

class Matrix4:
    def __init__(self, content = [[1.0,0.0,0.0,0.0], [0.0,1.0,0.0,0.0], [0.0,0.0,1.0,0.0], [0.0,0.0,0.0,1.0]]):
        self.content = content

    @classmethod
    def identity():
        return Matrix4()

    def m(self, i,j):
        return self.content[i][j]

    def transpose(self):
        return Matrix4([[self.content[0][0], self.content[1][0], self.content[2][0], self.content[3][0]],
                        [self.content[0][1], self.content[1][1], self.content[2][1], self.content[3][1]],
                        [self.content[0][2], self.content[1][2], self.content[2][2], self.content[3][2]],
                        [self.content[0][3], self.content[1][3], self.content[2][3], self.content[3][3]]])

    def det(self):
        det00 = self.m(1,1)*self.m(2,2)*self.m(3,3) + self.m(1,2)*self.m(2,3)*self.m(3,1) + self.m(1,3)*self.m(2,1)*self.m(3,2)
        - self.m(1,3)*self.m(2,2)*self.m(3,1) - self.m(1,2)*self.m(2,1)*self.m(3,3) - self.m(1,1)*self.m(2,3)*self.m(3,2)

        det10 = self.m(0,1)*self.m(2,2)*self.m(3,3) + self.m(0,2)*self.m(2,3)*self.m(3,1) + self.m(0,3)*self.m(2,1)*self.m(3,2)
        - self.m(0,3)*self.m(2,2)*self.m(3,1) - self.m(0,2)*self.m(2,1)*self.m(3,3) - self.m(0,1)*self.m(2,3)*self.m(3,2)

        det20 = self.m(1,1)*self.m(1,2)*self.m(3,3) + self.m(1,2)*self.m(1,3)*self.m(3,1) + self.m(1,3)*self.m(1,1)*self.m(3,2)
        - self.m(1,3)*self.m(1,2)*self.m(3,1) - self.m(1,2)*self.m(1,1)*self.m(3,3) - self.m(1,1)*self.m(1,3)*self.m(3,2)

        det30 = self.m(1,1)*self.m(1,2)*self.m(2,3) + self.m(1,2)*self.m(1,3)*self.m(2,1) + self.m(1,3)*self.m(1,1)*self.m(2,2)
        - self.m(1,3)*self.m(1,2)*self.m(2,1) - self.m(1,2)*self.m(1,1)*self.m(2,3) - self.m(1,1)*self.m(1,3)*self.m(2,2)

        return self.m(0,0)*det00 - self.m(1,0)*det10 + self.m(2,0)*det20 + self.m(3,0)*det30

    def adjugate(self):
        pass
    #    A00 = self.m(1,1)*self.m(2,2)*self.m(3,3) + self.m(1,2)*self.m(2,3)*self.m(3,1) + self.m(1,3)*self.m(2,1)*self.m(3,2)
    #    - self.m(1,3)*self.m(2,2)*self.m(3,1) - self.m(1,2)*self.m(2,1)*self.m(3,3) - self.m(1,1)*self.m(2,3)*self.m(3,2)
