from src import bingo

mi_carton = bingo.generar_carton()

# Guarda la cantidad de celdas ocupadas
cant_celdas_ocupadas = bingo.contar_celdas_ocupadas(mi_carton)

# Verifica que la matriz sea de 3x9
def test_nueveXtres():
    assert bingo.nueveXtres(mi_carton)

#Verifica que el rango de las celdas este en valores entre 1 y 90
def test_uno_noventa():
    assert bingo.uno_noventa(mi_carton)

#Verifica que no haya numeros repetidos en el carton
def test_sin_repetir():
    assert bingo.sin_repetir(mi_carton)

#Verifica que haya 15 celdas contar_celdas_ocupadas
def test_contar_celdas_ocupadas():
    assert cant_celdas_ocupadas == 15

#Verifica que haya 5 celdas ocupadas por fila
def test_5_ocupadas_por_fila():
    assert (bingo.contar_celdas_ocupadas_en_fila(mi_carton[0]) == 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[1]) == 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[2]) == 5)

#Verifica que no haya columnas vacias
def test_columnas_no_vacias():
    assert bingo.columnas_no_vacias(mi_carton)

# Verifica que no haya filas vacias
def test_filas_no_vacias():
    assert bingo.filas_no_vacias(mi_carton)

# verifica que vayan aumentando el valor de las celdas de izquierda a derecha
def test_filas_aumentan():
    assert bingo.filas_aumentan(mi_carton)

#Verifica que descienda el valor de las columnas
def test_columnas_bajan():
    assert bingo.columnas_bajan(mi_carton)

# Verifica que no haya columnas llenas
def test_sin_colums_llenas():
    assert bingo.sin_colums_llenas(mi_carton)

# Verifica que no haya filas con 3 celdas ocupadas consecutivas
def test_celdas_ocupadas_consecutivas():
    assert bingo.celdas_ocupadas_consecutivas(mi_carton)

# Verifica que no haya filas con 3 celdas vacias consecutivas
def test_celdas_vacias_consecutivas():
    assert bingo.celdas_vacias_consecutivas(mi_carton)
