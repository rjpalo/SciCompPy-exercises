#cw 6-1

import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): # return string "Vector(x, y, z)"
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

    def is_zero(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return True
        else:
            return False
        
    def __eq__(self, other): # v == w
        return (self - other).is_zero()

    def __ne__(self, other): # v != w
        return not self == other

    def __add__(self, other): # v + w
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def __sub__(self, other): # v - w
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def __mul__(self, other): # return the dot product (number)
        total = self.x * other.x + self.y * other.y + self.z * other.z
        return total

    def cross(self, other): # return the cross product (Vector)
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def length(self): # the length of the vector
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return length

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended


#test1

v = Vector(1, 1, 1)
w = Vector(2, 2, 2)
assert v != w
assert repr(v) == "Vector(1, 1, 1)"
assert v + w == Vector(3, 3, 3) 
assert v - w == Vector(-1, -1, -1) 
assert v * w == 6 
assert v.cross(w) == Vector(0, 0, 0) 
assert v.length() == math.sqrt(3) 
S = set([v, v, w])
assert len(S) == 2 

print("Test 1 passed")

#test2

a = Vector(-1, 5, 0)
b = Vector(2, 3, -6)
assert a != b
assert repr(a) == "Vector(-1, 5, 0)"
assert a + b == Vector(1, 8, -6) 
assert a - b == Vector(-3, 2, 6) 
assert a * b == 13 
assert a.cross(b) == Vector(-30, -6, -13) 
assert a.length() == math.sqrt(26) 
S = set([a, a, b])
assert len(S) == 2 

print("Test 2 passed")

#test3

c = Vector(1, 0, 0)
d = Vector(0, 1, 0)
assert c != d
assert repr(d) == "Vector(0, 1, 0)"
assert c + d == Vector(1, 1, 0) 
assert c - d == Vector(1, -1, 0) 
assert c * d == 0
assert c.cross(d) == Vector(0, 0, 1) 
assert c.length() == math.sqrt(1) 
S = set([c, c, d, d])
assert len(S) == 2 

print("Test 3 passed")

input("naciśnij klawisz: ")
#eof
