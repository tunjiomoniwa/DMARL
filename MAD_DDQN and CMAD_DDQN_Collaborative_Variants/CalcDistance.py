import math


# Function definition is here
def CalcDistance(xx1, yy1, zz1, xx2, yy2, zz2):
    dist = (xx2-xx1)**2+(yy2-yy1)**2+(zz2-zz1)**2
    euclideanDistance = math.sqrt(dist)#pow(dist, 0.5)
    return euclideanDistance;
