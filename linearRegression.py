import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([[300],[400],[500],[600],[700]])
#print(x)
y=np.array([[150],[200],[300],[370],[430]])
y
model = LinearRegression()
model.fit(x,y)

predicted = model.predict(x)
predicted
#model.coef_
#model.intercept_
plt.scatter(x, y, color='blue', label='Actual data') 
plt.plot(x, predicted, color='red', label='Regression line')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

