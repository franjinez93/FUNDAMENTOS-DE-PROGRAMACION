matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

buscar_valor = 8

for fila in range (len(matriz)):
    for columna in range (len(matriz[fila])):
     if matriz[fila][columna] == buscar_valor:
        print(f"se encontro en la posicion {fila} , {columna}")
        break
    else:
        continue
    break
else:
    print("valor no encontrado")