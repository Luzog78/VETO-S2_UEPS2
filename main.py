#########################################
##            VETO-S2_UEPS2            ##
## Calculateur de dosage médicamenteux ##
#########################################

import matplotlib.pyplot as plt
import numpy as np


def random_color():
    return np.random.choice([
        'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange',
        'purple', 'brown', 'pink', 'gray', 'olive', 'skyblue', 'lime',
    ])


class Medicament:
    def __init__(self, nom: str, unite: str, dose_recommandee: float, color: str | None = None):
        self.nom = nom
        self.unite = unite
        self.dose_recommandee = dose_recommandee
        self.color = color if color is not None else random_color()


medicaments: list[Medicament] = [
    Medicament("a", "mL", 10),
    Medicament("b", "g", 0.4),
    Medicament("c", "µL", 75),
]


def prescription(nom_medicament: str, poids_animal: float):
    """
    Renvoie:
        - None si medicament non-recommendé ou non trouvé
        - Sinon la dose de médicament à préscrire (en 'unité')
    """
    for medic in medicaments:
        if medic.nom == nom_medicament:
            dose = poids_animal * medic.dose_recommandee
            return dose
    return None


def afficher_prescription(nom_medicament: str, poids_animal: float):
    for medic in medicaments:
        if medic.nom == nom_medicament:
            break
    dose = prescription(nom_medicament, poids_animal)
    if dose is None:
        print(f"Le médicament '{nom_medicament}' n'est pas reconnu ou n'est pas recommendé pour un animal de {poids_animal}kg.")
    else:
        print(f"Il faut préscrire {dose}{medic.unite} de '{medic.nom}' à un animal de {poids_animal}kg.")


fig = None
def afficher_graphique(nom_medicament: str):
    global fig, ax
    for medic in medicaments:
        if medic.nom == nom_medicament:
            print(f"Affichage du graphique de {medic.nom}.")

            plt.style.use('_mpl-gallery')

            if fig is None:
                fig, ax = plt.subplots()
                fig.set_size_inches(10, 8)
                fig.subplots_adjust(left=0.8, right=0.95, top=0.95, bottom=0.8)
                fig.canvas.mpl_connect('close_event', lambda evt: exit(0))

            x = np.linspace(0, 100, 1000)
            y = [prescription(nom_medicament, poids) for poids in x]
            y1 = [yy - 3 for yy in y]
            y2 = [yy + 3 for yy in y]

            ax.plot(x, y, linewidth=2, color=medic.color, label=f"{medic.nom} ({medic.unite})")
            ax.fill_between(x, y1, y2, color=medic.color, alpha=0.1)

            ax.set_xlabel('Poids (kg)')
            ax.set_ylabel('Dose à préscrire (voir légende)')
            ax.legend(loc='upper left')

            plt.suptitle(f"Dose à prescrire en fonction du poids de l'animal")
            plt.show(block=False)

            return
    print(f"Le médicament '{nom_medicament}' n'est pas reconnu.")


while True:
    try:
        nom = input("Nom du médicament: ")
        poids = input("Poids de l'animal (ou 'graph'): ")
        if poids == "graph":
            afficher_graphique(nom)
        else:
            try:
                poids = float(poids)
                afficher_prescription(nom, poids)
            except ValueError:
                print("Erreur sur le poids.")
        print()
    except KeyboardInterrupt:
        break

print()
