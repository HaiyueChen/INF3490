import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return -x**4 + 2*x**3 + 2*x**2-x

def df(x):
    return -4*x**3 + 6*x**2 + 4*x - 1

x = np.linspace(-2, 3, 100)

start = random.uniform(-2, 3)
gradient = df(start)
print("gradient start:", gradient)
print("start:", start)
iteration = 0

while(iteration < 99 and gradient != 0):
    if(gradient < 0):
        start -= 0.1
    elif(gradient > 0):
        start += 0.1
    gradient = df(start)
    iteration += 1


print("ending point:", start)


plt.plot(start, f(start), color="red", marker="s")
plt.plot(x, f(x))
plt.show()
