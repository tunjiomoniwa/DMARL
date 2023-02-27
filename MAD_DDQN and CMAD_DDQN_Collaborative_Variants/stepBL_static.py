import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def stepBL_static(action, x1, y1, z1, e1, dist1, Lo, Hi, zLim):

    mobilitystep = 20 
    matxMax = [950]
    matxMin = [50]
    matyMax = [950]
    matyMin = [50]
    zMax = 400
    zMin = 210

        ####
    Utip = 120 ##Tip speed of the rotor blade (m/s),
    A = 0.503   #rotor disc area from zeng
    rho = 1.225  #Air density in kg/m3
    s = 0.05  #Rotor solidity, defined as the ratio of the total blade area bcR to the disc area A
    c0 = 0.02
    ci = 0.03
    #%%%%%%%% Sppeed of drones
    #%     DJI Mavic Air – 42.5 mph
    #%     DJI Mavic Pro – 40 mph
    ##%     DJI Phantom 4 Pro – 45 mph
    V = 20  #%%%44.7387mph 
    Vh = 0  #%hovering velocity which is approx 0m/s
    Vlow = 10 
    v0 = 2 
    d0 = 0.6  #%Fuselage drag ratio, defined as d0
    d0n = 0.4
    b_factor =35
    energyfactorstatichover = b_factor*(c0*(1 + (3*Vh**2)/Utip**2) + ci*math.sqrt(math.sqrt(1 + (Vh**4)/(4*v0**4)) + (Vh**2)/(2*v0**2)) + (rho*d0*s* A*Vh**3)/2)
    
    energydrain = b_factor*(c0*(1 + (3*V**2)/Utip**2) + ci*math.sqrt(math.sqrt(1 + (V**4)/(4*v0**4)) + (V**2)/(2*v0**2)) + (rho*d0n*s* A*V**3)/2)
    ##%2.0; %10Joules to move unit step (to insert the model)
    ##%%powerdrain = c0*(1 + (3*V**2)/Utip**2) + ci*sqrt(sqrt(1 + (V**4)/(4*v0**4)) + (V**2)/(2*v0**2)) + (rho*d0*s* A*V**3)/2
    energydrainUp = b_factor*(c0*(1 + (3*V**2)/Utip**2) + ci*math.sqrt(math.sqrt(1 + (V**4)/(4*v0**4)) + (V**2)/(2*v0**2)) + (rho*d0*s* A*V**3)/2)
    ##%3.4;
    energydrainDown = b_factor*(c0*(1 + (3*Vlow**2)/Utip**2) + ci*math.sqrt(math.sqrt(1 + (Vlow**4)/(4*v0**4)) + (Vlow**2)/(2*v0**2)) + (rho*d0*s* A*Vlow**3)/2)
    ##%1.0;
    dt = 1 ## %timeslot of 1unit(secs) of time
    altitudestep = 15

    if (action == 1): #%means north
        x1 = x1
        z1 = z1
        y1 = y1 + mobilitystep
        e1 = e1 + energydrain
        dist1 = dist1  + mobilitystep 
    elif (action == 2): #%means south
        x1 = x1
        z1 = z1
        y1 = y1 - mobilitystep
        e1 = e1 + energydrain
        dist1 = dist1  + mobilitystep 
    elif (action == 3): #%means east
        y1 = y1
        z1 = z1
        x1 = x1 + mobilitystep
        e1 = e1 + energydrain
        dist1 = dist1  + mobilitystep 
    elif (action == 4): #%means west
        y1 = y1
        z1 = z1
        x1 = x1 - mobilitystep
        e1 = e1 + energydrain
        dist1 = dist1  + mobilitystep 
    elif (action == 5): #%means up
        y1 = y1
        x1 = x1
        z1 = z1 + altitudestep
        e1 = e1 + energydrainUp
        dist1 = dist1  + altitudestep 
    elif (action == 6): #%means down
        y1 = y1
        x1 = x1
        z1 = z1 - altitudestep
        e1 = e1 + energydrainDown
        dist1 = dist1  + altitudestep 
    else: ##%static
        y1 = y1
        x1 = x1
        z1 = z1 
        e1 = e1 + energyfactorstatichover
        dist1 = dist1
        
    [x1,y1,z1]
    energy1 = e1
    #%stepUAV1 = [[x1,y1,z1], energy1]
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ## to keep UAV within coverage region
    if (x1 > matxMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(x1 - matxMax[0])
        #% Walk in the x direction.
        x1 = matxMax[0] - distanceBeyond
    elif (x1 < matxMin[0]):
        #% It's past the left edge
        distanceBeyond = abs(matxMin[0] - x1)
        #% Walk in the x direction.
        x1 = matxMin[0] + distanceBeyond
    else:
        x1 = x1


    if (y1 > matyMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(y1 - matyMax[0])
        #% Walk in the x direction.
        y1 = matyMax[0] - distanceBeyond
    elif y1 < matyMin[0]:
        #% It's past the left edge
        distanceBeyond = abs(matyMin[0] - y1)
        #% Walk in the x direction.
        y1 = matyMin[0] + distanceBeyond
    else:
        y1 = y1


    ##%%%% check for z
    if (z1 > zMax):
         # % It's past the right edge
        distanceBeyond = abs(z1 - zMax)
        ##% Walk in the x direction.
        z1 = zMax - distanceBeyond
    elif z1 < zMin:
        #% It's past the left edge
        distanceBeyond = abs(zMin - z1)
        #% Walk in the x direction.
        z1 = zMin + distanceBeyond
    else:
        z1 = z1

    x1= abs(x1)
    y1 = abs(y1)
    z1 = abs(z1)

    done1= bool(energy1 <= 5000000 and z1>=zLim and x1>=Lo and x1<Hi and y1>=Lo and y1<Hi)
    

    obsUAVBL1 = [x1,y1,z1, energy1, done1, dist1]
    return obsUAVBL1
    #print(obsUAVBL1)
