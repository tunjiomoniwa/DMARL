import numpy as np
import time
import matplotlib.pyplot as plt
from sumo_position_data import update

#Fxn that reads from our csv file
##def update(kk):
##        
##        x= []
##        y= []
##        with open("Output_position_data.csv",newline='') as f:
##                ereader = csv.DictReader(f)                
##                for row in ereader:
##                    if float(row['time']) == kk:
##                        x.append(float(row['xnew'])*3000)
##                        y.append(float(row['ynew'])*3000)                        
##        return x, y
cc= update(0)
#print(cc[0])
#print(cc[1])


# creating initial data values
# of x and y
x = cc[0]
y = cc[1] 

# to run GUI event loop
plt.ion()

# here we are creating sub plots
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(x, y, '.')

# setting title
plt.title("Dublin City Centre with HDVs Deployed (SUMO)", fontsize=14)

# setting x-axis label and y-axis label
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")

# Loop
for i in range(50):
	# creating new X & Y values	
	new_val = update(i)
	new_x = new_val[0]
	new_y = new_val[1]

	# updating data values
	line1.set_xdata(new_x)
	line1.set_ydata(new_y)

	# drawing updated values
	figure.canvas.draw()

	# This will run the GUI event
	# loop until all UI events
	# currently waiting have been processed
	figure.canvas.flush_events()

	time.sleep(0.001)
