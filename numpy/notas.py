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
escala = [10, 20, 100]
sobre_10 = (notas/escala) *10

nota_media_sobre10 = sobre_10.mean(axis=1)
print(f"Nota media de cada alumno sobre 10: {nota_media_sobre10.round(2)}")

# Ranking
notas_maximas = notas.max(axis=0)
notas_minimas = notas.min(axis=0)

notas_normalizadas = (notas - notas_minimas) / (notas_maximas - notas_minimas)

media_normalizada_por_alumno = notas_normalizadas.mean(axis=1)
print(f"Media de notas normalizada por alumno: {media_normalizada_por_alumno.round(2)}")

mejor_alumno = media_normalizada_por_alumno.argmax()
peor_alumno = media_normalizada_por_alumno.argmin()

print(f"Mejor alumno: {mejor_alumno}")
print(f"Peor alumno: {peor_alumno}")