import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10.10,0.0001)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,x,y2)
plt.title("Sine curve and cosine curve")
plt.xlabel('values of x')
plt.ylabel('values of y')
plt.grid()
plt.show()
