# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 06:29:35 2019

@author: Pregrado
"""

import numpy as np

n=np.random.rand(4,3) #Genera aleatorios entre 0 Y 1
print(n)
n1=np.random.randint(8, size=(3,5)) #Genera aleatorios hasta el numero indicado
print(n1)
n2=np.random.randint(1,29, size=(7,5)) # genera aleatorios entre los numeros indicados
print(n2)
n3=np.random.randn() #Genera un aleatorio tomado de la distribucion normal
print(n3)
n4=np.random.randn(3,3) #Genera una matriz de aleatorios con la distribucion normal
print(n4)
n5=np.random.bytes(10) #Genera un numero alatorio de Bytes
print (n5)

int_list = [5, 7, 13, 19, 29, 31]
sum = 0
for iter in int_list:
    sum += iter
print(sum)

vowels="AEIOU"
for iter in vowels:
    print("char:", iter)

a=1
while a<7:
    a +=1
print (a)

i = 1
suma = 0
while i <= 100:
    suma += i
    i += 1
print(suma) 