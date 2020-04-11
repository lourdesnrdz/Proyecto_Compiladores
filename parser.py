
#parser

import sys
import ply.yacc as yacc

from scanner import tokens

# funcion principal del programa
def p_programa(p) :
	'''programa : PROGRAMA ID PUNTOCOMA main
	| PROGRAMA ID PUNTOCOMA d_vars funcs main
	'''

# funcion main
def p_main(p):
	'''main : PRINCIPAL PARENT_A PARENT_C LLAVE_A LLAVE_C END
	| PRINCIPAL PARENT_A PARENT_C LLAVE_A estatutos_dos LLAVE_C END 
	'''

# declaración de variables
def p_dec_vars(p):
	'''dec_vars : VAR tipo_simple ids_simple PUNTOCOMA d_vars
	| VAR tipo_complejo ids_comp PUNTOCOMA d_vars
	'''
# declarar a más variables
def p_d_vars(p):
	'''d_vars : dec_vars
	| empty
	'''

# tipos simples de variables
def p_tipo_simple(p):
	'''tipo_simple : INT
	| FLOAT
	| STRING
	| CHAR
	'''

# tipo complejo (dataframe)
def p_tipo_complejo(p):
	'tipo_complejo : DATAFRAME'

#ids con o sin dimensión 
def p_ids_simple(p):
	'''ids_simple : ID
	| ID dimension
	| ID COMA ids_simple
	| ID dimension COMA ids_simple
	'''

# ids de tipo dataframe
def p_ids_comp(p):
	'''ids_comp : ID
	| ID COMA ids_comp
	'''

# establecer las dimensiones para vectores o matrices
def p_dimension(p):
	'''dimension : CORCHETE_A CTE_I CORCHETE_C
	| CORCHETE_A CTE_I CORCHETE_C CORCHETE_A CTE_I CORCHETE_C
	'''

# declaracion de variables
def variable(p):
	'''variable : ID
	| ID dim
	'''

# establecer las dimensiones para vectores o matrices
def p_dim(p):
	'''dim : CORCHETE_A expresion CORCHETE_C
	| CORCHETE_A expresion CORCHETE_C CORCHETE_A expresion CORCHETE_C
	'''

# declaración para funciones
# tipo simple o void
def p_funcion(p):
	'''funcion: FUNCION tipo_simple func_dos
	| FUNCION VOID func_dos
	'''
# cuerpo de la funcion
def p_func_dos(p):
	'''func_dos : ID PARENT_A params PARENT_C d_vars LLAVE_A estatutos_dos LLAVE_C funcs
	'''

# declarar una funcion o no
def p_funcs(p):
	'''funcs : funcion
	| empty'''

# declaracion de parametros
def p_parametros(p):
	'''parametros : tipo_simple variable
	| tipo_simple variable COMA parametros
	'''

# declarar parametros o no 
def p_params(p):
	'''params : parametros
	| empty
	'''

# tipos de estatutos
def p_estatutos(p):
	'''estatutos : asignacion estatutos_dos
	| llamada estatutos_dos
	| retorno estatutos_dos
	| lectura estatutos_dos
	| escritura estatutos_dos
	| carga_datos estatutos_dos
	| decision estatutos_dos
	| ciclo_for estatutos_dos
	| ciclo_while estatutos_dos
	| funciones_especiales estatutos_dos
	'''

# llamar o no a estatutos
def p_estatutos_dos(p):
	'''estatutos_dos : estatutos
	| empty
	'''

# asignacion a una variable
def p_asignacion(p):
	'''asignacion : variable IGUAL expresion'''

# llamada de una funcion
def p_llamada(p):
	'''llamada : ID PARENT_A PARENT_C
	| ID PARENT_A expresiones PARENT_C
	'''

# llamar o no a expresiones
def p_expresiones(p):
	'''expresiones : expresion
	| expresion COMA expresion
	| empty
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
	| m_expresion op_logicos mexpresion
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
	| termino + m_expresion
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
	| CTE_STR
	| variable
	| llamada
	'''

# retorno de una funcion
def p_retorno(p):
	'retorno : REGRESA PARENT_A expresion PARENT_C'

# estatuto de lectura
def p_lectura(p):
	'lectura : LEER PARENT_A variables PARENT_C'


# varias variables
def p_variables(p):
	'''variables : variable
	| variabe COMA variables '''


# estatuto de escritura
def p_escritura(p):
	'escritura : ESCRIBIR PARENT_A escr PARENT_C'

# imprimir letrero o funcion
def p_escritura_dos(p):
	'''escritura_dos : LETRERO 
	| EXPRESION
	'''

# imprimir uno o varios letreros o expresiones
def p_escr(p):
	'''escr : escritura_dos
	| escritura_dos COMA escr
	'''

# estatuto de cargar archivo
def p_carga_datos(p):
	'carga_datos : CARGAARCHIVO PARENT_A ID COMA RUTA_ARCHIVO COMA CTE_I COMA CTE_I PARENT_C'

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

# funciones especiales
def p_funciones_especiales():
	'''funciones_especiales : var_archivo
	| media
	| moda
	| varianza
	| dist_normal
	| dist_poisson
	'''













def p_empty(p):
	'''empty :'''
	pass