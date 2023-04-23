#cw 7-1

import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): 
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

    def __add__(self, other): 
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def __sub__(self, other): 
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def __mul__(self, other): 
        total = self.x * other.x + self.y * other.y + self.z * other.z
        return total

    def cross(self, other): 
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector

    def length(self): 
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return length

    def normalize(self): #still on floats, aka not ideal
        new_x = self.x / self.length()
        new_y = self.y / self.length()
        new_z = self.z / self.length()
        new_vector = Vector(new_x, new_y, new_z)
        return new_vector
    
    def __hash__(self):   
        return hash((self.x, self.y, self.z))   

def find_axis(v1, v2):
    '''returns unit vector v3 perp. to v1 and v2'''

    v = v1.cross(v2)
    if v1.is_zero() or v2.is_zero():
        raise ValueError('zero vector')
    elif v.is_zero():
        raise ValueError('vectors are parallel')
    v3 = v.normalize()
    return v3


#test1

v1 = Vector(1, -9, 87)
v2 = Vector(-1, 48, -2)
v3 = find_axis(v1, v2)

print('test 1')
assert v3.length() == 1
print(v3)

#test2 - parallel vectors

v4 = Vector(1, 1, 1)
v5 = Vector(-2, -2, -2)

print('test 2')
print(find_axis(v4, v5))

input("naciśnij klawisz: ")
#eof
