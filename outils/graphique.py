import matplotlib.pyplot as plt

# situation sociale
## plot 1: Hommes/Femmes
plt.subplot(2, 2, 1)
plt.pie([70, 30], autopct='%d%%')
plt.legend(labels=['femme', 'homme'])
plt.title("Ratio homme/femme")
## plot 2: française
plt.subplot(2, 2, 2)
plt.pie([80, 20], autopct='%d%%')
plt.legend(labels=['fraçaise', 'autres'])
plt.title("Nationalité")
## plot 3: famille
plt.subplot(2, 2, 3)
plt.pie([37, 30, 33], autopct='%d%%')
plt.legend(labels=['personnes isolées', 'famille monoparentales', 'autres'])
plt.title("situation familiale")

plt.savefig("../img/situation_sociale.jpg")
plt.close()

# situation professionnelle
plt.pie([14, 6, 17, 33, 30], labels=['travail à temps partiel', 'en emploi', 'retraité', 'chomâge', 'autres'],
        autopct='%d%%')
plt.title("situation professionnelle")
plt.savefig("../img/situation_professionnelle.jpg")
plt.close()

# situation financière
## plot 1: avoir recours à l'aide
plt.subplot(1, 2, 1)
plt.pie([70, 30], autopct='%d%%')
plt.title("avoir recours à l'aide")
plt.legend(labels=['depuis au moins d\'un an', 'depuis six mois'], loc=1)

## plot 2: logement
plt.subplot(1, 2, 2)
plt.pie([75, 11, 14], autopct='%d%%')
plt.legend(labels=['propriétaire', 'locataire', 'sans logement stable'], loc=1)
plt.title("logement stable")

plt.savefig("../img/situation_financiere.jpg")
plt.close()

## plot 3: dépenses
plt.bar(['logement', 'électricités & eau', 'alimentation'], [0.77, 0.51, 0.36])
plt.title("Dépenses")

plt.savefig("../img/dépenses.jpg")
plt.close()

# Etat de santé
params = {
    'figure.figsize': '15, 4'
}
plt.rcParams.update(params)
plt.bar(['maux de dos', 'problèmes de vue', 'problèmes dentaires', 'arthrose', 'problèmes osseux', 'surpoids'],
        [0.39, 0.34, 0.28, 0.28, 0.19, 0.19])
plt.title("Etat de santé")

plt.savefig("../img/etat_sante.jpg")
plt.close()

# recours
params = {
    'figure.figsize': '8, 4'
}
plt.rcParams.update(params)
## plot 1: raison du recours
plt.subplot(1, 2, 1)
plt.pie([26, 21, 20, 22], autopct='%d%%')
plt.title("Raison du recours à l'aide alimentaire")
plt.legend(labels=['perte d\'emploi', 'maladie', 'divorce', 'endettement'])
plt.subplot(1, 2, 2)
## plot 2: type de produits demandés
plt.pie([23, 22, 22], autopct='%d%%')
plt.title("type de produits demandés")
plt.legend(labels=['féculents', 'fruits et légumes', 'viande et poisson'])

plt.savefig("../img/recours_a_l_aide.jpg")
plt.close()
