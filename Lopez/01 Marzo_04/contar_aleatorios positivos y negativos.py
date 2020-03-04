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
ceros=0
#le pedimos al programa que para cada número positivo se aumente el contador positivo, y de lo contrario se aumente el contador negativo.
for x in aleatorios:
    if x>0:
        #contarposi=contarposi+1
        contarposi+=1
    elif x<0:
        contarneg+=1
    else:
        #contarneg=contarneg+1
        ceros+=1
#pedimos que se pinte el vector aleatorio
print("arreglo de aleatorios:\n",aleatorios)
#pedimos que se pinte la cantidad de positivos
print("\nla cantidad de positivos es:\n",contarposi)
#pedimos que se pinte la cantidad de negativos
print("\nla cantidad de negativos es:\n",contarneg)
#pedimos que se pinte la cantidad de ceros
print("\nla cantidad de ceros es:\n",ceros)
print(type(aleatorios))
print(aleatorios[5])

print(np.histogram(aleatorios))
