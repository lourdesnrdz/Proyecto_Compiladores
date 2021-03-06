# Lenguaje Forever Alone

Forever Alone es un lenguaje procedural construido con Python en su versión 3.6.9. 

## PLY

El compilador utiliza los modulos lex.py y yacc.py de la herramienta [PLY](https://www.dabeaz.com/ply/ply.html) para el análisis del léxico y sintaxis. 

## Ejecución

Para utilizar el compilador es necesario descargar el proyecto, el scanner.py, parser.py, semantics_cube.py y vm.py deben estar en el mismo directorio. 

Para ejecutar el compilador se debe abrir la terminar al directorio donde están los archivos anteriormente mencionados y correr el siguiente comando:

```
python3 vm.py <archivo>
```

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
float | Valores numéricos decimales positivos | 2.0, 6.4, 8.1, ...
char | Caracteres que representan una letra, número, etc. | 'a', 'b', 'c', ...

*Los operadores unarios no son soportados en el lenguaje de forma explícita en una expresión. Para utilizar valores negativos es necesario recibirlos por parte del usuario y estar almacenados en una variable*

## Variables

### Alcance
Se manejan dos tipos de alcance para las variables: **Globales** y **Locales**.

* **Globales**: se pueden utilizar en cualquier módulo aparte del principal.
* **Locales**: su uso está restringido al módulo en que han sido declaradas.

### Variables Simples y Dimensionadas
El lenguaje soporta variables simples y dimensionadas, éstas últimas únicamente pueden contener una dimensión de **tamaño N** (0 a N-1). El tamaño de la dimensión siempre debe estar definido por una constante **entera**.

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

&nbsp;&nbsp;Id *dimension* = Nombre_Módulo((*param1*, (*param2*,…);

* A un identificador se le puede asignar el resultado de una expresión en donde se invoca a una función

&nbsp;&nbsp;Id *dimension* = Nombre_Módulo(*param1*,..) + Id *dimension* – cte

```
funcion float promedio()
{
	regresa((a + c) / b);
}

principal()
{
	a = 4;
	b = 2;
	c = 6;
	
	prom = promedio();
}
```

### Llamada a una Función Void
Se manda llamar una función que no regresa valor (caso de funciones void).

&nbsp;&nbsp;*Nombre_Módulo*(*param1*,..);

```
funcion void inicia (int y)
var int x;
{
	x = 0;
	mientras (x < 10) haz
	{
		p = y * x;
		x = x+1;
	}
}

principal()
{
	inicia(5);
	escribe("p:", p);
}
```

### Retorno de una Función
Este estatuto se encuentra únicamente en las funciones con un tipo distinto a void e indica el retorno de un valor.

&nbsp;&nbsp;**regresa**(expresión);

```
funcion float promedio(int a, float b, float c)
{
	regresa((a + c) / b);
}

principal()
{
	prom = promedio(4, 2, 6);
}
```

### Lectura
Se puede leer uno ó más identificadores (con o sin dimensiones) separados por comas.

&nbsp;&nbsp;**lee** ( id *dimension* , id *dimension* ....);

```
funcion float promedio(int a, float b, float c)
{
	regresa((a + c) / b);
}

principal()
{
	lee(a);
	lee(b);
	lee(c);
	prom = promedio(a, b, c);
}
```

### Escritura
Se pueden escribir **letreros** y/ó **resultados de expresiones** separadas por comas.

&nbsp;&nbsp;**escribe** (*"letrero" ó expresión*, *"letrero" ó expresión*...);

```
principal()
{
	escribe("x = ", a + 5);
}
```

### Decisión (si... entonces ... sino)
El estatuto else es opcional, sin embargo, si se declara siempre debe seguir a un estatuto if.

&nbsp;&nbsp;**si**(expresión) **entonces**<br>
&nbsp;&nbsp;&nbsp;{ *Estatutos* }<br>
&nbsp;&nbsp;**sino**<br>
&nbsp;&nbsp;&nbsp;{ *Estatutos* }

```
si (prom > 10) entonces 
{
	escribe("promedio mayor a 10");
} 
sino {
	escribe("promedio menor a 10");
}
```

### Repetición Condicional (mientras... haz)
Se repiten los estatutos mientras la expresión sea verdadera.

&nbsp;&nbsp;**mientras**(expresión) **haz**<br>
&nbsp;&nbsp;&nbsp;{ *Estatutos* }

```
mientras (x < 10) haz
{
	x = x+1;
}
```

### Repetición No-Condicional (desde... hasta... hacer)
Se repite de **N** a **M** veces, brincando de 1 en 1.

&nbsp;&nbsp;**desde** Id *dimensiones* = exp **hasta** exp **hacer** <br>
&nbsp;&nbsp;&nbsp;{ *Estatutos* }

```
desde i = 0 hasta 9 hacer
{ 
	escribe("Escribe un número:");
	lee(Arreglo[i]);
}
```

## Expresiones
El lenguaje soporta las operaciones aritméticas, las operaciones lógicas y las operaciones relacionales.

### Operaciones Aritméticas

Operación | Token
---- | ----------- 
Suma | +
Resta | -
Multiplicación | * 
División | /

### Operaciones Lógicas

Operación | Token
---- | ----------- 
And | &
Or | |

### Operaciones Relacionales

Operación | Token
---- | ----------- 
Menor Que | <
Mayor Que | >
Menor o Igual | <=
Mayor o Igual | >=
Igual Igual | ==
Diferente | !=

## Comentarios
El lenguaje soporta el uso de comentarios, que son “ignorados” por el compilador y éstos deben seguir dos símbolos de porcentaje (**%%**). No se cuenta con la funcionalidad de comentarios multilínea.

```
%%esta es la función inicia
funcion void inicia (int y)
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