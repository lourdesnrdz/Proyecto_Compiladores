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
}