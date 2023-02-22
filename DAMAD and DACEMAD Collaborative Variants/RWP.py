import math
import random
import numpy.matlib
import numpy as np


def RWP(mob_x, mob_y):
    matxMax = [980]
    matxMin = [20]
    matyMax = [980]
    matyMin = [20]
    
    ###
    num_devices = len(mob_x)
    inc_xs =[]
    inc_ys =[]
    for i in range(num_devices):
        inc_x, inc_y = circle(random.randrange(-5, 5), random.randrange(-2, 2), random.randrange(0, 10), random.randrange(0, 360), random.uniform(0, 1))   
        inc_xs.append(inc_x)
        inc_ys.append(inc_y)

    newx = np.add(mob_x,inc_xs)
    newy = np.add(mob_y,inc_ys)
    for i in range(num_devices):
        if (newx[i] > matxMax):
            # It's past the right edge
            distancemBeyond = abs(newx[i] - matxMax);
            #% Walk in the x direction.
            newx[i] = matxMax - distancemBeyond;
        elif (newx[i] <matxMin):
            #% It's past the left edge
            distancemBeyond = abs(matxMin - newx[i]);
            #% Walk in the x direction.
            newx[i] = matxMin + distancemBeyond;
        else:
            newx[i] = newx[i]
            #######
        if (newy[i] > matyMax):
            # It's past the right edge
            distancemBeyond = abs(newy[i] - matyMax);
            #% Walk in the x direction.
            newy[i] = matyMax - distancemBeyond;
        elif (newy[i] <matyMin):
            #% It's past the left edge
            distancemBeyond = abs(matyMin - newy[i]);
            #% Walk in the y direction.
            newy[i] = matyMin + distancemBeyond;
        else:
            newy[i] = newy[i]
    return newx, newy




def circle(a,b,r,t, pause_prob):
    if pause_prob>0.5:
        cosinus = r*math.cos(t)
        sinus = r*math.sin(t) 
        x = a + cosinus
        y = b + sinus
    else:
        x = 0
        y = 0
    return x,y


