import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def step_fairness(conn_dev_array):
    conn_dev_array = np.array(conn_dev_array, dtype=np.float64)
    N = len(conn_dev_array)
    len1 = np.array(range(0,len(conn_dev_array)))
    num = 0
    den = 0
    for i in len1:
        de_ = pow(conn_dev_array[i],2)
        den = np.add(den, de_)
        nu_ = conn_dev_array[i]
        num = np.add(num, nu_)

    fair = pow(num,2)/(N*den)
    return fair
