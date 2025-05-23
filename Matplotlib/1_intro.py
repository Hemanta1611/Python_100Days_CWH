import numpy as np
import matplotlib.pyplot as plt


'''
np.random.random(50): This part generates an array of 50 random floating-point numbers 
uniformly distributed between 0 and 1. np.random.random() function generates random numbers 
from a uniform distribution over the half-open interval [0.0, 1.0).

* 100: This part multiplies each of the random numbers generated by np.random.random() by 100. 
This scales the random numbers to be uniformly distributed between 0 and 100 instead of between 0 and 1.'''

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

# plt.scatter(x_data, y_data, c = "red", marker=",", alpha=0.4, )
# plt.show()



XX_data = np.random.uniform(10, 100, 50)
'''np.random.uniform(10, 100, 50): This function generates an array of 50 random floating-point 
numbers uniformly distributed between 10 and 100. The first argument 10 is the lower bound (inclusive), 
the second argument 100 is the upper bound (exclusive), and the third argument 50 specifies the size of the array.'''


years = [2003 + x for x in range(20)]
print(len(years))
weights = [4, 6, 10, 20, 24, 28, 32, 35, 38, 40, 42, 44, 45, 47, 48, 49, 50, 51, 53, 55]
print(len(weights))

plt.plot(years, weights, c='b', lw=2, linestyle="--")
plt.show()



