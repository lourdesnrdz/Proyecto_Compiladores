
#parser

import sys
import ply.yacc as yacc
from scanner import tokens
from semantics_cube import semantic_cube

# variable para guardar el tipo
current_type = ''

# variable para guardar el nombre de la fucion
func_name = 'global'

# variable para guardar el nombre de una variable
var_name = ''

# varaible para guardar el tamaño del vector
dim_size = 0

# diccionario para guardar lista de variables
list_vars = {}

# diccionario para guardar lista de parametros
list_params = {}

# tabla de simbolos
symbol_table = {
	'global': {
		'vars': {

		},
		'next_int' : 1,
		'next_float' : 3000,
		'next_char' : 6000,
		'next_temp' : 9000
	}
}

# precedencia de operadores en caso de conflicto
precedence = (
   ("right", 'IGUAL'),
   ("left", 'OR'),
   ("left", 'AND'),
   ("nonassoc", 'MENORQUE', 'MAYORQUE', 'IGUALIGUAL', 'DIFERENTE', 'MENORIGUAL', 'MAYORIGUAL'),
   ("left", 'MAS', 'MENOS'),
   ("left", 'POR', 'DIV')
)

# DIRECCIONES DE MEMORIA
# GLOBAL
# Global int : 1 - 2999
# Global float : 3000 - 5999
# GLOBAL char : 6000 - 8999
# Global temporales : 9000 - 9999

# LOCAL
# Local int : 10000 - 12999
# Local float : 13000 - 15999
# Local char : 16000 - 18999
# Local temporales : 19000 - 19999

# CONSTANTES
# Constantes : 20000 - 22999


# pila de operandos
op_stack = [] 
# pila de tipos
type_stack = []
# pila de operadores
oper_stack = []
#arreglo de cuadruplos
quadruples = []
# pila de saltos
jump_stack = []
# contador que apunta al siguiente cuadruplo
q_count = 1




# funcion principal del programa
def p_programa(p) :
	'programa : PROGRAMA ID PUNTOCOMA prog'
	
	global symbol_table

	program_name = p[2]

	# guardo el nombre del programa
	symbol_table[program_name] =  {
		'type' : 'program'
	}


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

	# global func_name, symbol_table

	# func_name = 'principal'

	# symbol_table[func_name] = {
	
	# }


# # funcion main
# def p_main(p):
# 	'''main : PRINCIPAL PARENT_A PARENT_C LLAVE_A LLAVE_C
# 	| PRINCIPAL PARENT_A PARENT_C LLAVE_A estatutos_dos LLAVE_C
# 	'''

# declaración de variables
def p_dec_vars(p):
	'dec_vars : VAR vars save_vars'

# def p_create_vars_table(p):
# 	'''create_vars_table : '''
# 	global symbol_table

# 	# si se están definiento las variables globales
# 	# crea la tabla de variables globales
# 	# if(func_name == 'global'):
# 	# 	symbol_table['global'] = {
# 	# 		'vars' : {

# 	# 		}
# 	# 	}

# declarar una o más variables
def p_vars(p):
	'''vars : tipo_simple ids_simple PUNTOCOMA
	| tipo_simple ids_simple PUNTOCOMA vars
	'''

# guardar las variables en la funcion correspondiente
# sea global o una funcion
def p_save_vars(p):
	'''save_vars : '''

	global list_vars, symbol_table

	symbol_table[func_name]['vars'] = list_vars
	list_vars = {}

# tipos simples de variables
def p_tipo_simple(p):
	'''tipo_simple : INT
	| FLOAT
	| CHAR
	'''
	global current_type
	# guarda el tipo
	# en variable temporal
	current_type = p[1]

#ids con o sin dimensión 
def p_ids_simple(p):
	'''ids_simple : ID save_vars_name
	| ID save_vars_name dimension
	| ID save_vars_name COMA ids_simple
	| ID save_vars_name dimension COMA ids_simple
	'''

# funcion para guardar los nombres de las variables temporalmente
def p_save_vars_name(p):
	'''save_vars_name : '''

	global list_vars, var_name

	var_name = p[-1]

	# checar si la variable ya existe dentro de la función
	if var_name in list_vars:
		error(p, 'variable ya declarada')

	# si no existe, la agrega a la lista de variables
	list_vars[var_name] = {
		'type' : current_type,
		'address': get_address(func_name, current_type)
	}


# establecer las dimensiones para vectores o matrices
def p_dimension(p):
	'dimension : CORCHETE_A CTE_I CORCHETE_C'

	global dim_size, list_vars

	dim_size = p[2]

	# guarda la dimension de la variable en la lista de variables
	list_vars[var_name]['dim'] = dim_size

	dim_size = 0

# declaracion de variables
def p_variable(p):
	'''variable : ID r_push_id
	| ID r_push_id dim
	'''

# regla para guardar el id en la pila
def p_r_push_id(p):
	'''r_push_id : '''
	global op_stack, type_stack
	
	var_name = p[-1]
	parent_func = ''

	# checa si la variable está definida como parámetro
	if var_name in symbol_table[func_name]['params']:
		parent_func = func_name
		# op_stack.append(var_name)
		op_stack.append(symbol_table[func_name]['params'][var_name]['address'])
		type_stack.append(symbol_table[parent_func]['params'][var_name]['type'])
	# checa si la variable está definida dentro de la función
	elif var_name in symbol_table[func_name]['vars']:
		parent_func = func_name
		# op_stack.append(var_name)
		op_stack.append(symbol_table[parent_func]['vars'][var_name]['address'])
		type_stack.append(symbol_table[parent_func]['vars'][var_name]['type'])
	# checa si es una variable global
	elif var_name in symbol_table['global']['vars']:
		parent_func = 'global'
		# op_stack.append(var_name)
		op_stack.append(symbol_table[parent_func]['vars'][var_name]['address'])
		type_stack.append(symbol_table[parent_func]['vars'][var_name]['type'])
	# si la variable no existe, manda error
	else:
		error(p, 'variable no declarada')

	# op_stack.append(var_name)
	# type_stack.append(symbol_table[parent_func]['vars'][var_name]['type'])

	# aux = pila.pop()

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

# tipo simple o void para funciones
def p_funcion(p):
	'''funcion : FUNCION tipo_simple ID create_func_table func_dos
	| FUNCION VOID func_type_void ID create_func_table func_dos
	'''

def p_func_type_void(p):
	'''func_type_void : '''

	global current_type
	current_type = 'void'

# crear y guardar la funcion en la symbol table
def p_create_func_table(p):
	'''create_func_table : '''

	global func_name, symbol_table

	func_name = p[-1]

	# checa si la función ya está declarada
	# para que no haya dos funciones con el mismo nombre
	if func_name in symbol_table:
		error(p, 'funcion ya declarada')

	# sino existe, la guarda en la tabla de funciones
	symbol_table[func_name] = {
		'func_type' : current_type,
		'vars' : {

		},
		'next_int' : 10000,
		'next_float' : 13000,
		'next_char' : 16000,
		'next_temp' : 19000
	}

# declarar o no parametros en una funcion
def p_func_dos(p):
	'''func_dos : PARENT_A PARENT_C var_funcs
	| PARENT_A parametros PARENT_C save_params var_funcs
	'''
# guardar los parametros en symbol table
# dentro de la funcion correspondiente
def p_save_params(p):
	'''save_params : '''

	global symbol_table, list_params

	# guarda los parametros en la tabla de la funcion
	symbol_table[func_name]['params'] = list_params

	list_params = {}

# declarar o no variables dentro de una funcion
def p_var_funcs(p):
	'''var_funcs : dec_est
	| dec_vars dec_est
	'''

# declaracion de parametros
def p_parametros(p):
	'''parametros : tipo_simple ID save_params_list
	| tipo_simple ID save_params_list COMA parametros
	'''

# guardar los parámetros en lista temporal
def p_save_params_list(p):
	'''save_params_list : '''

	global list_params

	param_name = p[-1]

	#checa si el parámetro ya existe en la lista de parámetros 
	if param_name in list_params:
		error(p, 'parámetro ya existe')

	# guarda los parametros en la lista de parametros
	list_params[param_name] = {
			'type' : current_type,
			'address' : get_address(func_name, current_type)
		}

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
	'''m_expresion : termino r_generate_quad_masmen
	| termino r_generate_quad_masmen MAS r_push_oper m_expresion
	| termino r_generate_quad_masmen MENOS r_push_oper m_expresion
	'''

# multiplicacion y division
def p_termino(p):
	'''termino : factor r_generate_quad_muldiv
	| factor r_generate_quad_muldiv POR r_push_oper termino
	| factor r_generate_quad_muldiv DIV r_push_oper termino
	'''
def p_r_push_oper(p):
	'''r_push_oper : '''
	global oper_stack
	oper_stack.append(p[-1])


def p_r_generate_quad_masmen(p):
	'''r_generate_quad_masmen : '''
	generate_quadruple(['+', '-'])

def p_r_generate_quad_muldiv(p):
	'''r_generate_quad_muldiv : '''
	generate_quadruple(['*', '/'])


def generate_quadruple(operations):
	# ...
	global oper_stack, op_stack, type_stack, quadruples, q_count

	# print(oper_stack)
	# print(op_stack)
	if oper_stack:
		aux = oper_stack.pop()
		oper_stack.append(aux)

		if aux in operations:
			right_op = op_stack.pop()
			right_type = type_stack.pop()
			left_op = op_stack.pop()
			left_type = type_stack.pop()
			operator = oper_stack.pop()

			# obtiene el tipo del resultado del cubo semántico
			result_type = semantic_cube[left_type][operator][right_type]
			# print(result_type)

			# checa que el tipo del resultado sea válido
			if(result_type != None):
				# print(func_name)
				# obtiene la direccion temporal para el resultado
				result = get_address(func_name, 'temp')

				# result = gen_quad(left_op, operator, right_op)

				# guarda el cuadruplo en el stack
				quadruples.append([operator, left_op, right_op, result])
				q_count += 1

				# print(result)
				# guarda el resultado en el stack de operandos
				op_stack.append(result)
				# guarda el tipo del resultado
				type_stack.append(result_type)
			else:
				error('Type mismatch: los tipos no coinciden')


	# 	#...
		# quadruples.append([])

# def gen_quad(left_op, operator, right_op):
# 	if(operator == '+'):
# 		result = left_op + right_op
# 	elif(operator == '-'):
# 		result = left_op - right_op
# 	elif(operator == '*'):
# 		result = left_op * right_op
# 	elif(operator == '/'):
# 		result = left_op / right_op
# 	else:
# 		error('operación no válida')

# 	return result


# factores
def p_factor(p):
	''' factor : PARENT_A expresion PARENT_C
	| CTE_I r_push_cte_i
	| CTE_F r_push_cte_f
	| CTE_CH r_push_cte_c
	| variable
	| llamada
	'''

def p_r_push_cte_i(p):
	'''r_push_cte_i : '''
	global op_stack, type_stack
	
	cte = p[-1]

	op_stack.append(cte)
	type_stack.append('int')

def p_r_push_cte_f(p):
	'''r_push_cte_f : '''
	global op_stack, type_stack
	
	cte = p[-1]

	op_stack.append(cte)
	type_stack.append('float')

def p_r_push_cte_c(p):
	'''r_push_cte_c : '''
	global op_stack, type_stack
	
	cte = p[-1]

	op_stack.append(cte)
	type_stack.append('char')


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
	'''decision : if r_end_if 
	| if r_goto_ifelse else r_end_if'''

# condicion if
def p_if(p):
	'if : SI PARENT_A expresion PARENT_C r_check_exp_type ENTONCES LLAVE_A estatutos_dos LLAVE_C'

def p_r_check_exp_type(p):
	'r_check_exp_type : '

	global type_stack, op_stack, quadruples

	#obtiene el tipo del resultado de la expresión del if 
	exp_type = type_stack.pop()
	# si el tipo no es bool -> error
	# if(exp_type != 'bool'):
	# 	error('Type-mismatch')
	# else:
	# obtiene el resultado
	result = op_stack.pop()
	# genera el cuatruplo GotoF
	quad = ['GotoF', result, None, '']
	quadruples.append(quad)
	# guarda el contador en la pila de saltos
	jump_stack.append(q_count-1)

def p_r_end_if(p):
	'r_end_if : '

	global jump_stack

	# obtiene el número del cuadruplo pendiente
	# de la pila de saltos
	end = jump_stack.pop()
	# asigna el contador al cuadruplo pendiente
	fill(end, q_count)

def p_r_goto_ifelse(p):
	'r_goto_ifelse : '

	global jump_stack, q_count

	false = jump_stack.pop()
	jump_stack.append(q_count-1)
	fill(false, q_count)



def fill(val, cont):

	global quadruples
	# asigna al cuadruplo a dónde va a saltar
	quadruples[val][3] = cont


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
    sys.exit()

def error(p, message):
	print("Error: ", message)
	p_error(p)


# DIRECCIONES DE MEMORIA
# GLOBAL
# Global int : 1 - 2999
# Global float : 3000 - 5999
# GLOBAL char : 6000 - 8999
# Global temporales : 9000 - 9999

# LOCAL
# Local int : 10000 - 12999
# Local float : 13000 - 15999
# Local char : 16000 - 18999
# Local temporales : 19000 - 19999

# CONSTANTES
# Constantes : 20000 - 22999


# función para obtener el valor de la dirección de memoria
def get_address(func, type_value):

	global symbol_table

	if(type_value == 'int'):
		# guarda la dirección
		address = symbol_table[func]['next_int']
		# actualiza el valor de la siguiente dirección
		symbol_table[func]['next_int'] += 1
	elif(type_value == 'float'):
		# guarda la dirección
		address = symbol_table[func]['next_float']
		# actualiza el valor de la siguiente dirección
		symbol_table[func]['next_float'] += 1
	elif(type_value == 'char'):
		# guarda la dirección
		address = symbol_table[func]['next_char']
		# actualiza el valor de la siguiente dirección
		symbol_table[func]['next_char'] += 1
	elif(type_value == 'temp'):
		# guarda la dirección
		address = symbol_table[func]['next_temp']
		# actualiza el valor de la siguiente dirección
		symbol_table[func]['next_temp'] += 1
	else:
		error('.')

		# falta checar que no haya overflow

	# regresa la dirección
	return address





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
