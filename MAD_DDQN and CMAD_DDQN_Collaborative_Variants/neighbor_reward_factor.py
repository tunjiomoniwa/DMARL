import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance


def neighbor_reward_factor(xs, ys, zs, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    ##n1, n2, n3, n4, n5, n6, n7
    Ns1 = CalcDistance(xs, ys, zs, x1, y1, z1)
    Ns2 = CalcDistance(xs, ys, zs, x2, y2, z2)
    Ns3 = CalcDistance(xs, ys, zs, x3, y3, z3)
    Ns4 = CalcDistance(xs, ys, zs, x4, y4, z4)
     
        
    
    myList = [Ns1, Ns2, Ns3, Ns4]            
    
    ans = np.argsort(myList)
    ##array([0, 1, 2, 4, 3])
    return ans

def neighbor_val(xs, ys, zs, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    Ns1 = CalcDistance(xs, ys, zs, x1, y1, z1)
    Ns2 = CalcDistance(xs, ys, zs, x2, y2, z2)
    Ns3 = CalcDistance(xs, ys, zs, x3, y3, z3)
    Ns4 = CalcDistance(xs, ys, zs, x4, y4, z4)
     
       
    
    myList = [Ns1, Ns2, Ns3, Ns4]            
    
    val = np.sort(myList)
    return val

def neighbor_rew_fxn(x1, x2, x3, y1, y2, y3):
    if (x1+x2+x3)> (y1+y2+y3):
        mu = 1
    elif (x1+x2+x3)== (y1+y2+y3):
        mu = 0
    elif (x1+x2+x3)< (y1+y2+y3):   
        mu = -1    
    return mu

def agent_i_rew_fxn(m, cn, co, en, eo):
    if cn > co:
        r = m + 1 + (eo - en)/(eo + en)
    elif cn == co:
        r = m + (eo - en)/(eo + en)
    elif cn < co:
        r = m - 1 + (eo - en)/(eo + en)
    return r

def done_agent_i_rew(cc, Absorbing_state):
    if cc>=1:
        r = Absorbing_state
    return r
