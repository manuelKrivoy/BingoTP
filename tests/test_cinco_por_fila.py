from src.bingo import carton

def test_cincoCeldasPorFila():
    carton =((1, 2, 3, 4 ,5, 0, 0, 0, 0),
           (1, 2, 3, 4 ,5, 0, 0, 0, 0),
           (1, 2, 3, 4 ,5, 0, 0, 0, 0)
          )
    c = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                c += 1
        assert c == 5
        c = 0
