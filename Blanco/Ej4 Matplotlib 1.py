import numpy as np
import matplotlib as mpl

puntos = []
for i in range(10):
     x0 = np.random.randint(-10,10,size=2).tolist()
     x1 = np.random.randint(-10,10,size=2).tolist()
     puntos.append([x0,x1])
    
print (puntos)

def recta(a1,a2):
    m = (a1[1]-a2[1])/(a1[0]-a2[0])
    b = m*a1[0] + a2[1]
    return m, b

valores = []    
for i in range(len(puntos)):
    print (puntos[i][0],puntos[i][1])

    
for i in range(len(puntos)):
    recta(puntos[i][i][0],puntos[i][i][1])

print(valores)
        

