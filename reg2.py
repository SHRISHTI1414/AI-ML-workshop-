import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample data
x = np.arange(0, 10)
area = [2, 3, 9, 5, 6, 7, 8, 9, 2, 4]
prices = [10, 40, 30, 40, 50, 60, 70, 80, 90, 100]
y = [3, 4, 10, 7, 9, 8, 9, 10, 7, 18]

# Combine x and area into 2D features
X = np.column_stack((x, area))

# Polynomial transformation (degree 2 or 3 is good for 3D)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit model
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, area, y, color='blue', label='Actual')
ax.scatter(x, area, y_pred, color='red', label='Predicted')

ax.set_xlabel('x')
ax.set_ylabel('Area')
ax.set_zlabel('y')
plt.title("3D Polynomial Regression")
plt.legend()
plt.show() 