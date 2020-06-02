# Lenguaje Forever Alone

Forever Alone es un lenguaje procedural construido con Python en su versión 3.6.9. 

## PLY

El compilador utiliza los modulos lex.py y yacc.py de la herramienta [PLY](https://www.dabeaz.com/ply/ply.html) para el análisis del léxico y sintaxis. 

## Estructura General del Lenguaje

Un programa que utiliza el lenguaje FA debe iniciar con la variable reservada **programa** y el nombre del programa, seguido por la declaración de variables globales, declaración de funciones y el procedimiento principal. Es obligatorio que el programa contenga el procedimiento principal.

```
programa Nombre_prog;
<Declaración de Variables Globales>

<Declaración de Funciones>

%%Procedimiento principal
principal()
{
	<Estatutos>
}
```

## Tipos de Datos
El lenguaje FA maneja únicamente 3 tipos de datos simples: **int**, **float**, **char**.

Tipo | Descripción | Ejemplo
---- | ----------- | -------
int | Valor numérico entero positivo | 1, 2, 3, ...
float | Valores numéricos decimales positivos | 1, 2.0, 6.4, ...
char | Caracteres que representan una letra, número, etc. | 'a', 'b', 'c', ...

*Los operadores unarios no son soportados en el lenguaje de forma explícita en una expresión. Para utilizar valores negativos es necesario recibirlos por parte del usuario y estar almacenados en una variable*

## Variables

### Alcance
Se manejan dos tipos de alcance para las variables: **Globales** y **Locales**.

* **Globales**: se pueden utilizar en cualquier módulo aparte del principal.
* **Locales**: su uso está restringido al módulo en que han sido declaradas.

### Variables Simples y Dimensionadas
El lenguaje soporta variables simples y dimensionadas, éstas últimas únicamente pueden contener una dimensión de tamaño N (0 a N-1). 

```
int id1[cte_i], id2, id3;
```
*Cabe aclarar que siempre, a excepción de en la declaración, las Dimensiones son Expresiones aritméticas.*

### Declaración de Variables
La declaración de variables comienza con la variable reservada **var**, seguido por el tipo y el id. Es posible declarar varios identificadores para el mismo tipo y éstas deben ir separadas por comas.

```
var
	int var1[10], var2, var3;
	float var4;
	char var5, var6; 
```

## Funciones
La declaración de cada función comienza con la variable reservada **funcion**, seguido por el tipo de retorno, el nombre del módulo y los parámetros. Después, está la declaración de variables locales, que siguen la estructura descrita anteriormente. Las funciones declaradas con un tipo distinto a void deben contener un estatuto de retorno. 

El lenguaje también soporta las llamadas recursivas a la misma función y llamadas a otras funciones.

```
funcion void inicia(int y)
var int x;
{
	x = 0;
	mientras (x < 10) haz
	{
		p = y * x;
		x = x+1;
	}
}
```

## Parámetros
Las funciones pueden contener o no parámetros, es completamente opcional. Los parámetros únicamente reciben **variables simples**, es decir, que no se aceptan variables dimensionadas.

## Tipos de Retorno
Los tipos retorno pueden ser cualquier tipo soportado (int, float, char) o **void**.

### Funciones Void
Las funciones void no tienen estatuto de retorno. Estas funciones no pueden ser llamadas dentro de una expresión.

```
funcion void hello_world()
{
	escribe("Hello World!");
}
```

### Funciones No-Void
Estas funciones contienen tipos diferentes a void. Deben contener un estatuto de retorno que regresa un valor con el mismo tipo de la función.

```
funcion int suma(int x, int y)
{
	regresa (x + y);
}
```

## Estatutos
Los estatutos se declaran dentro de cada función.

### Asignación
A un identificador (pudiera ser simple o una casilla de un elemento dimensionado) se le asigna el valor de una expresión. 

* A un identificador, se le asigna el valor que regresa una función.

Id<dimension> = Nombre_Módulo((<param1>, (<param2>,…);

* A un identificador se le puede asignar el resultado de una expresión en donde se invoca a una función

Id<dimension> = Nombre_Módulo(<param1>,..) + Id<dimension> – cte

### Llamada a una Función Void

### Retorno de una Función

### Lectura

### Escritura

### Decisión (si... entonces ... sino)

### Repetición Condicional (mientras... haz)

### Repetición No-Condicional (desde... hasta... hacer)

## Expresiones
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Comentarios
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.