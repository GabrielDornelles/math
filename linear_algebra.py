import math
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm


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
        Pass a vector *v1*, or a list *points* with two tuples containing your points to build a vector.
        Then pass a point *p* to check.
        """

        x = points[1][0] - points[0][0]
        y = points[1][1] - points[0][1]
        z = points[1][2] - points[0][2]
        v1 = np.array([x,y,z])

        return ((p[0]-points[0][0])/v1[0])==((p[1]-points[0][1])/v1[1])==((p[2] - points[0][2])/v1[2])

    def plot_3_vectors(self,v1,v2,v3):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        O = np.array([0,0,0])
        ax.quiver(O,O,O,v1,v2,v3)
        ax.set_xlim([-10,10])
        ax.set_ylim([-10,10])
        ax.set_zlim([-10,10])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.show()

    def plan_equation(self, points:list,vp:tuple=None):
        """
        Plan equation is defined by: ax+by+cz+d=0
        input: list of tuples with the given points in 3d space
        """
        A = points[0]
        B = points[1]
        C = points[2]
        #create the plan
        AB= np.subtract(B,A)
        AC= np.subtract(C,A)
        normal_vector = self.cross_product(AB,AC)
        D = -(normal_vector[0]*A[0]+ normal_vector[1]*A[1]+ normal_vector[2]*A[2])
        print(D)
        print(normal_vector)
        if vp is not None:
            x,y,z=vp
            contains = (normal_vector[0]*x)+(normal_vector[1]*y)+(normal_vector[2]*z)+D==0
            answer = "is" if contains else "is not"
            print(f"the point {vp} {answer} contained by the plan")
        auto_size = max(abs(normal_vector[0]),abs(normal_vector[1]),abs(normal_vector[2]))
        x = np.linspace(-auto_size,auto_size,10)
        y = np.linspace(-auto_size,auto_size,10)
        X,Y = np.meshgrid(x,y)
        a,b,c,d = normal_vector[0],normal_vector[1],normal_vector[2],D
        Z = (d - a*X - b*Y) / c
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X, Y, Z,color="black")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        O = np.array([0,0,0])
        ax1 = fig.gca(projection="3d")
        ax1.quiver(O,O,O,normal_vector[0],normal_vector[1],normal_vector[2],color="red")
        plt.title("plan and normal vector")
        plt.show()

vectors = LinearAlgebraOperations()
vectors.plan_equation(points=[(2,0,1),(3,2,3),(0,4,4)])
#vectors.plan_equation(points=[(20,12,8),(20,6,10),(0,12,8)])
vector_1 = np.array([3,0,0])
vector_2 = np.array([0,2,0])
vector_3 = np.array([3,2,-4])


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


### plotting to see if it works
#vectors.plot_3_vectors(vector_1,vector_2,vectors.cross_product(vector_1,vector_2))

