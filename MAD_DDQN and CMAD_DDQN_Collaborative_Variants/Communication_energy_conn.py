import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance


def Communication_energy_conn(N12, N13, N14, N15, N23, N24, N25, N34, N35, N45, cov_obs[1], cov_obs[2], cov_obs[3], cov_obs[4],  ):
    ProximityThreshold = 500

    if N12<ProximityThreshold:
        cd12 = cov_obs[1]-old_cov2
        ed12 =  sprime2[3]/(sprime1[3]+sprime2[3])
    else:
        cd12 = 0
        ed12 = 0

    if N13<ProximityThreshold:
        cd13 = cov_obs[2]-old_cov3
        ed13 =  sprime3[3]/(sprime1[3]+sprime3[3])
    else:
        cd13 = 0
        ed13 = 0

    if N14<ProximityThreshold:
        cd14 = cov_obs[3]-old_cov4
        ed14 =  sprime4[3]/(sprime1[3]+sprime4[3])
    else:
        cd14 = 0
        ed14 = 0

    if N15<ProximityThreshold:
        cd15 = cov_obs[4]-old_cov5
        ed15 =  sprime5[3]/(sprime1[3]+sprime5[3])
    else:
        cd15 = 0
        ed15 = 0
    ######
    if N23<ProximityThreshold:
        cd23 = cov_obs[2]-old_cov3
        ed23 =  sprime3[3]/(sprime2[3]+sprime3[3])
    else:
        cd23 = 0
        ed23 = 0
    if N24<ProximityThreshold:
        cd24 = cov_obs[3]-old_cov4
        ed24 =  sprime4[3]/(sprime2[3]+sprime4[3])
    else:
        cd24 = 0
        ed24 = 0

    if N25<ProximityThreshold:
        cd25 = cov_obs[4]-old_cov5
        ed25 =  sprime5[3]/(sprime2[3]+sprime5[3])
    else:
        cd25 = 0
        ed25 = 0
    ##
    if N34<ProximityThreshold:
        cd34 = cov_obs[3]-old_cov4
        ed34 =  sprime4[3]/(sprime3[3]+sprime4[3])
    else:
        cd34 = 0
        ed34 = 0

    if N35<ProximityThreshold:
        cd35 = cov_obs[4]-old_cov5
        ed35 =  sprime5[3]/(sprime3[3]+sprime5[3])
    else:
        cd35 = 0
        ed35 = 0
        
    ####
    if N35<ProximityThreshold:
        cd45 = cov_obs[4]-old_cov5
        ed45 =  sprime5[3]/(sprime4[3]+sprime5[3])
    else:
        cd45 = 0
        ed45 = 0

    
    comm_obs = [cd12, cd13, cd14, cd15, cd23, cd24, cd25, cd34, cd35, cd45, ed12, ed13, ed14, ed15, ed23, ed24, ed25, ed34, ed35, ed45]
    return comm_obs
