import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x,y):
    m_curr=b_curr=0
    rate=0.1
    n=len(x)
    for i in range(109):
    
        y_pred=m_curr*x +b_curr
        plt.plot(x,y_pred,color="blue")
        mse=(1/n) * sum([val**2 for val in (y-y_pred)])
        print(mse)
        md=-(2/n)* sum(x*(y-y_pred))
        bd=-(2/n)* sum(x*(y-y_pred))
        
        m_curr=m_curr -rate*md
        b_curr=b_curr -rate*bd
    plt.show()
        
        
        
        
        

x=np.array([1,2,3,4,5])
y=np.array([5,6,9,11,13])
gradient_descent(x,y)


