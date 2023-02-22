import math
import random
import numpy.matlib
import numpy as np


def GMM(mob_x, mob_y):
    matxMax = [980]
    matxMin = [20]
    matyMax = [980]
    matyMin = [20]
    
    ###
    num_devices = len(mob_x)
    inc_xs =[]
    inc_ys =[]
    for i in range(num_devices):
        inc_x, inc_y = gauss(random.randrange(0, 360), random.randrange(0, 2), random.uniform(0, 1), 5)
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


def gauss(angle, trav_dist, alpha, avg_speed):
   angle = angle*alpha + avg_speed*(1-alpha) + math.sqrt((1-alpha**2)*random.uniform(0, 1))
   trav_dist = trav_dist*alpha + avg_speed*(1-alpha) + math.sqrt((1-alpha**2)*random.uniform(0, 1))
   x1,y1 = pol2cart(trav_dist, angle)
   x = x1 + random.uniform(0, 1)*math.cos(angle)
   y = y1 + random.uniform(0, 1)*math.sin(angle)
   return x, y

    

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


