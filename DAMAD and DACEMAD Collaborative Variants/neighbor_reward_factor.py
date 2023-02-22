import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance


def neighbor_reward_factor(xs, ys, zs, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, x9, y9, z9, x10, y10, z10):
    ##n1, n2, n3, n4, n5, n6, n7
    Ns1 = CalcDistance(xs, ys, zs, x1, y1, z1)
    Ns2 = CalcDistance(xs, ys, zs, x2, y2, z2)
    Ns3 = CalcDistance(xs, ys, zs, x3, y3, z3)
    Ns4 = CalcDistance(xs, ys, zs, x4, y4, z4)
    Ns5 = CalcDistance(xs, ys, zs, x5, y5, z5)
    Ns6 = CalcDistance(xs, ys, zs, x6, y6, z6)
    Ns7 = CalcDistance(xs, ys, zs, x7, y7, z7)
    Ns8 = CalcDistance(xs, ys, zs, x8, y8, z8)
    Ns9 = CalcDistance(xs, ys, zs, x9, y9, z9)
    Ns10 = CalcDistance(xs, ys, zs, x10, y10, z10)
    
    
    myList = [Ns1, Ns2, Ns3, Ns4, Ns5, Ns6, Ns7, Ns8, Ns9, Ns10]            
    
    ans = np.argsort(myList)
    ##array([0, 1, 2, 4, 3])
    return ans

def neighbor_val(xs, ys, zs, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, x9, y9, z9, x10, y10, z10):
    Ns1 = CalcDistance(xs, ys, zs, x1, y1, z1)
    Ns2 = CalcDistance(xs, ys, zs, x2, y2, z2)
    Ns3 = CalcDistance(xs, ys, zs, x3, y3, z3)
    Ns4 = CalcDistance(xs, ys, zs, x4, y4, z4)
    Ns5 = CalcDistance(xs, ys, zs, x5, y5, z5)
    Ns6 = CalcDistance(xs, ys, zs, x6, y6, z6)
    Ns7 = CalcDistance(xs, ys, zs, x7, y7, z7)
    Ns8 = CalcDistance(xs, ys, zs, x8, y8, z8)
    Ns9 = CalcDistance(xs, ys, zs, x9, y9, z9)
    Ns10 = CalcDistance(xs, ys, zs, x10, y10, z10)
    
    
    myList = [Ns1, Ns2, Ns3, Ns4, Ns5, Ns6, Ns7, Ns8, Ns9, Ns10]            
    
    val = np.sort(myList)
    return val

#six closest neighbours
def neighbor_rew_fxn(x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6, present_cov, past_cov):
    if (x1+x2+x3+x4+x5+x6)> (y1+y2+y3+y4+y5+y6):
        mu = (present_cov+1)/(past_cov+1)
    elif (x1+x2+x3+x4+x5+x6)== (y1+y2+y3+y4+y5+y6):
        mu = 0
    elif (x1+x2+x3+x4+x5+x6)< (y1+y2+y3+y4+y5+y6):   
        mu = -1*(present_cov+1)/(past_cov+1)    
    return mu

def agent_i_rew_fxn(m, cn, co, en, eo):
    if cn > co:
        r = m + 1 + (eo - en)/(eo + en)
    elif cn == co:
        r = m + (eo - en)/(eo + en)
    elif cn < co:
        r = m - 1 + (eo - en)/(eo + en)
    return r

def done_agent_i_rew(cc, Absorb_state):
    if cc>=1:
        r = Absorb_state
    return r
