matriz = [
    [5, 2, 9],
    [3, 7, 1],
    [8, 4, 6]
]
def bubble_sort_fila(fila):
    n = len(fila)
    for fil in range(n - 1):
        for col in range(n - fil - 1):
            if fila[col] > fila[col + 1]:
                fila[col], fila[col + 1] = fila[col + 1], fila[col]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Matriz Inicial:")
mostrar_matriz(matriz)

for fila in matriz:
    bubble_sort_fila(matriz[1])

print(f"Matriz Ordenada la fila: , {matriz[1]} ")
mostrar_matriz(matriz)