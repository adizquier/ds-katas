import numpy as np

# Datos dados. Las filas son los dias de la semana y las columnas las horas
rng = np.random.default_rng(1)
perfil = np.array([0.30, 0.25, 0.20, 0.20, 0.20, 0.25, 0.40, 0.80, 0.90, 0.60, 0.50, 0.50,
                   0.60, 0.90, 1.00, 0.70, 0.60, 0.70, 1.10, 1.40, 1.60, 1.30, 0.90, 0.50])
consumo = (perfil + rng.normal(0, 0.15, size=(7, 24))).clip(0.05).round(2)

# Consumo total de cada dia y de toda la semana

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

consumo_total_por_dia = consumo.sum(axis=1)
consumo_total = consumo_total_por_dia.sum()

print("Consumo total por dia:")
for dia, consumo_dia in zip(dias_semana, consumo_total_por_dia):
    print(f"{dia}: {consumo_dia:.2f}")

print(f"\nConsumo total de la semana: {consumo_total:.2f}\n")

# Consumo medio por hora

consumo_por_hora = consumo.mean(axis=0)
hora_maxima = consumo_por_hora.argmax()
hora_minima = consumo_por_hora.argmin()

print(f"Hora de mayor consumo: {hora_maxima} con consumo medio de {consumo_por_hora[hora_maxima]:.2f}")
print(f"Hora de menor consumo: {hora_minima} con consumo medio de {consumo_por_hora[hora_minima]:.2f}\n")

# Horas de la semana que superan 1.2 kWh

por_encima = consumo > 1.2
horas_por_encima = por_encima.sum()
print(f"Numero de horas en total que superan 1.2 kWh: {horas_por_encima}")

dias_por_encima = por_encima.sum(axis=1)

print("Numero de horas por dia que superan los 1.2 kWh:")
for dia, cantidad in zip(dias_semana, dias_por_encima):
    print(f"{dia}: {cantidad}")
print()

# Vector precio. Valle, llano y punta

vector_consumo = np.full(24, 0.08)
vector_consumo[8:23] = 0.15
vector_consumo[10:14] = 0.25
vector_consumo[18:22] = 0.25

coste_semanal = vector_consumo * consumo

coste_por_dia = coste_semanal.sum(axis=1)
for dia, coste in zip(dias_semana, coste_por_dia):
    print(f"{dia}: {coste:.2f}")

coste_total = coste_por_dia.sum()
print(f"\nCoste total: {coste_total:.2f}")