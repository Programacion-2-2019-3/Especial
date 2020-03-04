# para trabajar los últimos m números seasn positivos
import numpy as np 
#Número de números aleatorios
n = 30
#Números a comparar
m = 5
contador1 = 0
contador2 = 0
while contador2 != m:
	alea = np.random.randint(-5,5,n)
#	print(alea)
	contador2 = 0
	contador1 += 1
	for i in range(1,m+1):
		if alea[n-i] >= 0:
			contador2 += 1
print(f"Fueron {contador1} intentos, y el vector final es:\n{alea}")
x=alea
print (x)
        