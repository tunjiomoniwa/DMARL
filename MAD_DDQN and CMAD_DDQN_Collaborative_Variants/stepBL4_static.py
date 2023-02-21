import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def stepBL4_static(action, x4, y4, z4, e4, dist4):

    mobilitystep = 20 
    matxMax = [900]
    matxMin = [600]
    matyMax = [900]
    matyMin = [600]
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
        x4 = x4
        z4 = z4
        y4 = y4 + mobilitystep
        e4 = e4 + energydrain
        dist4 = dist4  + mobilitystep 
    elif (action == 2): #%means south
        x4 = x4
        z4 = z4
        y4 = y4 - mobilitystep
        e4 = e4 + energydrain
        dist4 = dist4  + mobilitystep 
    elif (action == 3): #%means east
        y4 = y4
        z4 = z4
        x4 = x4 + mobilitystep
        e4 = e4 + energydrain
        dist4 = dist4  + mobilitystep 
    elif (action == 4): #%means west
        y4 = y4
        z4 = z4
        x4 = x4 - mobilitystep
        e4 = e4 + energydrain
        dist4 = dist4  + mobilitystep 
    elif (action == 5): #%means up
        y4 = y4
        x4 = x4
        z4 = z4 + altitudestep
        e4 = e4 + energydrainUp
        dist4 = dist4  + altitudestep 
    elif (action == 6): #%means down
        y4 = y4
        x4 = x4
        z4 = z4 - altitudestep
        e4 = e4 + energydrainDown
        dist4 = dist4  + altitudestep 
    else: ##%static
        y4 = y4
        x4 = x4
        z4 = z4 
        e4 = e4 + energyfactorstatichover
        dist4 = dist4

    energy4 = e4
    [x4,y4,z4]
    #%stepUAV1 = [[x4,y4,z4], energy4]
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ## to keep UAV within coverage region
    if (x4 > matxMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(x4 - matxMax[0])
        #% Walk in the x direction.
        x4 = matxMax[0] - distanceBeyond
    elif (x4 < matxMin[0]):
        #% It's past the left edge
        distanceBeyond = abs(matxMin[0] - x4)
        #% Walk in the x direction.
        x4 = matxMin[0] + distanceBeyond
    else:
        x4 = x4


    if (y4 > matyMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(y4 - matyMax[0])
        #% Walk in the x direction.
        y4 = matyMax[0] - distanceBeyond
    elif y4 < matyMin[0]:
        #% It's past the left edge
        distanceBeyond = abs(matyMin[0] - y4)
        #% Walk in the x direction.
        y4 = matyMin[0] + distanceBeyond
    else:
        y4 = y4


    ##%%%% check for z
    if (z4 > zMax):
         # % It's past the right edge
        distanceBeyond = abs(z4 - zMax)
        ##% Walk in the x direction.
        z4 = zMax - distanceBeyond
    elif z4 < zMin:
        #% It's past the left edge
        distanceBeyond = abs(zMin - z4)
        #% Walk in the x direction.
        z4 = zMin + distanceBeyond
    else:
        z4 = z4

    x4= abs(x4)
    y4 = abs(y4)
    z4 = abs(z4)
    
    ##done4 =  bool(energy4 <= 5000000 and z4>=390 and x4>=700 and x4<800 and y4>=700 and y4<800)
    done4 =  bool(energy4 <= 5000000 and z4>=390 and x4>=700 and x4<=800 and y4>=700 and y4<=800)
    

    obsUAVBL4 = [x4,y4,z4, energy4, done4, dist4]
    return obsUAVBL4
    #print(obsUAVBL4)
