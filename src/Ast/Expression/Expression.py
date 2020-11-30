from src.Ast.Expression.ExprResult import ExprResult
from abc import ABC,abstractmethod
from src.Ast.Nodo import Nodo

class Expression(Nodo):
	'''
		Esta clase representa un expresion de
		cualquier tipo
	'''

	def __init__(self, linea: int, col: int):
		super().__init__(linea, col)

	@abstractmethod
	def execute(self) -> ExprResult:
		"""

		:rtype: object
		"""
		pass