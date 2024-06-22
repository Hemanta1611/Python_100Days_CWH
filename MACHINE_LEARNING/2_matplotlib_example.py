from matplotlib import pyplot as plt
from matplotlib import style
x = [1, 5, 4]
y = [4, 8, 9]
x2 = [3, 7, 3]
y2 = [5, 8, 2]
plt.scatter(x, y, label="first")
plt.plot(x2, y2, label="second")
plt.title("Random Bhai Data")
plt.ylabel("This is Y")
plt.xlabel("This is X")
plt.legend()
plt.show()