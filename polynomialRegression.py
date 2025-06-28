import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
x= np.arange(0,10)
print(x)
x=x.reshape(-1,1)
print(x)
y=[3,4,5,7,9,8,9,10,12,18]
print(y)
plt.scatter(x,y)
plt.show()

