from matplotlib import pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = False
delta = 0.025

fig, ax = plt.subplots(figsize=(5,5))

xrange = np.arange(-20.0, 20.0, delta)
yrange = np.arange(-20.0, 20.0, delta)
x, y = np.meshgrid(xrange, yrange)


def animate(n):
    ax.clear()
    l = n/10
    equation = 2.8*(x*math.cos(l)-y*math.sin(l))**2*((x*math.cos(l)-y*math.sin(l))**2*(2.5*(x*math.cos(l)-y*math.sin(l))**2+(x*math.sin(l)+y*math.cos(l))**2-2)+1.2*(x*math.sin(l)+y*math.cos(l))**2*((x*math.sin(l)+y*math.cos(l))*(3*(x*math.sin(l)+y*math.cos(l))-0.75)-6.0311)+3.09)+0.98*(x*math.sin(l)+y*math.cos(l))**2*(((x*math.sin(l)+y*math.cos(l))**2-3.01)*(x*math.sin(l)+y*math.cos(l))**2+3)-1.005
    cont=plt.contour(x,y, equation, [0])
    plt.axis('square')
    return cont

ani = animation.FuncAnimation(
    fig, animate,frames=63, interval=0.1, repeat = True)

ani.save('test.gif',writer=PillowWriter(fps=30))

plt.show()
