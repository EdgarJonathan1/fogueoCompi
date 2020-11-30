from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.Expression.Tipo import Tipo


class Suma(Expression):
	'''
		Esta clase recibe dos operadores para realizar la suma
	'''
	def __init__(self, izq: Expression, der: Expression, linea: int, col: int):
		super().__init__(linea, col)
		self.izq = izq
		self.der = der

	def execute(self) -> ExprResult:

		izqResult:ExprResult = self.izq.execute()
		derResult:ExprResult = self.der.execute()

		if izqResult.tipo==Tipo.DOUBLE and derResult.tipo==Tipo.DOUBLE:
			result:float = float(izqResult.value) + float(derResult.value)
			return ExprResult(Tipo.DOUBLE,result)

		elif izqResult.tipo==Tipo.STRING and derResult.tipo==Tipo.STRING:
			result:str = str(izqResult.value) + str(derResult.value)
			return ExprResult(Tipo.STRING,result)

		elif izqResult.tipo==Tipo.STRING and derResult.tipo==Tipo.DOUBLE:
			result:str = str(izqResult.value) + str(derResult.value)
			return ExprResult(Tipo.STRING,result)

		elif izqResult.tipo==Tipo.STRING and derResult.tipo==Tipo.BOOLEAN:
			result:str = str(izqResult.value) + str(derResult.value)
			return ExprResult(Tipo.STRING,result)


		return ExprResult(Tipo.ERROR,"Alguns tipos de datos no son permitidos")