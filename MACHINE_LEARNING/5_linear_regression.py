import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error as mse


diabetes = datasets.load_diabetes()

diabetes_x = np.array([[1], [2], [3]])


diabetes_x_train = diabetes_x
diabetes_x_test = diabetes_x

diabetes_y_train = np.array([[3], [2], [4]])
diabetes_y_test = np.array([[3], [2], [4]])


model = linear_model.LinearRegression()
model.fit(diabetes_x_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_x_test)

print("Mean squared error is:", mse(diabetes_y_test, diabetes_y_predicted))
print("Weights (value of tan(theta)):", model.coef_)
print("Intercept:", model.intercept_)

 
plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_predicted)
plt.show()






