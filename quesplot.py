import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.array([1127, 1460, 861, 1295, 1131, 1096, 1725, 1045, 163])

plt.figure(figsize=(8, 5))
sns.lineplot(data=arr, marker="o")
plt.title("Array Values Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()

