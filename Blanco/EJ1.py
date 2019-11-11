# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 06:45:41 2019

@author: Pregrado
"""

# generar n aleatorios [-5,5], contar cuantos son positivos cuanto son negativos


import numpy as np

n0=np.random.randint(-5, 5, size =16)
print(n0)

Pos = 0
Neg = 0
Zero = 0
for iter in n0:
     if iter > 0:
         Pos +=1
     elif iter < 0:
         Neg +=1
     else:
         Zero +=1
print ("P = ",Pos) 
print("N = " ,Neg)
p=n0>0
print ("p2 = ",p,np.sum(p))
print (Zero)

# generar n aleatorios [-5,5] m veces hasta que todos ellos sean postivos y mostrar cuantos intentos tomo
s0=2
n1=np.random.randint(-5,5, size=s0)
print (n1)
P1=0
c1 =0
while P1<s0:
    c1 += 1
    for iter in n1:
     if iter > 0:
         P1 += 1
    if P1 < s0:
        P1 = 0
        n1=np.random.randint(-5,5, size=s0)
        print (n1)
             
print (c1)

#generar numeros aleatorios entre [-5,5] hasta que 2 numeros consecutivos sean positivos
#matplotlib
s1=2
n2=np.random.randint(-5,5, size=s1)
print (n2)

