import matplotlib.pyplot as plt
import numpy as np


def f(x):
    #return 1/x
    return x**2 + 2*x + 1

def derivert(x, delta_x):
    return (f(x+delta_x)-f(x))/delta_x

x = np.linspace(-10,10,1000)
y = f(x)

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.plot(x,y)

y = derivert(x,1E-10)
plt.plot(x,y)

plt.grid()
plt.show()
