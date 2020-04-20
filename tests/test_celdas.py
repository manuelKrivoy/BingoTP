from src.bingo import carton, columna

#Funcion que verifica que no haya mas ni menos de 15 celdas ocupadas en un carton.
def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador==15

#Funcion que verifica que haya al menos una celda ocupada por columna.
def test_al_menos_una_celda_por_columna():
    mi_carton = carton()
    contador_columnas = 0
    check = 0
    for contador_columnas in range(9):
        mi_columna = columna(mi_carton,contador_columnas)
        if sum(mi_columna) >= 1:
            check= check + 1

    assert check == 9

#Funcion que verifica que cada fila tenga al menos una celda ocupada.
def test_filas_no_vacias():
    mi_carton = carton()
    contador = 0
    filas = 0
    columnas = 0
    check = 0
    for columnas in range(3):
        for filas in range(9):
            contador += mi_carton[columnas][filas]
            filas += 1
        if contador >= 1:
            check += 1
        contador = 0
        filas = 0
        columnas += 1

    assert check == 3
