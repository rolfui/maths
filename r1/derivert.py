# -*- coding: utf-8 -*-
import matplotlib 
import matplotlib.pyplot as plt
import numpy 


def derivert(f, x, delta_x):
    return (f(x+delta_x)-f(x))/delta_x

def f(x):
    return x**2 + 2*x + 1

x = numpy.linspace(-10,10,1000)
y = f(x)
plt.xlim(-2,2)
plt.ylim(-1,3)
plt.plot(x,y)

y = derivert(f,x,1E-10)
plt.plot(x,y)

plt.grid()
plt.show()

