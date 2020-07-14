
[![Build Status](https://travis-ci.com/manuelKrivoy/BingoTP.svg?branch=master)](https://travis-ci.com/manuelKrivoy/BingoTP) [![Coverage Status](https://coveralls.io/repos/github/manuelKrivoy/BingoTP/badge.svg?branch=master)](https://coveralls.io/github/manuelKrivoy/BingoTP?branch=master)

# TP Bingo

Este es un proyecto hecho para la materia AAT en 2020. El objetivo es que se generen cartones para jugar al bingo que cumplan con diversas reglas. Tenemos la opción de generar una salida en python(consola) y otra en html (Versión WEB)

## Reglas

* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.
* Los números del carton se encuentran en el rango 1 a 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton es una matrix de 3 x 9.
* Cada carton tiene 15 celdas ocupadas.
* Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.

# Cómo generar nuestros cartones aleatorios:

## Clonar repositorio

Para poder utilizar este repositorio y así generar cartones de bingo lo primero que debemos hacer es clonar este repositorio en tu computadora.

Para clonar:

```
git clone https://github.com/manuelKrivoy/BingoTP.git
```

## Uso de código

Tenemos `dos posibles salidas` , la primera es en la `consola` , para esta debemos usar el siguiente comando:

### Salida por consola en python

```
python src/bingo.py
```

### Ejemplo salida por consola
```
python src/bingo.py
[0, 11, 27, 0, 0, 51, 0, 71, 80]
[2, 0, 28, 0, 0, 56, 69, 0, 81]
[7, 18, 0, 33, 44, 0, 0, 78, 0]

```

### Salida web por HTML

```
python src/WebBingo.py
```
