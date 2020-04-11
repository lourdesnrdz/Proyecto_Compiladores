#scanner
import ply.lex as lex

# reserved key words
reserved = {
	'program' : 'PROGRAM',
	'var' : 'VAR',
	'principal' : 'PRINCIPAL',
	'end' : 'END',
	'int' : 'INT',
	'float' : 'FLOAT',
	'char' : 'CHAR',
	'string' : 'STRING',
	'void' : 'VOID',
	'dataframe' : 'DATAFRAME',
	'funcion' : 'FUNCION',
	'regresa' : 'REGRESA',
	'leer' : 'LEER',
	'escribir' : 'ESCRIBIR',
	'si' : 'SI',
	'entonces' : 'ENTONCES',
	'sino' : 'SINO',
	'mientras' : 'MIENTRAS',
	'haz' : 'haz',
	'desde' : 'DESDE',
	'hasta' : 'HASTA',
	'hacer' : 'HACER'
}

#tokens
tokens = {
	'CTE_I',
	'CTE_F',
	'CTE_CH',
	'CTE_STR',
	'COMA',
	'PUNTOCOMA',
	'DOSPUNTOS',
	'PUNTO',
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
	'DIV'
} + reserved

#Regular expressions
t_CTE_STR = r'\".*\"'
t_CORCHETEA = r'\{'
t_CORCHETEC = r'\}'
t_PARENTA = r'\('
t_PARENTC = r'\)'
t_IGUAL = r'='
t_DOSPUNTOS = r':'
t_PUNTOCOMA = r';'
t_COMA = r','
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_MAYORQUE = r'>' 
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>' 
t_MENORIGUAL = r'<'
t_DIF = r'!='
t_IGUALIGUAL = r'!='

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_ID(t):
    # r'[a-zA-Z_][a-zA-Z_0-9]*'
    r'[A-za-z]([A-za-z]|[0-9])*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a float number
def t_CTE_F(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t


# Define a variable int
def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a comment
def t_comment(t):
    r'\%%.*'
    pass

# Build the lexer
lex.lex()
