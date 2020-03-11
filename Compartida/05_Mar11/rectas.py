# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 06:40:26 2020

@author: aulasfce1
"""
import numpy as np
import matplotlib as mpl

n = 5 # cantidad de tramos de recta
x0 = np.random.randint(-10,10,size=[2,n]) # (x,y)
y0 = np.random.randint(-10,10,size=[2,n])

def recta(a1,a2): # a1 -> (x,y)
    m = (a1[1]-a2[1])/(a1[0]-a2[0]) # y = mx+b
    b = -m*a1[0] + a1[1]
    return m, b

#print(x0)
#print(x0[:,0])
#print(y0)

for i in range(len(x0[0])):
    mpl.pyplot.plot(x0[:,i],y0[:,i])
    mpl.pyplot.grid()
    mpl.pyplot.text(np.mean(x0[:,i]),np.mean(y0[:,i]),'R'+str(i))
    
    if i == n-1:
        break
    #print('i=',i)
    for j in range(i+1,n):
        # verificar los cruces entre recta i y recta j (y graficar)
        p1 = [x0[0][i],y0[0][i]]
        p2 = [x0[1][i],y0[1][i]]
        p3 = [x0[0][i],y0[0][i]]
        p4 = [x0[1][i],y0[1][i]]
        #print(p1,p2)
        #print(recta(p1,p2))
        #print('j=',j)
        m1,b1 = recta(p1,p2)
        m2,b2 = recta(p3,p4)
        
        xc,yc = cruce(m1,b1,m2,b2)
        # y1 = m1x1+b1
        # y2 = m2x2+b2
        pass



