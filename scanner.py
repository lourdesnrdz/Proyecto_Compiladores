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
	'void' : 'VOID',
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