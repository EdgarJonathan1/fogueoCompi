from src.Ast.Expression import Tipo

class ExprResult:
	'''
		esta clase se retorna al ejecutar el metodo execute
	'''
	def __init__(self,tipo:Tipo,value:any):
		self.tipo = tipo
		self.value = value

