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

for i in range(len(x0[0])):
    mpl.pyplot.plot(x0[:,i],y0[:,i])
    mpl.pyplot.grid()
    mpl.pyplot.text(np.mean(x0[:,i]),np.mean(y0[:,i]),'R'+str(i))
    
    if i == n-1:
        break
    #print('i=',i)
    for j in range(i+1,n):
        # verificar los cruces entre recta i y recta j (y graficar)        
        #xc,yc = cruce(x0,y0,i,j)
        xc,yc = 1 ,3
        mpl.pyplot.plot(xc,yc,'ko')
        pass

