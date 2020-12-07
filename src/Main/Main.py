from  src.Parser import gramatica as g
from src.Ast.Statement.Statement import Statement

if __name__ == '__main__':

        # TODO: leer libro capitulo 6 del dragon

	f = open("./entrada.txt", "r")
	input = f.read()
	#print(input)
	stmts = g.parse(input)

	i=0
	while i < len(stmts):
		stmt = stmts[i]
		stmt.execute({})
		i+=1
