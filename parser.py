
#parser

import sys
import ply.yacc as yacc

from scanner import tokens

# variable para guardar el tipo de variables o funciones
current_type = ''
# variable que guarda el nombre de las funciones
func_name = 'global'
# variable que guarda el nombre de las variables
var_name = ''
# variable que guarda el tamaño de un vector
value_dim = 0

# diccionario para guardar las variables globales y locales
# luego se agrega a la symbol table
lista_vars = {}

# diccionario para guardar los parametros de una funcion
lista_params = {}


symbol_table = {}

# symbol_table = {
# 	'nombre' : {
# 		'tipo': 'int'
# 		'var': {
# 			'nombre': {
# 				'tipo':¨'int'
# 			}

# 		}
# 	}
# 	'global': {
# 		'var':¨{
# 			'nombre':¨{
# 				'tipo': 'int'
# 			}
# 		}
# 	}
# }

# precedencia de operadores en caso de conflicto
precedence = (
   ("right", 'IGUAL'),
   ("left", 'OR'),
   ("left", 'AND'),
   ("nonassoc", 'MENORQUE', 'MAYORQUE', 'IGUALIGUAL', 'DIFERENTE', 'MENORIGUAL', 'MAYORIGUAL'),
   ("left", 'MAS', 'MENOS'),
   ("left", 'POR', 'DIV')
)

# funcion principal del programa
def p_programa(p) :
	'programa : PROGRAMA ID PUNTOCOMA prog'
	# p[0] = "Valid"

	#guarda el nombre del programa 
	symbol_table['programa'] = p[2]

# declarar o no variables y/o funciones
def p_prog(p):
	'''prog : main
	| dec_vars dec_funciones main
	| dec_vars main
	| dec_funciones main
	'''

# funcion main
def p_main(p):
	'main : PRINCIPAL PARENT_A PARENT_C dec_est'

# # funcion main
# def p_main(p):
# 	'''main : PRINCIPAL PARENT_A PARENT_C LLAVE_A LLAVE_C
# 	| PRINCIPAL PARENT_A PARENT_C LLAVE_A estatutos_dos LLAVE_C
# 	'''

# declaración de variables
def p_dec_vars(p):
	'dec_vars : VAR create_vars_table vars'

	# global lista_vars
	# print(lista_vars)
	# lista_vars.clear()


# crear la tabla de variables globales
def p_create_vars_table(p):
	'''create_vars_table : '''
	# crea el espacio en la symbol table para las variables globales
	if(func_name == 'global'):
		symbol_table[func_name] = {
			'vars' : {

			}
		}


# guarda las variables en la lista de variables de la funcion
def p_guarda_vars(p):
	'''guarda_vars : '''

	global symbol_table, lista_vars
	# guarda las variables dentro de a funcion
	symbol_table[func_name]['vars'] = lista_vars

	lista_vars = {}


# declarar una o más variables
def p_vars(p):
	'''vars : tipo_simple ids_simple PUNTOCOMA guarda_vars
	| tipo_simple ids_simple PUNTOCOMA vars
	'''

# tipos simples de variables
def p_tipo_simple(p):
	'''tipo_simple : INT
	| FLOAT
	| CHAR
	'''

	# guarda el tipo
	global current_type
	current_type = p[1]


#ids con o sin dimensión 
def p_ids_simple(p):
	'''ids_simple : ID
	| ID dimension
	| ID COMA ids_simple
	| ID dimension COMA ids_simple
	'''
	# guarda el nombre de la variable
	global var_name, lista_vars, value_dim

	var_name = p[1]

	# guarda las variables en el diccionario de variables
	# print(var_name, ' - ', value_dim)
	lista_vars[var_name] = {
		'type' : current_type
	}

	# # si la variable tiene dimensión, se guarda el tamaño en el diccionario
	if(value_dim > 0): 
		lista_vars[var_name]['dimension'] = value_dim
		value_dim = 0

# establecer las dimensiones para vectores o matrices
def p_dimension(p):
	'dimension : CORCHETE_A CTE_I CORCHETE_C'

	# guarda el tamaño del vector (la cte_i)
	global value_dim
	value_dim = p[2]
	print(var_name, ' - ', value_dim)

# declaracion de variables
def p_variable(p):
	'''variable : ID
	| ID dim
	'''

# declarar unao varias variables
def p_variables(p):
	'''variables : variable
	| variable COMA variables 
	'''

# establecer las dimensiones para vectores o matrices
def p_dim(p):
	'''dim : CORCHETE_A expresion CORCHETE_C
	'''

# declaración para una o varias funciones
def p_dec_funciones(p):
	'''dec_funciones : funcion
	| funcion dec_funciones
	'''


# # crear la tabla de funciones
# def p_create_func_table(p):
# 	'''create_func_table : '''

# 	# crea el espacio en la symbol table para las funciones
# 	symbol_table[func_name] = {
# 		'vars' : {

# 		}
# 	}
	

# tipo simple o void para funciones
def p_funcion(p):
	'''funcion : FUNCION tipo_simple ID register_func func_dos
	| FUNCION VOID save_type_void ID register_func func_dos
	'''


def p_save_type_void(p):
	'''save_type_void : '''
	# guarda el tipo
	global current_type
	current_type = p[-1]

def p_register_func(p):
	'''register_func : '''
	global func_name
	func_name = p[-1]

	symbol_table[func_name] = {
		'tipo' : current_type,
		'vars' : {

		}
	}

# declarar o no parametros en una funcion
def p_func_dos(p):
	'''func_dos : PARENT_A PARENT_C var_funcs
	| PARENT_A parametros PARENT_C var_funcs
	'''

# declarar o no variables dentro de una funcion
def p_var_funcs(p):
	'''var_funcs : dec_est
	| dec_vars dec_est
	'''

# declaracion de parametros
def p_parametros(p):
	'''parametros : tipo_simple ID
	| tipo_simple ID COMA parametros
	'''

# # declarar parametros o no 
# def p_params(p):
# 	'''params : parametros
# 	| empty
# 	'''

# declarar o no estatutos
def p_dec_est(p):
	'''dec_est : LLAVE_A LLAVE_C
	| LLAVE_A estatutos_dos LLAVE_C
	'''

# tipos de estatutos
def p_estatutos(p):
	'''estatutos : asignacion PUNTOCOMA 
	| llamada PUNTOCOMA 
	| retorno PUNTOCOMA 
	| lectura PUNTOCOMA 
	| escritura PUNTOCOMA 
	| decision 
	| ciclo_for 
	| ciclo_while 
	'''

# llamar uno o más estatutos
def p_estatutos_dos(p):
	'''estatutos_dos : estatutos
	| estatutos estatutos_dos
	'''

# asignacion a una variable
def p_asignacion(p):
	'asignacion : variable IGUAL expresion'

# llamada de una funcion
def p_llamada(p):
	'''llamada : ID PARENT_A PARENT_C
	| ID PARENT_A expresiones PARENT_C
	'''

# llamar o no a expresiones
def p_expresiones(p):
	'''expresiones : expresion
	| expresion COMA expresion
	'''

# expresiones OR
def p_expresion(p):
	'''expresion : t_expresion
	| t_expresion OR expresion
	'''

# expresiones AND
def p_t_expresion(p):
	'''t_expresion : g_expresion
	| g_expresion AND t_expresion
	'''

# expresiones logicas
def p_g_expresion(p):
	'''g_expresion : m_expresion
	| m_expresion op_logicos m_expresion
	'''

# operadores logicos
def p_op_logicos(p):
	'''op_logicos : MAYORQUE
	| MENORQUE
	| MAYORIGUAL
	| MENORIGUAL
	| IGUALIGUAL
	| DIFERENTE
	'''

# sumas o restas
def p_m_expresion(p):
	'''m_expresion : termino
	| termino MAS m_expresion
	| termino MENOS m_expresion
	'''

# multiplicacion y division
def p_termino(p):
	'''termino : factor
	| factor POR termino
	| factor DIV termino
	'''

# factores
def p_factor(p):
	''' factor : PARENT_A expresion PARENT_C
	| CTE_I
	| CTE_F
	| CTE_CH
	| variable
	| llamada
	'''

# retorno de una funcion
def p_retorno(p):
	'retorno : REGRESA PARENT_A expresion PARENT_C'

# estatuto de lectura
def p_lectura(p):
	'lectura : LEER PARENT_A variables PARENT_C'


# estatuto de escritura
def p_escritura(p):
	'escritura : ESCRIBIR PARENT_A escr PARENT_C'


# imprimir letrero o funcion
def p_escritura_dos(p):
	'''escritura_dos : CTE_STR 
	| expresion
	'''

# imprimir uno o varios letreros o expresiones
def p_escr(p):
	'''escr : escritura_dos
	| escritura_dos COMA escr
	'''

# ESTATUTOS IF
def p_decision(p):
	'''decision : if 
	| if else'''

# condicion if
def p_if(p):
	'if : SI PARENT_A expresion PARENT_C ENTONCES LLAVE_A estatutos_dos LLAVE_C'

# condicion else
def p_else(p):
	'else : SINO LLAVE_A estatutos_dos LLAVE_C'

# ciclo while
def p_ciclo_while(p):
	'ciclo_while : MIENTRAS PARENT_A expresion PARENT_C HAZ LLAVE_A estatutos_dos LLAVE_C'

# ciclo for
def p_ciclo_for(p):
	'ciclo_for : DESDE variable IGUAL expresion HASTA expresion HACER LLAVE_A estatutos_dos LLAVE_C'

# # empty
# def p_empty(p):
# 	'''empty :'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)
    # p[0] = "Invalid"

# Build the parser
yacc.yacc()

file = sys.argv[1]
f = open(file, 'r')
data = f.read()
f.close()
yacc.parse(data)
# if yacc.parse(data) == "Valid":
# 	print("Valid input")
# else:
# 	print("Invalid input")

# print(symbol_table)
for key, val in symbol_table.items():
	print(key, ':', val)
	print('\n')

print(lista_vars)