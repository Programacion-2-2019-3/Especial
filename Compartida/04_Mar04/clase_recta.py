class clase_recta(object):
	"""docstring for clase_recta"""
	def __init__(self, arg):
		super(clase_recta, self).__init__()
		self.arg = arg
		print('clase=',self.arg)

	def funcion1(self,valor1):
		print('El valor ingresado es:',valor1)