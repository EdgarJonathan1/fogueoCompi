from src.Ast.Expression.Expression import Expression
from src.Ast.Expression.ExprResult import ExprResult
from src.Ast.Expression.Tipo import Tipo
from src.Ast.TablaSimbolo import Entorno

#todo: hacer resta y terminar el ejemplo

class Division(Expression):
	'''
		Esta clase recibe dos operadores para realizar la suma
	'''
	def __init__(self, izq: Expression, der: Expression, linea: int, col: int):
		super().__init__(linea, col)
		self.izq = izq
		self.der = der

	def execute(self,entorno:Entorno) -> ExprResult:
		izqResult:ExprResult = self.izq.execute(entorno)
		derResult:ExprResult = self.der.execute(entorno)

		if izqResult.tipo != Tipo.DOUBLE or derResult.tipo != Tipo.DOUBLE:
			msg:str = "Error Semantico: linea:"+str(self.izq.linea)+" Col:"+str(self.izq.col)+\
					  "algun uno de los operadores no cumple con ser Double"
			return ExprResult(Tipo.ERROR,msg)

		result:float = float(izqResult.value) / float(derResult.value)
		return ExprResult(Tipo.ERROR,result)
