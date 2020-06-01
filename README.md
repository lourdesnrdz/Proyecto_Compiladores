# Lenguaje Forever Alone

Forever Alone es un lenguaje procedural construido con Python en su versión 3.6.9. 

## PLY

El compilador utiliza los modulos lex.py y yacc.py de la herramienta [PLY](https://www.dabeaz.com/ply/ply.html) para el análisis del léxico y sintaxis. 

## Estructura General del Lenguaje

Un programa que utiliza el lenguaje FA debe iniciar con el nombre del programa, seguido por la declaración de variables globales, declaración de funciones y el procedimiento principal. Es obligatorio que el programa tenga el procedimiento principal.


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
El lenguaje FA maneja únicamente 3 tipos de datos simples: int, float, char.

Tipo | Descripción | Ejemplo
---- | ----------- | -------
int | Valor numérico entero positivo | 1, 2, 3, ...
float | Valores numéricos decimales positivos | 1, 2.0, 6.4, ...
char | Caracteres que representan una letra, número, etc. | 'a', 'b', 'c'

*Los operadores unarios no son soportados en el lenguaje de forma explícita en una expresión. Para utilizar valores negativos es necesario recibirlas por parte del usuario y estar almacenados en una variable*

## Variables

### Alcance
Se manejan dos tipos de alcance para las variables: Globales y Locales.

* Globales: se pueden utilizar en cualquier módulo aparte del principal.
* Locales: su uso está restringido al módulo en que han sido declaradas.

### Declaración de Variables

### Variables Dimensionadas

## Funciones
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Estatutos
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Expresiones
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Comentarios
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.