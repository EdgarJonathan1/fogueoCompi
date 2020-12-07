from src.Ast.Statement.Statement import Statement
from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.Expression.Tipo import Tipo
from src.Ast.TablaSimbolo import Entorno

class Declaration(Statement):

    #int id = 5
	def __init__(self,tipo:Tipo,identifier:str, val:Expression):
		super().__init__()
		self.tipo = tipo
		self.identifier = identifier
		self.val = val

	def execute(self,entorno:Entorno) -> None:
		exprResult:ExprResult = self.val.execute(entorno)

