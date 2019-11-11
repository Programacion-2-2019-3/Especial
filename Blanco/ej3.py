import numpy as np
import matplotlib.pyplot as plt

a=2
b=0
x = np.linspace(0, 5, 500)
y0 = np.sin(x)
#print (y0)
y1 = np.cos(x)
#print (y1)
y2 = a*x+b
#print (y2)
y3 = np.arctan(x)
#print (y3)
a0=[]
for idx, (i,j,k,l) in enumerate(zip(y0,y1,y2,y3)):
    if i==j==k==l:
        a0.append(zip(y0,y1,y2,y3)[(i,j,k,l)])
    else : 
        a0.append(0)
print (a0)

fig, ax = plt.subplots()
ax.plot(x,y0)
ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y3)

plt.show()