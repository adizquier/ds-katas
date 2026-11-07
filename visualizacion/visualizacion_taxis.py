import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("taxis")
colores_taxi = {"yellow": "#E0A800", "green": "#2E8B57"}

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Histograma de distancias
sns.histplot(data=df, x="distance", bins=60, ax=axes[0, 0])

axes[0, 0].set_xlim(0, 10)
axes[0, 0].set(title="La mayoría de viajes son cortos",
               xlabel="Distancia (millas)", ylabel="Número de viajes")

# Distancia frente a tarifa
sns.scatterplot(data=df, x="distance", y="fare", hue="color", palette=colores_taxi, alpha=0.4, ax=axes[0, 1])

axes[0, 1].set(title="La tarifa crece con la distancia",
               xlabel="Distancia (millas)", ylabel="Tarifa ($)")
axes[0, 1].legend(title="Color del taxi")

# Tarifa por distrito de recogida
sns.boxplot(data=df, x="pickup_borough", y="fare", ax=axes[1, 0])

axes[1, 0].set(title="Tarifa según el distrito de recogida",
               xlabel="Distrito de recogida", ylabel="Tarifa ($)")

# Método de pago por color
sns.countplot(data=df, x="payment", hue="color", palette=colores_taxi, ax=axes[1, 1])

axes[1, 1].set(title="Método de pago según el color del taxi",
               xlabel="Método de pago", ylabel="Número de viajes")
axes[1, 1].legend(title="Color del taxi")

fig.suptitle("Viajes en taxi por Nueva York", fontsize=14)
fig.tight_layout()
fig.savefig("../figuras/taxis_resumen.png", dpi=150, bbox_inches="tight")
plt.show()