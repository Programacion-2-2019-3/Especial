#¿CÓMO HACER QUE TODOS LOS NÚMEROS DE UN VECTOR ALEATORIO SEAN POSITIVOS?
#se importa la libreria numpy
import numpy as np
#asignamos una variable para la cantidad de números aleatorios
n=5
#generamos un contador que nos cuente los números positivos que van saliendo en cada vector 
contador1=0
#generamos otro contador que nos cuente los intentos 
contador2=0
#pedimos al programa que hacer mientras no se tengan los n números positivos.
while contador1 !=n:
    contador1=0
    contador2+=1
    aleatorio = np.random.randint(-5,5,n)
#pedimos al programa que cuando un número sea positivo, se aumente el contador de los positivos   
    for i in aleatorio:
        if i>=0:
            contador1+=1
#pintamos  los intentos y el vector que se genera con todos los positivos.
print("intentos: ",contador2," vector aleatorio: ",aleatorio)
  
