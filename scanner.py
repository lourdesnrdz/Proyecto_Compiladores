#scanner
import ply.lex as lex
import math

# reserved key words
reserved = {
	'programa' : 'PROGRAMA',
	'var' : 'VAR',
	'principal' : 'PRINCIPAL',
	'int' : 'INT',
	'float' : 'FLOAT',
	'char' : 'CHAR',
	'void' : 'VOID',
	'funcion' : 'FUNCION',
	'regresa' : 'REGRESA',
	'lee' : 'LEER',
	'escribe' : 'ESCRIBIR',
	'si' : 'SI',
	'entonces' : 'ENTONCES',
	'sino' : 'SINO',
	'mientras' : 'MIENTRAS',
	'haz' : 'HAZ',
	'desde' : 'DESDE',
	'hasta' : 'HASTA',
	'hacer' : 'HACER',
}

#tokens
tokens = [
	'PROGRAMA',
	'VAR',
	'PRINCIPAL',
	'INT',
	'FLOAT',
	'CHAR',
	'VOID',
	'FUNCION',
	'REGRESA',
	'LEER',
	'ESCRIBIR',
	'SI',
	'ENTONCES',
	'SINO',
	'MIENTRAS',
	'HAZ',
	'DESDE',
	'HASTA',
	'HACER',
	'ID',
	'CTE_I',
	'CTE_F',
	'CTE_CH',
	'CTE_STR',
	'COMA',
	'PUNTOCOMA',
	'PARENT_A',
	'PARENT_C',
	'CORCHETE_A',
	'CORCHETE_C',
	'LLAVE_A',
	'LLAVE_C',
	'IGUAL',
	'OR',
	'AND',
	'MAYORQUE',
	'MENORQUE',
	'MAYORIGUAL',
	'MENORIGUAL',
	'IGUALIGUAL',
	'DIFERENTE',
	'MAS',
	'MENOS',
	'POR',
	'DIV',
]

#Regular expressions
# t_CTE_STR = r'\".*\"'
# t_CTE_CH = r'\'.\''
t_COMA = r','
t_PUNTOCOMA = r';'
# t_DOSPUNTOS = r':'
# t_PUNTO = r'.'
t_PARENT_A = r'\('
t_PARENT_C = r'\)'
t_CORCHETE_A  = r'\['
t_CORCHETE_C  = r'\]'
t_LLAVE_A = r'\{'
t_LLAVE_C = r'\}'
t_IGUAL = r'='
t_MAYORQUE = r'>' 
t_MENORQUE = r'<'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # r'[A-za-z]([A-za-z]|[0-9])*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTE_STR(t):                                        
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_CTE_CH(t):                                        
    r'\'.\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_CTE_F(t):
	r'([0-9]*[.])?[0-9]+'
	# si el numero ya es un entero
	# se regresa el mismo numero entero
	if int(math.floor(float(t.value))) == float(t.value):
	# t.value = int(t.value)
	# t.type = 'CTE_I'
		try:
			t.value = int(t.value)
			t.type = 'CTE_I'
		except ValueError:
			# value error: si el valor termina 
			#con .0 marca este error
			#Ej. 2.0
			# Entonces es float
			t.value = float(t.value)
	else:
		t.value = float(t.value)
	return t


# OR
def t_OR(t):
    r'\|'
    return t

# AND
def t_AND(t):
    r'\&'
    return t

# MENORIGUAL
def t_MENORIGUAL(t):
    r'<='
    return t

# MAYORIGUAL
def t_MAYORIGUAL(t):
    r'>='
    return t

# IGUALIGUAL
def t_IGUALIGUAL(t):
    r'=='
    return t

# DIFERENTE
def t_DIFERENTE(t):
    r'!='
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a comment
def t_comment(t):
    r'\%\%.*'
    pass

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    print("Lexical error ' {0} ' found in line ' {1} ' ".format(t.value[0], t.lineno))
    t.lexer.skip(1)

# Build the lexer
lex.lex()

# # Test it out
# data = '''
# programa foreveralone; 
# var
# 	int i, j, p;
# 	int Arreglo[10], OtroArreglo[10];
# 	float valor; 

# funcion int fact (int j)
# var int i;
# {
# 	i = j + (p - j * 2 + j);
# 	si (j == 1) entonces 
# 	{ regresa (j);}
# 	sino
# 	{regresa (j * fact(j - 1));}
# }

# funcion void inicia (int y)
# var int x;
# {
# 	x = 0;
# 	mientras (x < 11) haz
# 	{
# 	Arreglo[x] = y * x;
# 	x = x+1;
# 	}
# }

# principal()
# {
# 	lee(p); j = p * 2;
# 	inicia (p * j - 5);
# 	desde i = 0 hasta 9 hacer
# 		{ 
# 		Arreglo[i] = Arreglo[i] * fact(Arreglo[i] - p);
# 		}
# 	desde i = 0 hasta 9 hacer
# 		{ 
# 		OtroArreglo[i] = Arreglo[i] - p;
# 		}
# 	mientras (i < 10) haz
# 	{ 
# 		escribe("Otros datos", OtroArreglo[i], p, i + OtroArreglo[i]);
# 		i = i + 1;
# 	}
# }


# '''

# # Give the lexer some input
# lex.input(data)

# # Tokenize
# while 1:
#     tok = lex.token()
#     if not tok: 
#     	break      # No more input
#     print(tok)

# def buildlexer(file):
# 	lex.input(data)
# 	# Tokenize
# 	while 1:
# 	    tok = lex.token()
# 	    if not tok: 
# 	    	break      # No more input
# 	    print(tok)