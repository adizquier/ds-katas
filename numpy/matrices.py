import numpy as np

generador = np.random.default_rng(42)

matriz = generador.integers(0, 100, size=(10,10))
print(matriz)
print(f"\nDimension de la estructura {matriz.shape}")
print(f"Tipo de datos contenidos en la estructura de datos {matriz.dtype}")

for i, fila in enumerate(matriz):
    print(i, fila)

print(f"\nMedia de cada fila {matriz.mean(axis=1)}")
print(f"Media de cada columna {matriz.mean(axis=0)}")

print(f"Cantidad de numeros mayores a 90: {(matriz > 90).sum()}")

matrizCopia = matriz.copy()
matrizCopia[(matrizCopia) > 90] = 0

print(f"\n Matriz copia sin elementos mayor a 90")
for fila in matrizCopia:
    print(fila)

vMin = matrizCopia.min(axis=0)
vMax = matrizCopia.max(axis=0)

matrizNormalizada = (matrizCopia - vMin) / (vMax - vMin)

print(f"\n Matriz copia normalizada")
for fila in matrizNormalizada:
    print(fila)
