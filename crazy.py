# 📚 Importing the big shots
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 📦 Data - Aaj simple rakhte hain
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)   # reshape => bhai model ko table chahiye
y = np.array([5, 9, 15, 23, 35, 49])             # nonlinear target (jaise zindagi 😅)

# 🎩 Polynomial Features - Magic trick!
poly = PolynomialFeatures(degree=2)              # Degree 2 polynomial (quadratic curve)
X_poly = poly.fit_transform(X)                   # Bana diya X^2, X, 1 — 3 columns

# 🧠 ML Model - Ab model sikhega
model = LinearRegression()
model.fit(X_poly, y)                             # Train kar diya model

# 🔮 Prediction
X_test = np.linspace(1, 6, 100).reshape(-1, 1)   # Smooth input for sexy curve
X_test_poly = poly.transform(X_test)             # Transform test input
y_pred = model.predict(X_test_poly)              # Predict kar diya

# 🎨 Plotting ka jaadu
plt.scatter(X, y, color='red', label="Original Data")
plt.plot(X_test, y_pred, color='blue', label="Polynomial Curve")
plt.title("🔥 Crazy Polynomial Regression 🔥")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
