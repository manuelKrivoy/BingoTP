def test_filas_aumentan_izqader():
    carton=(
        (1,2,3,4,5,6,7,8,9),
        (10,11,12,13,14,15,16,17,18),
        (19,20,21,22,23,24,25,26,27)
    )
    contador = 0
    for i in range(0,3):
        if carton[i][0] < carton[i][1] and carton[i][2] < carton[i][3] and carton[i][3] < carton[i][4] and carton[i][4] < carton[i][5] and carton[i][5] < carton[i][6] and carton[i][6] < carton[i][7] and carton[i][7] < carton[i][8]:
            contador += 1
    assert contador == 3
