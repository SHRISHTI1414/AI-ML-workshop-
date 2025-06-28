import matplotlib.pyplot as plt
year=[10,20,30,40,50]
pop=[1,2,3,4,5]

plt.plot(year,pop)
plt.xlabel("year")
plt.ylabel("population")
plt.title("world population")
plt.yticks([0,2,4,6,8],['0B','1B','2B','3B','4B'])

plt.grid(True)

plt.show()

