from src.Ast.Statement.Statement import Statement
from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult

class ExpressionStatement(Statement):

	def __init__(self,val:Expression):
		super().__init__()
		self.val = val

	def execute(self) -> None:
		self.val.execute()


