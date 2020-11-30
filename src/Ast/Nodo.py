from abc import ABC,abstractmethod

class Nodo(ABC):
	'''
		Esta la clase que representa todos los nodos del ast
	'''
	def __init__(self,linea:int =0 ,col:int=0):
		self.linea = linea
		self.col = col