from src.Ast.Statement.Statement import Statement


class ListStatement(Statement):

	def __init__(self):
		super().__init__()
		self.stmts:[Statement] = []


	def add(self,stmt:Statement):
		self.stmts.append(stmt)

	def execute(self) -> None:
		for stmt in self.stmts:
			stmt.execute()

