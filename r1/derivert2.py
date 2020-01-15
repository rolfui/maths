import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1/x
    #return x**2 + 2*x + 1
def derivert(x, delta_x):
    return (f(x+delta_x)-f(x))/delta_x

#x = np.linspace(-10,10,1000)
#y = f(x)

x_vals=[]
y_vals=[]
y_der_vals=[]
x_step=0.1
x_min=-5.0
x_max=5.0
y_min=0
y_max=0
y=0

i=x_min
while i<=x_max:
    try:
        x_vals.append(i)
        
        y=f(i)
        if y<y_min: y_min=y
        if y>y_max: y_max=y
        y_vals.append(y)
        
        y=derivert(i,1E-10)
        if y<y_min: y_min=y
        if y>y_max: y_max=y
        y_der_vals.append(y)
    except:
       print("Illegal value for x:",i)
    i=i+x_step

plt.xlim(x_min,x_max)
plt.ylim(-10,10)

plt.plot(x_vals,y_vals)
plt.plot(x_vals,y_der_vals)
plt.grid()
plt.show()

#print(x_vals)
