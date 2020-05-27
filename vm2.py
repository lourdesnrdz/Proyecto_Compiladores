import sys
import parser2 as parser

# se manda el arhivo al parser
file = sys.argv[1]
parser.build(file)

# se lee el resultado de los quadruplos, la tabla de ctes y symboltable
f2 = open('datos.txt', 'r', newline='\n')
data = eval(f2.read())
f2.close()
# print(data['ctes'])

quadruples = data['quadruples']
symbol_table = data['symbol_table']
ctes_table = data['ctes']

# int, float, char, bool
cont_vars = [0, 0, 0, 0]
# int, float, char, bool
cont_temps = [0, 0, 0, 0]

# instruction pointer
ins_p = 0

# guarda el pointer al cuadruplo 
pointer_stack = []
# guarda la memoria local de la función anterior a la llamada
local_stack = []
# guarda los temporales de la funcion
temp_stack = []

params_stack = []

cont = 0
for q in quadruples:
	print(cont, q)
	cont += 1

for key, val in symbol_table.items():
	print(key, ':', val)
	print('\n')

for key, val in ctes_table.items():
	print(key, ':', val)

class Memory():
	"""docstring for Memory"""
	def __init__(self, size_i, size_f, size_c, size_b, size_p):
		print(size_i, size_f, size_c, size_b)
		self.int_mem = [None] * size_i
		self.float_mem = [None] * size_f
		self.char_mem = [None] * size_c
		self.bool_mem = [None] * size_b
		self.point_mem = [None] * size_p


def init_Memory(func_name):
	global cont_vars, cont_temps

	cont_vars = symbol_table[func_name]['cont_vars']
	cont_temps = symbol_table[func_name]['cont_temps']

# DIRECCIONES DE MEMORIA
# GLOBAL
# Global int : 1 - 3999
# Global float : 4000 - 6999
# GLOBAL char : 7000 - 9999

# TEMPORALES : 
# temp int : 10000 - 12999
# temp float : 13000 - 15999
# temp char : 16000 - 18999
# temp bool : 19000 - 21999

# LOCAL
# Local int : 22000 - 24999
# Local float : 25000 - 27999
# Local char : 28000 - 30999
# Local temporales : 

# CONSTANTES
# CONSTANTES int : 31000 - 33999
# CONSTANTES float : 34000 - 36999
# CONSTANTES char : 37000 - 39999
# CONSTANTES str : 40000 - 42999

# POINTERS : 43000 - 45999

# obtener el valor de la dirección de memoria
def get_val(addr):
	global global_mem, temp_mem

	# Variables Globales
	# int
	if addr >= 1 and addr <= 3999:
		return int(global_mem.int_mem[addr - 1])
	# float
	if addr >= 4000 and addr <= 6999:
		return float(global_mem.int_mem[addr - 4000])
	# char
	if addr >= 7000 and addr <= 9999:
		return global_mem.int_mem[addr - 7000]
	
	# Temporales
	# int
	if addr >= 10000 and addr <= 12999:
		return int(temp_mem.int_mem[addr - 10000])
	# float
	if addr >= 13000 and addr <= 15999:
		return float(temp_mem.int_mem[addr - 13000])
	# char
	if addr >= 16000 and addr <= 18999:
		return temp_mem.int_mem[addr - 16000]
	# bool
	if addr >= 19000 and addr <= 21999:
		return bool(temp_mem.int_mem[addr - 19000])

	# Variables Locales
	# int
	if addr >= 22000 and addr <= 24999:
		# print(addr - 22000)
		# print(local_mem.int_mem)
		return int(local_mem.int_mem[addr - 22000])
	# float
	if addr >= 25000 and addr <= 27999:
		return float(local_mem.int_mem[addr - 25000])
	# char
	if addr >= 28000 and addr <= 30999:
		return local_mem.int_mem[addr - 28000]
	
	# Constantes
	# int
	if addr >= 31000 and addr <= 33999:
		return int(list(ctes_table.keys())[list(ctes_table.values()).index(addr)])
	# float
	if addr >= 34000 and addr <= 36999:
		return float(list(ctes_table.keys())[list(ctes_table.values()).index(addr)])
	# char
	if addr >= 37000 and addr <= 39999:
		return list(ctes_table.keys())[list(ctes_table.values()).index(addr)]
	# bool
	if addr >= 40000 and addr <= 42999:
		return list(ctes_table.keys())[list(ctes_table.values()).index(addr)]

	# Pointers
	if addr >= 43000 and addr <= 45999:
		# la dirección del indice es el key de la direccion
		ad = local_mem.point_mem[addr - 43000]
		correct_addr = get_val(ad)
		return correct_addr


# asignar el valor a la dirección de memoria
def assign_val(addr, result):
	global global_mem, temp_mem

	# Variables Globales
	# int
	if addr >= 1 and addr <= 3999:
		# print(addr - 1)
		# print(global_mem.int_mem)
		global_mem.int_mem[addr - 1] = result
	# float
	if addr >= 4000 and addr <= 6999:
		global_mem.int_mem[addr - 4000] = result
	# char
	if addr >= 7000 and addr <= 9999:
		global_mem.int_mem[addr - 7000] = result
	
	# Temporales 
	# int
	if addr >= 10000 and addr <= 12999:
		temp_mem.int_mem[addr - 10000] = result
	# float
	if addr >= 13000 and addr <= 15999:
		temp_mem.int_mem[addr - 13000] = result
	# char
	if addr >= 16000 and addr <= 18999:
		temp_mem.int_mem[addr - 16000] = result
	# bool
	if addr >= 19000 and addr <= 21999:
		temp_mem.int_mem[addr - 19000] = result

	# Variables Locales
	# int
	if addr >= 22000 and addr <= 24999:
		# print(result)
		# print(local_mem.int_mem[addr - 22000])
		local_mem.int_mem[addr - 22000] = result
	# float
	if addr >= 25000 and addr <= 27999:
		local_mem.int_mem[addr - 25000] = result
	# char
	if addr >= 28000 and addr <= 30999:
		local_mem.int_mem[addr - 28000] = result
	
	# Constantes
	# int
	if addr >= 31000 and addr <= 33999:
		list(ctes_table.keys())[list(ctes_table.values()).index(addr)] = result
	# float
	if addr >= 34000 and addr <= 36999:
		list(ctes_table.keys())[list(ctes_table.values()).index(addr)] = result
	# char
	if addr >= 37000 and addr <= 39999:
		list(ctes_table.keys())[list(ctes_table.values()).index(addr)] = result
	# bool
	if addr >= 40000 and addr <= 42999:
		list(ctes_table.keys())[list(ctes_table.values()).index(addr)] = result

	# Pointers
	if addr >= 43000 and addr <= 45999:
		temp_mem.point_mem[addr - 43000] = result

# acciones de los cuadruplos
def quad_actions():
	global ins_p, global_mem, global_temp_mem, temp_mem, local_mem, params_stack

	

	# obtiene el cuadruplo en la posicion del instruction pointer
	quad = quadruples[ins_p]

	if quad[0] == 'GOTO':
		print(ins_p, quad)
		ins_p = quad[3]

	if quad[0] == 'GOTOF':
		print(ins_p, quad)
		val = get_val(quad[1])
		# si es false
		if val == False:
			ins_p = quad[3]
		# si es true continua
		else:
			ins_p += 1

	if quad[0] == '+':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		res = val1 + val2
		# print(val1, val2, res)
		assign_val(quad[3], res)
		
		ins_p += 1

	if quad[0] == '-':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		res = val1 - val2
		assign_val(quad[3], res)
		
		ins_p += 1

	if quad[0] == '*':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		res = val1 * val2
		assign_val(quad[3], res)
		
		ins_p += 1

	if quad[0] == '/':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		res = val1 / val2
		assign_val(quad[3], res)
		
		ins_p += 1

	if quad[0] == '=':
		print(ins_p, quad)
		res = get_val(quad[1])
		# res = val1
		assign_val(quad[3], res)
		
		ins_p += 1

	if quad[0] == '|':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 or val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '&':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 and val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '<':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 < val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '>':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 > val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '<=':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 <= val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '>=':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 >= val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '==':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 == val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == '!=':
		print(ins_p, quad)
		val1 = get_val(quad[1])
		val2 = get_val(quad[2])
		
		if val1 != val2:
			assign_val(quad[3], 1)
		else:
			assign_val(quad[3], 0)
		
		ins_p += 1

	if quad[0] == 'LEER':
		print(ins_p, quad)
		res = input()
		assign_val(quad[3], res)

		ins_p += 1 

	if quad[0] == 'ESCRIBE':
		print(ins_p, quad)
		res = get_val(quad[3])
		print(res)

		ins_p += 1

	if quad[0] == 'REGRESA':
		print(ins_p, quad)
		# va al siguiente cuadruplo
		ins_p += 1
		quad = quadruples[ins_p]

		# asigna el valor a la variable global con el nombre de la funcion
		if quad[0] == '=':
			val1 = get_val(quad[1])
			res = val1
			assign_val(quad[3], res)
			ins_p += 1

		print(pointer_stack)

		if local_stack:
			local_mem = local_stack.pop()
		else:
			local_mem = None

		if temp_stack:
			temp_mem = temp_stack.pop()
		else:
			temp_mem = None

		print(pointer_stack)
		ins_p = pointer_stack.pop()
		ins_p += 1

	if quad[0] == 'GOSUB':
		print(ins_p, quad)
		print('gosub')
		# define el espacio de la memoria local
		local_mem = Memory(cont_vars[0], cont_vars[1], cont_vars[2], cont_vars[3], cont_vars[4])
		# define el espacio de la memoria temporal local
		temp_mem = Memory(cont_temps[0], cont_temps[1], cont_temps[2], cont_temps[3], cont_temps[4])

		print('stack: ', params_stack)
		for p in params_stack:
			assign_val(p[0], p[1])

		params_stack = []

		# guarda el apuntador al cuadrupo
		pointer_stack.append(ins_p)
		# obtiene el nombre de la función
		func_name = quad[3]
		print(func_name)
		ins_p = symbol_table[func_name]['quad_cont']

	if quad[0] == 'ERA':
		print(ins_p, quad)
		print('era')
		func_name = quad[3]
		init_Memory(func_name)
		
		if local_mem != None:
			local_stack.append(local_mem)
		if temp_mem != None:
			temp_stack.append(temp_mem)
		
		ins_p += 1

	if quad[0] == 'PARAMETER':
		print(ins_p, quad)
		# obtiene el valor a asignar
		param = get_val(quad[1])
		p = [quad[3], param]
		print('param', p)
		# se le asigna el valor a la dirección del parámetro
		# assign_val(quad[3], param)
		params_stack.append(p)

		ins_p += 1

	if quad[0] == 'ENDFunc':
		print(ins_p, quad)
		if local_stack:
			local_mem = local_stack.pop()
		else:
			local_mem = None

		if temp_stack:
			temp_mem = temp_stack.pop()
		else:
			temp_mem = None

		print(pointer_stack)
		ins_p = pointer_stack.pop()
		ins_p += 1

	if quad[0] == 'VERIFY':
		print(ins_p, quad)

		index = get_val(quad[1])

		# checa que el valor esté entre 0 y la dimensión
		if index < 0 or index >= quad[3]:
			print("Index out of bounds")
			sys.exit()
		
		# va al siguiente cuadruplo
		ins_p += 1
		

	if quad[0] == '+D':

		print(ins_p, quad)
		# obtiene la direccion base
		dirB = quad[2]
		# obtiene el valor del index
		index = get_val(quad[1])
		# suma el index a la direccion base
		# para obtener la direccion del valor al que se quiere acceder
		result = dirB + index

		# res = get_val(result)
		# print(res)
		assign_val(quad[3], result)
		ins_p += 1

	if quad[0] == 'ENDPROG':
		print(ins_p, quad)
		ins_p += 1

	# if quad[0] == '':

init_Memory('global')

# define el espacio de la memoria global
global_mem = Memory(cont_vars[0], cont_vars[1], cont_vars[2], cont_vars[3], cont_vars[4])
# define el espacio de la memoria temporal 
temp_mem = Memory(cont_temps[0], cont_temps[1], cont_temps[2], cont_temps[3], cont_temps[4])
# define el espacio de la memoria local
local_mem = None


while ins_p < len(quadruples):
	quad_actions()
print('endprog')