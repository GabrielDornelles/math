import math
import numpy as np

class LinearAlgebraOperations:

    def __init__(self):
        self.dp = 0
        self.cp = 0
        self.module = 0

    def dot_product(self,v1,v2):
        if len(v1) != len(v2):
            print("Vectors size don't match")
            return
        for i in range(0,len(v1)):
            self.dp += v1[i]*v2[i]
        return self.dp

    def cross_product(self,v1,v2):
        #truth is I dont know a smart way to do that, so I coded what I do to calculate by hand
        if len(v1) != len(v2):
            print("Vectors size don't match")
            return
        # 2d vectors:
        if len(v1)==2: return np.array([v1[0]*v2[1], v1[1]*v2[0]])
        # 3d vectors:
        self.cp_x = (v1[1]*v2[2]) - (v2[1]*v1[2])
        self.cp_y = (v1[2]*v2[0]) - (v2[2]*v1[0])
        self.cp_z = (v1[0]*v2[1]) - (v2[0]*v1[1])
        self.cp = np.array([self.cp_x,self.cp_y,self.cp_z])
        return self.cp

    def mixed_product(self,v1,v2,v3):
        return self.dot_product(v1,self.cross_product(v2,v3))

    def module_of_vector(self,v1):
        square_root_radicand = np.sum(([idx**2 for idx in v1]))
        print(f"vector {v1} module as square root: √{square_root_radicand}")
        return math.sqrt(square_root_radicand)

vector_1 = np.array([3,0,0])
vector_2 = np.array([0,2,0])
vector_3 = np.array([3,2,-4])
print(vector_1)
print(vector_2)
vectors = LinearAlgebraOperations()

#dot_product = vectors.dot_product(vector_1,vector_2)
#print(dot_product)

#cross_product = vectors.cross_product(vector_1, vector_2)
#print(cross_product)
mixed_product = vectors.mixed_product(vector_1,vector_2,vector_3)
print(mixed_product)
mod = vectors.module_of_vector(vector_3)
print(mod)
