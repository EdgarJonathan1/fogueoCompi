from src.Ast.Statement.Statement import Statement
from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.TablaSimbolo import Entorno

class Assignment(Statement):

	def __init__(self,identifier:str, val:Expression):
		super().__init__()
		self.identifier = identifier
		self.val = val

	def execute(self,entorno:Entorno) -> None:
		exprResult:ExprResult = self.val.execute(entorno)

		print('Valor de la asignacion: ',exprResult.value)


