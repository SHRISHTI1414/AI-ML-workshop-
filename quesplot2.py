import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

 
y = np.array([1127, 1460, 861, 1295, 1131, 1096, 1725, 1045, 163, 1892])

math_scores = np.random.normal(loc=70, scale=5, size=10)
science_scores = np.random.normal(loc=60, scale=6, size=10)
hindi_scores = np.random.normal(loc=80, scale=4, size=10)

x = np.arange(len(y))   

plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, math_scores, width=0.2, label='Math', color='skyblue')
plt.bar(x, science_scores, width=0.2, label='Science', color='lightgreen')
plt.bar(x + 0.2, hindi_scores, width=0.2, label='Hindi', color='salmon')

plt.xticks(x, y, rotation=45)
plt.xlabel("Student ID")
plt.ylabel("Scores")
plt.title("Student Scores by Subject")
plt.legend()
plt.tight_layout()
plt.show()