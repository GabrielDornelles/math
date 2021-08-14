import math
# I did learn that a long time ago, implemented for fun and demonstrate python to a friend.
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))

def get_angles(a,b,c):
    try:
        a_angle = a**2 - (b**2 + c**2)
        a_angle = a_angle / (-2*b*c)
        a_angle = math.acos(a_angle)*(180/ math.pi)

        b_angle = b**2 - (a**2 + c**2)
        b_angle = b_angle / ((-2)*a*c)
        b_angle = math.acos(b_angle)*(180/math.pi)

        c_angle = c**2 - (a**2 + b**2)
        c_angle = c_angle / (-2*a*b)
        c_angle = math.acos(c_angle)*(180/math.pi)

        print(f"opposite angle of a: {a_angle}º")
        print(f"opposite angle of b: {b_angle}º")
        print(f"opposite angle of c: {c_angle}º")
        print(f"sum of angles: {a_angle + b_angle + c_angle}")
        return a_angle,b_angle, c_angle
    except Exception as ex:
        print(f"{ex}, invalid triangle")
        return 0,0,0
aa,bb,cc = get_angles(a,b,c)
