from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.Expression.Tipo import Tipo
from src.Ast.TablaSimbolo import Entorno


class DoubleLiteral(Expression):
	def __init__(self, valor:float, linea: int, col: int):
		super().__init__(linea, col)
		self.valor = valor

	def execute(self,entorno:Entorno) -> ExprResult:
		return ExprResult(Tipo.DOUBLE,self.valor)

class BooleanLiteral(Expression):
	def __init__(self, valor:float, linea: int, col: int):
		super().__init__(linea, col)
		self.valor = valor

	def execute(self,entorno:Entorno) -> ExprResult:
		return ExprResult(Tipo.BOOLEAN,self.valor)
