import numpy as np
import matplotlib as mpl

i= 4
while i<8:
    global x_i
    x_i= np.random.randint(-10,10,size=2)
    i +=1
    
x0 = np.random.randint(-10,10,size=2)
x1 = np.random.randint(-10,10,size=2)
x2 = np.random.randint(-10,10,size=2)
x3 = np.random.randint(-10,10,size=2)
print (x0)
print (x1)
print (x2)
print (x3)

def recta(a1,a2):
    m = (a1[1]-a2[1])/(a1[0]-a2[0])
    b = m*a1[0] + a2[1]
    return m, b
    #if m!=0 and b==b:
     #   return m, b
    #else:
     #   m=0, b
    
m1, b1 = recta(x0, x1)
m2, b2 = recta(x0, x2)
m3, b3 = recta(x0, x3)
m4, b4 = recta(x1, x2)
m5, b5 = recta(x1, x3)
m6, b6 = recta(x2, x3)

def inter(a1, a2, a3, a4):
    a=(a4 - a2)/(a3 - a1)
    return a

x = np.linspace(-10,10,50)
y1 = m1*x + b1
y2 = m2*x + b2
y3 = m3*x + b3
y4 = m4*x + b4
y5 = m5*x + b5
y6 = m6*x + b6

mpl.pyplot.plot(x, y1, '.', x, y2, '*', x, y3, 'o', x, y4, 'v', x, y5, '^', x, y6, 's')

#for i in range(1,6):
 #   for j in range(1,6):
  #      if i>j:
   #         pass
    #    else:
     #       ai= inter(m_i, b_i, m_i+1, b_i+1)
