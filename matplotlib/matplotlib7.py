# Example Python Program to plot Cardioids that are

# symmetric around y axis

 

# import the numpy and pyplot modules

import numpy as np

import matplotlib.pyplot as plot

 

fig  = plot.figure()

fig.add_subplot(211, projection='polar')

 

# Set the title of the polar plot

plot.title('k-leaf roses in polar format:radius = a + (b*cos(k*radian))')

 

# Radian values upto 2*pi

rads    = np.arange(0, (2*np.pi), 0.01)

 

a   = 1

b   = 1

k   = 4

 

# a = -1 and b = -1

for radian in rads:

    radius = a + (b*np.cos(k*radian))

   

    # Plot the cardioids in polar co-ordinates

    plot.polar(radian, radius, 'v')

 

a = a+1

b = b+1

k = 5

fig.add_subplot(212, projection='polar')

 

# a = -2 and b = -2

for radian in rads:

    radius = a + (b*np.cos(k*radian))

    # Plot in polar co-ordinates

    plot.polar(radian, radius,'v')    

 

# Display the cardioids -

plot.show()