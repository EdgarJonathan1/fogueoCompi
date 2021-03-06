from abc import ABC, abstractmethod
from src.Ast.Nodo import Nodo
from src.Ast.TablaSimbolo import Entorno

class Statement(Nodo):
	'''
		Esta clase representa a una instruccion del lenguaje
	'''

	def __init__(self, linea: int=0, col: int=0):
		super().__init__(linea, col)

	@abstractmethod
	def execute(self,entorno:Entorno) -> None:
		pass
