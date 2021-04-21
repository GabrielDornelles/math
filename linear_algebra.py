import math
import numpy as np

class LinearAlgebraOperations:

    def dot_product(self,v1,v2):
        dp = 0
        if len(v1) != len(v2):
            print("Vectors size don't match")
            return
        for i in range(0,len(v1)):
            dp += v1[i]*v2[i]
        return dp

    def cross_product(self,v1,v2):
        cp,cp_x,cp_y,cp_z = [0,0,0,0]
        #truth is I dont know a smart way to do that, so I coded what I do to calculate by hand
        if len(v1) != len(v2):
            print("Vectors size don't match")
            return
        # 2d vectors:
        if len(v1)==2: return np.array([v1[0]*v2[1], v1[1]*v2[0]])
        # 3d vectors:
        cp_x = (v1[1]*v2[2]) - (v2[1]*v1[2])
        cp_y = (v1[2]*v2[0]) - (v2[2]*v1[0])
        cp_z = (v1[0]*v2[1]) - (v2[0]*v1[1])
        cp = np.array([cp_x,cp_y,cp_z])
        return cp

    def mixed_product(self,v1,v2,v3):
        return self.dot_product(v1,self.cross_product(v2,v3))

    def module_of_vector(self,v1,verbose=False):
        square_root_radicand = np.sum(([idx**2 for idx in v1]))
        if verbose : print(f"vector {v1} module as square root: √{square_root_radicand}")
        return math.sqrt(square_root_radicand)

    def angle_between_vectors(self,v1,v2):
        return math.acos((self.dot_product(v1,v2))/(self.module_of_vector(v1)*self.module_of_vector(v2)))*(180/math.pi)

    def contains_p_in_line(self,points: list = None, p : tuple=None) -> bool:
        """
        Pass a list *points* with two tuples containing your points to build a vector.
        Then pass a point *p* to check.
        """

        x = points[1][0] - points[0][0]
        y = points[1][1] - points[0][1]
        z = points[1][2] - points[0][2]
        v1 = np.array([x,y,z])

        return ((p[0]-points[0][0])/v1[0])==((p[1]-points[0][1])/v1[1])==((p[2] - points[0][2])/v1[2])

vector_1 = np.array([3,0,0])
vector_2 = np.array([0,2,0])
vector_3 = np.array([3,2,-4])
vectors = LinearAlgebraOperations()

mixed_product = vectors.mixed_product(vector_1,vector_2,vector_3)
print(f"mixed product between vectors {vector_1},{vector_2} and {vector_3}: {mixed_product}")

mod = vectors.module_of_vector(vector_3)
print(f"module of vector {vector_3}: {mod:.2f}")

v1 = np.array([-4,2,8])
v2 = np.array([2,-4,8])
abv = vectors.angle_between_vectors(v1,v2)
print(f"angle between vectors {v1} and {v2}: {abv:.2f}º")

contains = vectors.contains_p_in_line(points=[(1,0,1),(2,3,3)], p=(1,0,1))
print(contains)
