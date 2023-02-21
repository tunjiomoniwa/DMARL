import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def stepBL2_static(action, x2, y2, z2, e2, dist2):

    mobilitystep = 20 
    matxMax = [900]
    matxMin = [600]
    matyMax = [400]
    matyMin = [100]
    zMax = 400
    zMin = 210

    #print(matxMax[1])

    #matxmeMax = [450, 1000]
    #matxmeMin = [50, 500]
    #matymeMax = [450, 1000]
    #matymeMin = [50, 500]

    ##%%% Clustering (kmeans unsupervised learning)
    ##%     clusters = 1;
    ##%     Xclus = [xse; yse]';
    ##%     [idx,C] = kmeans(Xclus,clusters); %inbuilt ML toolbox fxn


    ##Xcent = [200, 250, 300; 500, 250, 300; 800, 250, 300]

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
    ##%0.2; # energy to hover
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
        x2 = x2
        z2 = z2
        y2 = y2 + mobilitystep
        e2 = e2 + energydrain
        dist2 = dist2  + mobilitystep 
    elif (action == 2): #%means south
        x2 = x2
        z2 = z2
        y2 = y2 - mobilitystep
        e2 = e2 + energydrain
        dist2 = dist2  + mobilitystep 
    elif (action == 3): #%means east
        y2 = y2
        z2 = z2
        x2 = x2 + mobilitystep
        e2 = e2 + energydrain
        dist2 = dist2  + mobilitystep 
    elif (action == 4): #%means west
        y2 = y2
        z2 = z2
        x2 = x2 - mobilitystep
        e2 = e2 + energydrain
        dist2 = dist2  + mobilitystep 
    elif (action == 5): #%means up
        y2 = y2
        x2 = x2
        z2 = z2 + altitudestep
        e2 = e2 + energydrainUp
        dist2 = dist2  + altitudestep 
    elif (action == 6): #%means down
        y2 = y2
        x2 = x2
        z2 = z2 - altitudestep
        e2 = e2 + energydrainDown
        dist2 = dist2  + altitudestep
    else: ##%static
        y2 = y2
        x2 = x2
        z2 = z2 
        e2 = e2 + energyfactorstatichover
        dist2 = dist2

    energy2 = e2
    [x2,y2,z2]
    #%stepUAV1 = [[x2,y2,z2], energy2]
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ## to keep UAV within coverage region
    if (x2 > matxMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(x2 - matxMax[0])
        #% Walk in the x direction.
        x2 = matxMax[0] - distanceBeyond
    elif (x2 < matxMin[0]):
        #% It's past the left edge
        distanceBeyond = abs(matxMin[0] - x2)
        #% Walk in the x direction.
        x2 = matxMin[0] + distanceBeyond
    else:
        x2 = x2


    if (y2 > matyMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(y2 - matyMax[0])
        #% Walk in the x direction.
        y2 = matyMax[0] - distanceBeyond
    elif y2 < matyMin[0]:
        #% It's past the left edge
        distanceBeyond = abs(matyMin[0] - y2)
        #% Walk in the x direction.
        y2 = matyMin[0] + distanceBeyond
    else:
        y2 = y2


    ##%%%% check for z
    if (z2 > zMax):
         # % It's past the right edge
        distanceBeyond = abs(z2 - zMax)
        ##% Walk in the x direction.
        z2 = zMax - distanceBeyond
    elif z2 < zMin:
        #% It's past the left edge
        distanceBeyond = abs(zMin - z2)
        #% Walk in the x direction.
        z2 = zMin + distanceBeyond
    else:
        z2 = z2

    x2= abs(x2)
    y2 = abs(y2)
    z2 = abs(z2)

    #done2= bool(energy2 <= 5000000 and z2>=390 and x2>=700 and x2<800 and y2>=200 and y2<300)
    done2= bool(energy2 <= 5000000 and z2>=390 and x2>=700 and x2<850 and y2>=200 and y2<=300)

    

    obsUAVBL2 = [x2,y2,z2, energy2, done2, dist2]
    return obsUAVBL2
    #print(obsUAVBL2)
