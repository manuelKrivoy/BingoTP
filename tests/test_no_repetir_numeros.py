
def test_no_repetir_numeros():
    carton = (
        (1,2,3,4,5,6,7,8,9),
        (10,11,12,3,14,15,16,17,18),
        (19,20,21,22,23,24,25,26,27),
    )
    contador = 0
    for recc in range (0, 3):
        for recf in range(0, 9):
            for recc2 in range (recc, 3):
                for recf2 in range(recf  , 9):
                    if carton[recc][recf] != carton[recc2][recf2]:
                        contador += 1
    assert contador == 242
