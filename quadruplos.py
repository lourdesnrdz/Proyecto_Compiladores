
# pila de operandos
op_stack = [] 
# pila de tipos
type_stack = []
# pila de operadores
oper_stack = []
#arreglo de cuadruplos
quadruples = []

# memoria

# GLOBAL -> 1 - 9999
# GLOBALES TEMPORALES -> 22000 - 25999

# int -> 1 - 2999
# float -> 3333 - 6665
# char -> 6666 - 9999


# int -> 1 - 2499
# float -> 2500 - 4999
# char -> 5000 - 7499
# bool -> 7500 - 9999


# LOCAL -> 10000 - 19999
# LOCALES TEMPORALES -> 26000 - 29999


# int -> 10000 - 12499
# float -> 12500 - 14999
# char -> 15000 - 17499
# bool -> 71500 - 19999



# CTEs -> 20000 - 21999

def get_address(func, type_value):

	if(type_value == 'int'):
		return symbol_table[func]['next_int']
	elif(type_value == 'float'):
		return symbol_table[func]['next_float']
	elif(type_value == 'char'):
		return symbol_table[func]['next_char']
