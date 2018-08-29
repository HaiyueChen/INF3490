import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 100)

def f(x):
    return -x**4 + 2*x**3 + 2*x**2-x

start = -2
end = 3

iter = -2
max = f(iter)

while(iter < end):
    current = f(iter)
    if(current > f(max)):
        max = iter
    iter += 0.01

print(max)
plt.plot(max, f(max), color="red", marker="s")
plt.plot(x, f(x))
plt.show()
