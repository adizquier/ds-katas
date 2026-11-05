import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
print(type(df), "\n")

print(df.head(), "\n")
print(f"Dimensiones del dataset: {df.shape}\n")
print(f"Tipo de datos:\n{df.dtypes}\n")
print(f"Datos nulos en el dataset:\n{df.isna().sum()} \n")


# Pinguinos de Biscoe y mas de 5000g
pinguinos_filtrados = df[(df["island"] == "Biscoe") & (df["body_mass_g"] > 5000)]
print("Pinguinos de la isla Biscoe con más de 5000g de peso")
print(pinguinos_filtrados.head(), "\n")


print(f"Cantidad de pinguinos que cumplen esta condicion: {len(pinguinos_filtrados)} \n")
print(f"Especies unicas {pinguinos_filtrados["species"].unique()} \n")

#Longitud media de pico por sexo y especie
media = df.groupby(["species", "sex"])["bill_length_mm"].mean().round(1)
print(f"Longitud media de pico por especie y sexo: \n{media}\n")

# Masa media por especie ordenada
masa_media = df.groupby("species")["body_mass_g"].mean().sort_values(ascending=False)
print(f"Masa media por especie ordenada de mayor a menor: \n {masa_media}")