import seaborn as sns

df = sns.load_dataset("taxis")

# Inspeccion del Dataset
print(type(df), "\n")
print(f"Dimensiones del dataset {df.shape}\n")
print(df.head(), "\n")
df.info()

print(f"Tipo de datos de fechas {df["pickup"].dtype}")
print(f"Cantidad de nulos:\n{df.isna().sum()}\n")

#Pagos con tarjeta sin propina
print(df[(df["payment"] == "credit card") & (df["tip"] == 0)].head())
num_tarjeta_sin_propina = len(df[(df["payment"] == "credit card") & (df["tip"] == 0)])
print(f"Numero de pagos con tarjeta y sin propina: {num_tarjeta_sin_propina}")

# Cantidad viajes largos. 20 millas o costaron más de 60 $
num_viajes_largos = len(df[(df["distance"] > 20) | (df["fare"] > 60)])
print(f"Numero de viajes de mas de 20 millas o que costaron mas de 60 dolares: {num_viajes_largos}")

# Viajes que empiezan en Manhattan y terminan en otro distrito
viajes_Manhatthan_otro = df[(df["pickup_borough"] == "Manhattan") & (df["dropoff_borough"] != "Manhattan") & ~df["dropoff_borough"].isna()]
print(f"Numero de viajes que empiezan en Manhattan y acaban en otro sitio: {len(viajes_Manhatthan_otro)}")

print(viajes_Manhatthan_otro["dropoff_borough"].value_counts(dropna=False))