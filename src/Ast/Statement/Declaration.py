from src.Ast.Statement.Statement import Statement
from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.Expression.Tipo import Tipo

class Declaration(Statement):

	def __init__(self,tipo:Tipo,identifier:str, val:Expression):
		super().__init__()
		self.tipo = tipo
		self.identifier = identifier
		self.val = val

	def execute(self) -> None:
		exprResult:ExprResult = self.val.execute()

