def carton():
    carton = (
        (0,1,0,1,1,0,1,0,0),
        (1,0,1,0,0,1,0,1,1),
        (0,1,0,1,1,0,1,1,1)
    )
    return carton


def columna(carton, nro_columna):
    return(
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna]
    )
print(columna(carton(),0))
