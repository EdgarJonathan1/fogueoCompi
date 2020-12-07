# -----------------------------------------------------------------------------
# Ejemplo interprete Fogueo
# -----------------------------------------------------------------------------

reservadas = {

    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'struct': 'STRUCT',
    'return': 'RETURN',
    'print': 'PRINT',
    'scan': 'SCAN',
    'double': 'DOUBLE',
    'boolean': 'BOOLEAN',
    'string': 'STRING',
    'arreglo': 'ARREGLO',

#literales
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL'
}

tokens = [
             'PTCOMA',
             'LLAVIZQ',
             'LLAVDER',
             'PARIZQ',
             'PARDER',
             'IGUAL',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'MENQUE',
             'MAYQUE',
             'IGUALQUE',
             'NIGUALQUE',
#			 'MAY_IG_QUE'
#			 'MEN_IG_QUE',
#			 'OR',
             'AND',
             'MOD',
             'DECIMAL',
             'ENTERO',
             'CADENA',
             'ID'
         ] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='
#TODO: Arreglar los simbolos MAY_IG_QUE ETC...
#t_MAY_IG_QUE = r'>='
#t_MEN_IG_QUE = r'<='
#t_OR = r'||'
t_AND = r'&&'
t_MOD = r'%'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        #t.value = DoubleLiteral(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        #t.value = DoubleLiteral(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()
#lexer = lex.lex(debug=1)

# ********************************
# Definición de la gramática
# ********************************

from src.Ast.Expression.Suma import Suma
from src.Ast.Expression.Resta import Resta
from src.Ast.Expression.Modulo import Modulo
from src.Ast.Expression.Multiplicacion import Multiplicacion
from src.Ast.Expression.Division import Division
from src.Ast.Literals.Literal import DoubleLiteral
from src.Ast.Literals.Literal import BooleanLiteral
from src.Ast.Statement.Declaration import Declaration
from src.Ast.Statement.ExpressionStatement import ExpressionStatement
from src.Ast.Statement.Assignment import Assignment

# Asociación de operadores y precedencia
precedence = (
    #	('left','OR'),
    ('left','AND'),
    ('left', 'IGUALQUE', 'NIGUALQUE'),
    #	('nonassoc', 'MENQUE', 'MAYQUE','MAY_IG_QUE','MEN_IG_QUE'),
    ('nonassoc', 'MENQUE', 'MAYQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO','MOD'),
    ('right', 'UMENOS'),
)

def p_init(t):
    'init :	statements'
    t[0] = t[1].copy()

def p_statament_list(t):
    'statements    : statements statement'
    t[1].append(t[2])
    t[0] = t[1]

def p_statements_statement(t):
    'statements    : statement '
    t[0] = [t[1]]

def p_statement(t):
    '''statement        : stmt_assignmet
                        | stmt_declaration
                        | stmt_expr
                        | stmt_ifexpr
    '''
    t[0] = t[1]

def p_if_expression():
    'stmt_ifexpr  : IF PARIZQ expression PARDER LLAVIZQ statements LLAVDER'


def p_if_expression_outStmt():
    'stmt_ifexpr  : IF PARIZQ expression PARDER LLAVIZQ  LLAVDER'


def p_stmt_asignmet(t):
    'stmt_assignmet     : ID IGUAL expression PTCOMA'
    t[0] = Assignment(t[1],t[3])

def p_stmt_declaration(t):
    'stmt_declaration     : expression PTCOMA'
    t[0] = ExpressionStatement(t[1])

def p_stmt_expr(t):
    'stmt_expr     : tipo ID IGUAL expression PTCOMA'
    t[0] = Declaration(t[1],t[2],t[4])

def p_tipo(t):
    '''tipo     : STRING
                | DOUBLE
                | BOOLEAN
    '''
    t[0] = t[1]

#TODO: hacer las funciones nativas print y scan HOY

def p_expression(t):
    '''expression   : expression MAS 		expression
                    | expression MENOS 		expression
                    | expression POR 		expression
                    | expression DIVIDIDO 	expression
                    | expression MOD 	 	expression
    '''
    if t[2] == '+':
        pass
        t[0] = Suma(t[1], t[3],t.lineno(1),t.lexpos(1))
    elif t[2] == '-':
        pass
        t[0] = Resta(t[1], t[3],t.lineno(1),t.lexpos(1))
    elif t[2] == '*':
        pass
        t[0] = Multiplicacion(t[1], t[3],t.lineno(1),t.lexpos(1))
    elif t[2] == '/':
        pass
        t[0] = Division(t[1], t[3],t.lineno(1),t.lexpos(1))
    elif t[2] == '%':
        pass
        t[0] = Modulo(t[1], t[3],t.lineno(1),t.lexpos(1))

def p_atomic_expression(t):
    '''expression	: booleanliteral
                    | doubleliteral
    '''
    t[0]= t[1]

def p_boleanliteral(t):
    '''booleanliteral 	: TRUE
                        | FALSE
    '''
    t[0] = BooleanLiteral(t[1],t.lineno(1),t.lexpos(1))

def p_doubleliteral(t):
    '''doubleliteral 	: ENTERO
                        | DECIMAL
    '''
    t[0] = DoubleLiteral(t[1],t.lineno(1),t.lexpos(1))


def p_unity_expression(t):
    'expression : MENOS expression %prec UMENOS'
    t[0] = t[2]


#def p_mientras_instr(t):
#	'mientras_instr     : MIENTRAS PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
#	t[0] = Mientras(t[3], t[6])
#
#
#def p_if_instr(t):
#	'if_instr           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
#	t[0] = If(t[3], t[6])
#
#
#def p_if_else_instr(t):
#	'if_else_instr      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
#	t[0] = IfElse(t[3], t[6], t[10])
#
#
#def p_expresion_binaria(t):
#	'''expresion_numerica : expresion_numerica MAS expresion_numerica
#						| expresion_numerica MENOS expresion_numerica
#						| expresion_numerica POR expresion_numerica
#						| expresion_numerica DIVIDIDO expresion_numerica'''
#	if t[2] == '+':
#		t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
#	elif t[2] == '-':
#		t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
#	elif t[2] == '*':
#		t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
#	elif t[2] == '/':
#		t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
#
#
#def p_expresion_unaria(t):
#	'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
#	t[0] = ExpresionNegativo(t[2])
#
#
#def p_expresion_agrupacion(t):
#	'expresion_numerica : PARIZQ expresion_numerica PARDER'
#	t[0] = t[2]
#
#
#def p_expresion_number(t):
#	'''expresion_numerica : ENTERO
#						| DECIMAL'''
#	t[0] = ExpresionNumero(t[1])
#
#
#def p_expresion_id(t):
#	'expresion_numerica   : ID'
#	t[0] = ExpresionIdentificador(t[1])
#
#
#def p_expresion_concatenacion(t):
#	'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
#	t[0] = ExpresionConcatenar(t[1], t[3])
#
#
#def p_expresion_cadena(t):
#	'expresion_cadena     : CADENA'
#	t[0] = ExpresionDobleComilla(t[1])
#
#
#def p_expresion_cadena_numerico(t):
#	'expresion_cadena     : expresion_numerica'
#	t[0] = ExpresionCadenaNumerico(t[1])
#
#
#def p_expresion_logica(t):
#	'''expresion_logica : expresion_numerica MAYQUE expresion_numerica
#						| expresion_numerica MENQUE expresion_numerica
#						| expresion_numerica IGUALQUE expresion_numerica
#						| expresion_numerica NIGUALQUE expresion_numerica'''
#	if t[2] == '>':
#		t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
#	elif t[2] == '<':
#		t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
#	elif t[2] == '==':
#		t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
#	elif t[2] == '!=':
#		t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)


