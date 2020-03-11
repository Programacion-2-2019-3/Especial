class clase_rectas(object):
	"""docstring for clase_rectas
	puntos1 [[1, 4], [11, -4]]
	puntos2 [[-9, 4], [-9, 4]]
	p1->(1,4) y p2->(-9,4) corresponden a la recta 1
	 """
	import numpy as np 
	def __init__(self, arg=0):
		super(clase_rectas, self).__init__()
		self.arg = arg
		self.puntos1 = []
		self.puntos2 = []
		print('Instancia creada')

	def adicionar_recta(self,p1,p2): # debe cumplir p1->[puntos1,puntos2] y p2->[x1,y1]
		self.puntos1.append(p1)
		self.puntos2.append(p2)

	def extraer_xy(self):
		#x=[]
		x = [i[0] for i in self.puntos1]
		x.append(self.puntos2[-1][0])
		y = [i[1] for i in self.puntos1]
		y.append(self.puntos2[-1][1])
		return [x,y]

	def cruces(self,valor1,valor2):
		
		#print('El valor ingresado es:',valor1)
		pass