
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

# lista para guardar los tipos de parametros
list_params = []

# tabla de simbolos
symbol_table = {
	'global': {
		'vars': {

		},
		'next_int' : 1,
		'next_float' : 4000,
		'next_char' : 7000,
		'next_temp_int' : 10000,
		'next_temp_float' : 13000,
		'next_temp_char' : 16000,
		'next_temp_bool' : 19000
	}
}

# tabla de constantes
ctes_table = {
	'next_cte_int' : 43000,
	'next_cte_float' : 46000,
	'next_cte_char' : 49000,
	'next_cte_str' : 52000
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
# Global int : 1 - 3999
# Global float : 4000 - 6999
# GLOBAL char : 7000 - 9999
# Global temporales : 
# Global temp int : 10000 - 12999
# Global temp float : 13000 - 15999
# Global temp char : 16000 - 18999
# Global temp bool : 19000 - 21999

# LOCAL
# Local int : 22000 - 24999
# Local float : 25000 - 27999
# Local char : 28000 - 30999
# Local temporales : 
# Local temp int : 31000 - 33999
# Local temp float : 34000 - 36999
# Local temp char : 37000 - 39999
# Local temp bool : 40000 - 42999

# CONSTANTES
# Constantes : 
# contantes int : 43000 - 45999
# constantes float : 46000 - 48999
# constantes char : 49000 - 51999
# constantes str : 52000 - 54999



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

	# generar cuadruplo de goto a la función main

# funcion main
def p_main(p):
	'main : PRINCIPAL PARENT_A PARENT_C dec_est'

	global func_name

	# asigno el nombre de la funcion principal
	func_name = 'main'

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
		'address': assign_address(func_name, current_type)
	}


# establecer las dimensiones para vectores o matrices
def p_dimension(p):
	'dimension : CORCHETE_A CTE_I CORCHETE_C'

	global dim_size, list_vars

	dim_size = p[2]

	# guarda la constante en la tabla de constantes
	cte_exists(dim_size, 'cte_int')

	# guarda la dimension de la variable en la lista de variables
	list_vars[var_name]['dim'] = dim_size

	dim_size = 0

# declaracion de variables
def p_variable(p):
	'''variable : ID r_push_id
	| ID r_push_id dim
	'''

# regla para guardar el id en la pila de operandos
def p_r_push_id(p):
	'''r_push_id : '''
	global op_stack, type_stack
	
	var_name = p[-1]
	parent_func = ''

	# checa si la variable está definida dentro de la función
	if var_name in symbol_table[func_name]['vars']:
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
	'''variables : variable r_generate_quad_leer
	| variable r_generate_quad_leer COMA variables 
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
		'next_int' : 22000,
		'next_float' : 25000,
		'next_char' : 28000,
		'next_temp_int' : 31000,
		'next_temp_float' : 34000,
		'next_temp_char' : 37000,
		'next_temp_bool' : 40000
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

	global symbol_table, list_vars, list_params

	# guarda los parametros en la tabla de variables de la funcion
	# symbol_table[func_name]['vars'] = list_vars
	# guarda los tipos de los parámetros en la tabla de la funcion
	symbol_table[func_name]['params'] = list_params

	# list_vars = {}
	list_params = []

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

	global list_vars, list_params

	param_name = p[-1]

	#checa si el parámetro ya existe en la lista de parámetros 
	if param_name in list_vars:
		error(p, 'parámetro ya existe')

	# guarda los parametros en la lista de parametros
	list_vars[param_name] = {
			'type' : current_type,
			'address' : assign_address(func_name, current_type)
		}

	list_params.append(current_type)

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
	'asignacion : variable IGUAL r_push_oper expresion r_generate_quad_asig'

## llama a la funcion de generar cuadriplo para asignación
def p_r_generate_quad_asig(p):
	'''r_generate_quad_asig : '''
	generate_quadruple_asig(['='])

def generate_quadruple_asig(operations):
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
			# print(left_type, operator, right_type, result_type)

			# checa que el tipo del resultado sea válido
			if(result_type != None):
				# print(func_name)
				# obtiene la direccion temporal para el resultado
				result = assign_address(func_name, 'temp_' + result_type)

				# result = gen_quad(left_op, operator, right_op)

				# genera el cuadruplo
				quad = [operator, right_op, None, left_op]
				# print(quad)

				# guarda el cuadruplo en el stack
				quadruples.append(quad)
				q_count += 1
			else:
				error('Type mismatch: los tipos no coinciden')


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
	'''expresion : t_expresion r_generate_quad_or
	| t_expresion r_generate_quad_or OR r_push_oper expresion
	'''
# llama a la funcion de generar cuadriplo para el OR
def p_r_generate_quad_or(p):
	'''r_generate_quad_or : '''
	generate_quadruple(['|'])


# expresiones AND
def p_t_expresion(p):
	'''t_expresion : g_expresion r_generate_quad_and
	| g_expresion r_generate_quad_and AND r_push_oper t_expresion
	'''
# llama a la funcion de generar cuadriplo para el AND
def p_r_generate_quad_and(p):
	'''r_generate_quad_and : '''
	generate_quadruple(['&'])

# expresiones logicas
def p_g_expresion(p):
	'''g_expresion : m_expresion r_generate_quad_logicos
	| m_expresion op_logicos m_expresion r_generate_quad_logicos
	'''

# llama a la funcion de generar cuadriplo para los operadores logicos
def p_r_generate_quad_logicos(p):
	'''r_generate_quad_logicos : '''
	generate_quadruple(['>', '<', '>=', '<=', '==', '!='])

# operadores logicos
def p_op_logicos(p):
	'''op_logicos : MAYORQUE r_push_oper
	| MENORQUE r_push_oper
	| MAYORIGUAL r_push_oper
	| MENORIGUAL r_push_oper
	| IGUALIGUAL r_push_oper
	| DIFERENTE r_push_oper
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


## llama a la funcion de generar cuadriplo para mas y menos
def p_r_generate_quad_masmen(p):
	'''r_generate_quad_masmen : '''
	generate_quadruple(['+', '-'])

# llama a la funcion de generar cuadriplo para por y div
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
			# print(left_type, operator, right_type, result_type)

			# checa que el tipo del resultado sea válido
			if(result_type != None):
				# print(func_name)
				# obtiene la direccion temporal para el resultado
				result = assign_address(func_name, 'temp_' + result_type)

				# result = gen_quad(left_op, operator, right_op)

				# genera el cuadruplo
				quad = [operator, left_op, right_op, result]
				# print(quad)

				# guarda el cuadruplo en el stack
				quadruples.append(quad)
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
	''' factor : PARENT_A r_push_ff expresion PARENT_C r_pop_ff
	| CTE_I r_push_cte_i
	| CTE_F r_push_cte_f
	| CTE_CH r_push_cte_c
	| variable
	| llamada
	'''

# guarda la cte en el diccionario de ctes
# lo agrega a la pila de operandos
# y agrega su tipo a la pila de tipos
def p_r_push_cte_i(p):
	'''r_push_cte_i : '''
	global op_stack, type_stack
	
	cte = p[-1]
	cte_exists(cte, 'cte_int')

	op_stack.append(ctes_table[cte])
	type_stack.append('int')

# guarda la cte en el diccionario de ctes
# lo agrega a la pila de operandos
# y agrega su tipo a la pila de tipos
def p_r_push_cte_f(p):
	'''r_push_cte_f : '''
	global op_stack, type_stack
	
	cte = p[-1]
	cte_exists(cte, 'cte_float')

	op_stack.append(ctes_table[cte])
	type_stack.append('float')

# guarda la cte en el diccionario de ctes
# lo agrega a la pila de operandos
# y agrega su tipo a la pila de tipos
def p_r_push_cte_c(p):
	'''r_push_cte_c : '''
	global op_stack, type_stack
	
	cte = p[-1]
	cte_exists(cte, 'cte_char')

	op_stack.append(ctes_table[cte])
	type_stack.append('char')

# agrega el fondo false de la pila
def p_r_push_ff(p):
	'''r_push_ff : '''
	global oper_stack

	oper_stack.append('$')

# saca el fondo false de la pila
def p_r_pop_ff(p):
	'''r_pop_ff : '''
	global oper_stack

	oper_stack.pop()

# funcion para checar si la constante existe en la table de constantes
# si no existe la incluye en la tabla
def cte_exists(cte, cte_type):
	global ctes_table

	if cte not in ctes_table:
		ctes_table[cte] = assign_address('cte', cte_type)


# retorno de una funcion
def p_retorno(p):
	'retorno : REGRESA PARENT_A expresion PARENT_C'

# estatuto de lectura
def p_lectura(p):
	'lectura : LEER PARENT_A variables PARENT_C'

# regla para generar el cuadruplo del estatuto de lectura
def p_r_generate_quad_leer(p):
	'''r_generate_quad_leer : '''

	global op_stack, type_stack, quadruples, q_count

	var = op_stack.pop()
	type_stack.pop()
	quad = ['LEER', None, None, var]
	
	quadruples.append(quad)
	q_count += 1

# estatuto de escritura
def p_escritura(p):
	'escritura : ESCRIBIR PARENT_A escr PARENT_C'


# imprimir letrero o funcion
def p_escritura_dos(p):
	'''escritura_dos : CTE_STR r_push_cte_str
	| expresion
	'''

# guarda la cte en el diccionario de ctes
# lo agrega a la pila de operandos
# y agrega su tipo a la pila de tipos
def p_r_push_cte_str(p):
	'''r_push_cte_str : '''
	global op_stack, type_stack
	
	cte = p[-1]
	cte_exists(cte, 'cte_str')

	op_stack.append(ctes_table[cte])
	type_stack.append('str')


# genera el cuadruplo para el estatuto de escritura
def p_r_generate_quad_escr(p):
	'''r_generate_quad_escr : '''

	global op_stack, type_stack, quadruples, q_count

	if op_stack:
		op = op_stack.pop()
		type_stack.pop()

		quad = ['ESCRIBE', None, None, op]
		# print(quad)
		quadruples.append(quad)
		q_count += 1
	else:
		error(p, 'Print action is not valid')

# imprimir uno o varios letreros o expresiones
def p_escr(p):
	'''escr : escritura_dos r_generate_quad_escr
	| escritura_dos r_generate_quad_escr COMA escr
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

	global type_stack, op_stack, quadruples, q_count

	#obtiene el tipo del resultado de la expresión del if 
	exp_type = type_stack.pop()
	# si el tipo no es bool -> error
	if(exp_type != 'bool'):
		print(exp_type)
		error(p, 'Type-mismatch')
	else:
		# obtiene el resultado
		result = op_stack.pop()
		# genera el cuatruplo GotoF
		quad = ['GotoF', result, None, None]
		# print(quad)
		quadruples.append(quad)
		q_count += 1
		# guarda el contador en la pila de saltos
		jump_stack.append(q_count - 1)


def p_r_end_if(p):
	'r_end_if : '

	global jump_stack

	# obtiene el número del cuadruplo pendiente
	# de la pila de saltos
	# print(jump_stack)
	end = jump_stack.pop()
	# print('end: ', end)
	# asigna el contador al cuadruplo pendiente
	fill(end, q_count)

def p_r_goto_ifelse(p):
	'r_goto_ifelse : '

	global jump_stack, q_count, quadruples

	quad = ['Goto', None, None, None]
	# print(quad)
	quadruples.append(quad)
	q_count += 1

	# obtiene el número del cuadruplo pendiente
	# de la pila de saltos
	# print(jump_stack)
	false = jump_stack.pop()
	# guarda el contador del goto
	jump_stack.append(q_count-1)
	# asigna el contador al cuadruplo pendiente GOTOF
	# si el if es false, brinca al else
	fill(false, q_count)



def fill(val, cont):

	global quadruples
	# asigna al cuadruplo a dónde va a saltar
	# print(quadruples)
	# print('quadruplo : ', quadruples[val])
	# print('fill', val, cont)
	# print('quadruplo: ', quadruples[val-1])
	quadruples[val-1][3] = cont


# condicion else
def p_else(p):
	'else : SINO LLAVE_A estatutos_dos LLAVE_C'

# ciclo while
def p_ciclo_while(p):
	'ciclo_while : MIENTRAS r_save_jump PARENT_A expresion PARENT_C r_check_exp_type HAZ LLAVE_A estatutos_dos LLAVE_C r_goto_while'

# 
def p_r_goto_while(p):
	'''r_goto_while : '''
	global jump_stack, quadruples, q_count

	# print(jump_stack)
	end = jump_stack.pop()

	_return = jump_stack.pop()

	quad = ['GOTO', None, None, _return]
	# print(quad)

	quadruples.append(quad)
	q_count += 1

	fill(end, q_count)


# función para agregar el contador de cuadruplos a la pila de saltos
def p_save_jump(p):
	'''r_save_jump : '''

	global jump_stack

	jump_stack.append(q_count)


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
# Global int : 1 - 3999
# Global float : 4000 - 6999
# GLOBAL char : 7000 - 9999
# Global temporales : 
# Global temp int : 10000 - 12999
# Global temp float : 13000 - 15999
# Global temp char : 16000 - 18999
# Global temp bool : 19000 - 21999

# LOCAL
# Local int : 22000 - 24999
# Local float : 25000 - 27999
# Local char : 28000 - 30999
# Local temporales : 
# Local temp int : 31000 - 33999
# Local temp float : 34000 - 36999
# Local temp char : 37000 - 39999
# Local temp bool : 40000 - 42999

# CONSTANTES
# Constantes : 
# contantes int : 43000 - 45999
# constantes float : 46000 - 48999
# constantes char : 49000 - 51999

# función para asignar el valor de la dirección de memoria a una variable global, local o constante
def assign_address(func, type_value):

	global symbol_table, ctes_table

	# direcciones para la funcion principal y variables globales
	if(func == 'main' or func == 'global'):
		if(type_value == 'int'):
			# guarda la dirección
			address = symbol_table[func]['next_int']

			# valida que la dirección no sea mayor al límite
			if(address > 3999):
				error("stack overflow")

			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_int'] += 1

		elif(type_value == 'float'):
			# guarda la dirección
			address = symbol_table[func]['next_float']
			# valida que la dirección no sea mayor al límite
			if(address > 6999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_float'] += 1

		elif(type_value == 'char'):
			# guarda la dirección
			address = symbol_table[func]['next_char']
			# valida que la dirección no sea mayor al límite
			if(address > 9999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_char'] += 1

		elif(type_value == 'temp_int'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_int']

			# valida que la dirección no sea mayor al límite
			if(address > 12999):
				error("stack overflow")

			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_int'] += 1

		elif(type_value == 'temp_float'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_float']
			# valida que la dirección no sea mayor al límite
			if(address > 15999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_float'] += 1

		elif(type_value == 'temp_char'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_char']
			# valida que la dirección no sea mayor al límite
			if(address > 18999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_char'] += 1
		elif(type_value == 'temp_bool'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_bool']
			# valida que la dirección no sea mayor al límite
			if(address > 21999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_bool'] += 1
	elif(func != 'cte'):
		if(type_value == 'int'):
			# guarda la dirección
			address = symbol_table[func]['next_int']

			# valida que la dirección no sea mayor al límite
			if(address > 24999):
				error("stack overflow")

			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_int'] += 1

		elif(type_value == 'float'):
			# guarda la dirección
			address = symbol_table[func]['next_float']
			# valida que la dirección no sea mayor al límite
			if(address > 27999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_float'] += 1

		elif(type_value == 'char'):
			# guarda la dirección
			address = symbol_table[func]['next_char']
			# valida que la dirección no sea mayor al límite
			if(address > 30999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_char'] += 1

		elif(type_value == 'temp_int'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_int']

			# valida que la dirección no sea mayor al límite
			if(address > 33999):
				error("stack overflow")

			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_int'] += 1

		elif(type_value == 'temp_float'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_float']
			# valida que la dirección no sea mayor al límite
			if(address > 36999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_float'] += 1

		elif(type_value == 'temp_char'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_char']
			# valida que la dirección no sea mayor al límite
			if(address > 39999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_char'] += 1

		elif(type_value == 'temp_bool'):
			# guarda la dirección
			address = symbol_table[func]['next_temp_bool']
			# valida que la dirección no sea mayor al límite
			if(address > 42999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			symbol_table[func]['next_temp_bool'] += 1
	else:
		if(type_value == 'cte_int'):
			# guarda la dirección
			address = ctes_table['next_cte_int']

			# valida que la dirección no sea mayor al límite
			if(address > 45999):
				error("stack overflow")

			# actualiza el valor de la siguiente dirección
			ctes_table['next_cte_int'] += 1

		elif(type_value == 'cte_float'):
			# guarda la dirección
			address = ctes_table['next_cte_float']
			# valida que la dirección no sea mayor al límite
			if(address > 48999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			ctes_table['next_cte_float'] += 1

		elif(type_value == 'cte_char'):
			# guarda la dirección
			address = ctes_table['next_cte_char']
			# valida que la dirección no sea mayor al límite
			if(address > 51999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			ctes_table['next_cte_char'] += 1
		elif(type_value == 'cte_str'):
			# guarda la dirección
			address = ctes_table['next_cte_str']
			# valida que la dirección no sea mayor al límite
			if(address > 54999):
				error("stack overflow")
			# actualiza el valor de la siguiente dirección
			ctes_table['next_cte_str'] += 1


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

print('\n')
for q in quadruples:
	print(q)
	print('\n')
print('\n')
for key, val in symbol_table.items():
	print(key, ':', val)
	print('\n')

# print("---------------------- \n")
# for key, val in ctes_table.items():
# 	print(key, ':', val)
# 	print('\n')