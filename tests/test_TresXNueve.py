from src.bingo import carton, columna

def test_nueveXtres():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for columna in mi_carton:
            contador = contador + 1

    assert len(mi_carton) == 3 and contador == 9
