import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")

fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data = df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)

ax.set_title("Longitud de la aleta frente a masa")
ax.set_xlabel("Longitud de la aleta (mm)")
ax.set_ylabel("Masa corporal (g)")
ax.legend(title = "Especie")

fig.savefig("../figuras/pinguins.png", dpi=150, bbox_inches="tight")

plt.show()