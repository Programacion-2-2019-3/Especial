#¿CÓMO CONTAR cuántos NÚMEROS ALEATORIOS POSITIVOS Y NEGATIVOS HAY EN UN VECTOR ALEATORIO?
#primero importamos la librería
import numpy as np
#asignamos una variable para la cantidad de aleatorios
n = 100
#se generan n aleatorios
aleatorios = np.random.randint(-5,5,n)
#se hace un contador para los números positivos
contarposi=0
#se hace un contador para los números negativos
contarneg=0
#le pedimos al programa que para cada número positivo se aumente el contador positivo, y de lo contrario se aumente el contador negativo.
for x in aleatorios:
    if x>=0:
        #contarposi=contarposi+1
        contarposi+=1
    else:
        #contarneg=contarneg+1
        contarneg+=1
#pedimos que se pinte el vector aleatorio
print("arreglo de aleatorios: ",aleatorios)
#pedimos que se pinte la cantidad de positivos
print("la cantidad de positivos es: ",contarposi)
#pedimos que se pinte la cantidad de negativos
print("la cantidad de negativos es: ",contarneg)        
        
        