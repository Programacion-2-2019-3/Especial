#¿COMO HACER PARA QUE LOS ÚLTIMOS NÚMEROS DE UN VECTOR ALEATORIO SEAN IGUALES?
#importamos la paquetería numpy
import numpy as np
#asignamos una variable para el tamaño del vector
n=30
#asignamos una variable que indique la constante que queremos igual.
numerofinal=5 # el número final debe ser menor que el rango del vector aleatorio
#
numerodeiguales=5 #menor a la cantidad de entradas del vector (posición n-1,n)
contador1=0 # va a contar si n-1=numerofinal y n=numerofinal 
contador2=0 #numero de intentos
while contador1!=numerodeiguales:
    contador1=0
    contador2+=1
    aleatorio=np.random.randint(-5,6,n) #crea el vector aleatorio
    for i in range(1,numerodeiguales+1):
        #print("i: ",i)
        if aleatorio[n-i]==numerofinal:
            contador1=contador1+1
print("Número de intentos: ",contador2)
print("vector aleatorio: ",aleatorio)
#________________________________________________________________________
#para intercambiar posiciones
#vectorn=[]
#for i in range(n):
#    vectorn.append(aleatorio[i])
#vectorn[4]=aleatorio[0]
#vectorn[0]=aleatorio[4]
#print("vector intercambiado: ",vectorn)