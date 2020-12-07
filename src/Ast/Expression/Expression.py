from src.Ast.Expression.ExprResult import ExprResult
from abc import ABC,abstractmethod
from src.Ast.Nodo import Nodo
from src.Ast.TablaSimbolo import Entorno

class Expression(Nodo):
	'''
		Esta clase representa un expresion de
		cualquier tipo
	'''

	def __init__(self, linea: int, col: int):
		super().__init__(linea, col)

	@abstractmethod
	def execute(self,entorno:Entorno) -> ExprResult:
		"""
			:rtype: object
		"""
		pass