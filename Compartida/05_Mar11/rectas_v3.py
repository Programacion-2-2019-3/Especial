# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 06:40:26 2020

@author: aulasfce1
"""
import numpy as np
import matplotlib as mpl
from clase_rectas import *

n = 5 # cantidad de tramos de recta
x0 = np.random.randint(-10,10,size=[2,n]) # (x,y)
y0 = np.random.randint(-10,10,size=[2,n])

#print('\nvalores de x0\n',x0)
#print('\nvalores de y0\n',y0)

rectas1 = clase_rectas()
rectas2 = clase_rectas()
#rectas1.funcion1(76)
rectas1.adicionar_recta([0,0],[2,2])
rectas1.adicionar_recta([2,2],[3,0])
rectas1.adicionar_recta([3,0],[5,1])

rectas2.adicionar_recta([-3,0],[5,-1])
#arre
#print('x0',lista_x0)
#print('y0',lista_y0)
x,y = rectas1.extraer_xy()
print(x,y)

mpl.pyplot.plot(x,y)

x2,y2 = rectas2.extraer_xy()
mpl.pyplot.plot(x2,y2)
mpl.pyplot.grid()

rectas1.cruces([x,y],[x2,y2])

#for i in range(len(x0[0])):
#    mpl.pyplot.plot(x0[:,i],y0[:,i])
#    mpl.pyplot.grid()
#    mpl.pyplot.text(np.mean(x0[:,i]),np.mean(y0[:,i]),'R'+str(i))
#    
#    if i == n-1:
#        break
#    print('i=',i)
#    for j in range(i+1,n):
#        # verificar los cruces entre recta i y recta j (y graficar)        
#        #xc,yc = cruce(x0,y0,i,j)
#        xc,yc = 1 ,3
#        mpl.pyplot.plot(xc,yc,'ko')
#        pass

