import math
from sumo_position_data import update_low
from sumo_position_data import update_M50
import matplotlib.pyplot as plt
import numpy as np



for i in range(100, 1100):
    data =np.array(update_M50(i))
    x = data[0]*4000
    y = data[1]*6000 
    plt.plot(x,y,'r.')    
    plt.draw()
    plt.pause(0.5)
    plt.clf()
