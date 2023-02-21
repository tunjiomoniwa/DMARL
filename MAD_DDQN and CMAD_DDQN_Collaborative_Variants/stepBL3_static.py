import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def stepBL3_static(action, x3, y3, z3, e3, dist3):

    mobilitystep = 20 
    matxMax = [400]
    matxMin = [100]
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
        x3 = x3
        z3 = z3
        y3 = y3 + mobilitystep
        e3 = e3 + energydrain
        dist3 = dist3  + mobilitystep 
    elif (action == 2): #%means south
        x3 = x3
        z3 = z3
        y3 = y3 - mobilitystep
        e3 = e3 + energydrain
        dist3 = dist3  + mobilitystep
    elif (action == 3): #%means east
        y3 = y3
        z3 = z3
        x3 = x3 + mobilitystep
        e3 = e3 + energydrain
        dist3 = dist3  + mobilitystep
    elif (action == 4): #%means west
        y3 = y3
        z3 = z3
        x3 = x3 - mobilitystep
        e3 = e3 + energydrain
        dist3 = dist3  + mobilitystep
    elif (action == 5): #%means up
        y3 = y3
        x3 = x3
        z3 = z3 + altitudestep
        e3 = e3 + energydrainUp
        dist3 = dist3  + altitudestep
    elif (action == 6): #%means down
        y3 = y3
        x3 = x3
        z3 = z3 - altitudestep
        e3 = e3 + energydrainDown
        dist3 = dist3  + altitudestep
    else: ##%static
        y3 = y3
        x3 = x3
        z3 = z3 
        e3 = e3 + energyfactorstatichover
        dist3 = dist3

    energy3 = e3

    [x3,y3,z3]
    ##print([x3,y3,z3])
    #%stepUAV1 = [[x3,y3,z3], energy3]
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ## to keep UAV within coverage region
    if (x3 > matxMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(x3 - matxMax[0])
        #% Walk in the x direction.
        x3 = matxMax[0] - distanceBeyond
    elif (x3 < matxMin[0]):
        #% It's past the left edge
        distanceBeyond = abs(matxMin[0] - x3)
        #% Walk in the x direction.
        x3 = matxMin[0] + distanceBeyond
    else:
        x3 = x3


    if (y3 > matyMax[0]):
        #% It's past the right edge
        distanceBeyond = abs(y3 - matyMax[0])
        #% Walk in the x direction.
        y3 = matyMax[0] - distanceBeyond
    elif y3 < matyMin[0]:
        #% It's past the left edge
        distanceBeyond = abs(matyMin[0] - y3)
        #% Walk in the x direction.
        y3 = matyMin[0] + distanceBeyond
    else:
        y3 = y3


    ##%%%% check for z
    if z3 > zMax:
         # % It's past the right edge
        distanceBeyond = abs(z3 - zMax)
        ##% Walk in the x direction.
        z3 = zMax - distanceBeyond
    elif z3 < zMin:
        #% It's past the left edge
        distanceBeyond = abs(zMin - z3)
        #% Walk in the x direction.
        z3 = zMin + distanceBeyond
    else:
        z3 = z3

    x3= abs(x3)
    y3 = abs(y3)
    z3 = abs(z3)

    done3= bool(energy3 <= 5000000 and z3>=390 and x3>=200 and x3<=300 and y3>=700 and y3<=800)
    ##done3= bool(energy3 <= 5000000 and z3>=390 and x3>=200 and x3<300 and y3>=700 and y3<800)
    ##done3= bool(energy3 <= 5000000 and z3>=390 and x3>=200 and y3>=700)




    obsUAVBL3 = [x3,y3,z3, energy3, done3, dist3]
    return obsUAVBL3
    #print(obsUAVBL3)
