import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def goal_target(x, y, z, x_new, y_new, z_new, c, c_new):
    if (x1+x2+x3+x4+x5+x6)> (y1+y2+y3+y4+y5+y6):
        mu = 1
    elif (x1+x2+x3+x4+x5+x6)== (y1+y2+y3+y4+y5+y6):
        mu = 0
    elif (x1+x2+x3+x4+x5+x6)< (y1+y2+y3+y4+y5+y6):   
        mu = -1    
    return mu
