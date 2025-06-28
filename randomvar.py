import numpy as np
dice1=np.random.randint(1,7,size=3)
dice2=np.random.randint(1,7,size=3)
print(dice1)
print(dice2)
dice3=dice1+dice2
count=np.count_nonzero(dice3==7)
print(count)
