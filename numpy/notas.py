import numpy as np

# Matriz alumnos X notas
notas = np.array([
    [7.5, 14, 62],
    [4.0,  9, 45],
    [9.0, 18, 88],
    [6.0, 11, 51],
    [3.5,  8, 30],
    [8.0, 16, 74],
    [5.5, 12, 49],
    [6.5, 17, 66],
])

# Media de cada prueba
medias = notas.mean(axis=0)
for i, prueba in enumerate(medias):
    print(f"Media de la prueba {i+1}: {prueba}")


# Aprobados
notasCorte = [5, 10, 50]
aprobados = (notas >= notasCorte)

aprobadosPorPrueba = aprobados.sum(axis=0)
print(f"Numero de aprobados por prueba: {aprobadosPorPrueba}")

pruebas_aprobadas = aprobados.sum(axis=1)

aprueban_tres = (pruebas_aprobadas == 3).sum()
print(f"Alumnos que aprueban las tres => {aprueban_tres}: {np.flatnonzero(pruebas_aprobadas == 3)}")

no_aprueban_ninguna = (pruebas_aprobadas == 0).sum()
print(f"Alumnos que no aprueban ninguna => {no_aprueban_ninguna}: {np.flatnonzero(pruebas_aprobadas == 0)}")


# Sobre 10


# Ranking