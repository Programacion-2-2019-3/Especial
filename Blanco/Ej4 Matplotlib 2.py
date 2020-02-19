#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib as mpl

get_ipython().run_line_magic('matplotlib', 'inline')

x0 = np.random.randint(-10,10,size=2)
x1 = np.random.randint(-10,10,size=2)
x2 = np.random.randint(-10,10,size=2)
x3 = np.random.randint(-10,10,size=2)
print (x0)
print (x1)
print (x2)
print (x3)

puntos = []
#puntos = np.array()

for i in range(6):
    x0 = np.random.randint(-10,10,size=2)
    x1 = np.random.randint(-10,10,size=2)
    puntos.append([x0,x1])
    #print(i)
print(puntos)
print(puntos[2])
print(puntos[2][0],puntos[2][1])
print(len(puntos))

for i in range(len(puntos)):
    
    
    pass
    


# In[5]:


def recta(a1,a2):
    m = (a1[1]-a2[1])/(a1[0]-a2[0])
    b = m*a1[0] + a2[1]
    return m, b
    #if m!=0 and b==b:
     #   return m, b
    #else:
     #   m=0, b
    
m1, b1 = recta(x0, x1)
m2, b2 = recta(x0, x2)
m3, b3 = recta(x0, x3)
m4, b4 = recta(x1, x2)
m5, b5 = recta(x1, x3)
m6, b6 = recta(x2, x3)

def inter(a1, a2, a3, a4):
    a=(a4 - a2)/(a3 - a1)
    return a


# In[6]:


x = np.linspace(-10,10,50)
y1 = m1*x + b1
y2 = m2*x + b2
y3 = m3*x + b3
y4 = m4*x + b4
y5 = m5*x + b5
y6 = m6*x + b6


# In[7]:



mpl.pyplot.plot(x, y1, '.', x, y2, '*', x, y3, 'o', x, y4, 'v', x, y5, '^', x, y6, 's')


# In[ ]:




