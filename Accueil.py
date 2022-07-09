import streamlit as st
from outils.variables import *


def initiation():
    """
    créer des composants du site
    :return:
    """
    st.set_page_config(page_title="Accueil", page_icon="🏠")

    titre = "A quoi sert ce site ?==Banques alimentaires: Qui sont bénéficiés?"
    action = st.sidebar.radio("", options=titre.split("=="))
    st.sidebar.image("img/image_tete.jpg")
    return action


def pres_site():
    """Présentation du site"""
    st.title("A quoi sert ce site ?")
    st.markdown(pres_du_site)
    st.image("img/Accueil.jpg")
    return


def profil_beneficiaire():
    st.header("Le profil des bénéficiaires de l’aide alimentaire aux Banques Alimentaires")

    expander = st.expander("Situation sociale")
    expander.markdown(
        """
        L'étude 2020 réalisée par l'institut CSA permet de définir un profil sociodémographique et financier des bénéficiaires de l'aide alimentaire, de qualifier le recours à l'aide alimentaire, de connaître leur état de santé ainsi que d'évaluer l'existence et le besoin d'accompagnement social.

Près de 1000 personnes bénéficiaires ont été sélectionnées au sein d'un échantillon national représentatif de 200 associations et CCAS partenaires du réseau.

Les femmes restent très majoritaires parmi les bénéficiaires (70%). Une large majorité des bénéficiaires est de nationalité française (80%). L’âge moyen est de 48 ans (+1pt par rapport à 2018) et la grande majorité dispose d’un logement stable (86%). Les personnes isolées (37%) et les familles monoparentales (30%) restent davantage concernées par l’aide alimentaire.
        """
    )
    expander.image("img/situation_sociale.jpg")

    expander = st.expander("Situation professionnel")
    expander.markdown("""
    20% des bénéficiaires interrogés ont un emploi (+3 pts vs 2018) mais 70% travaillent à temps partiel. Il y a également une importante part de retraités (17%) et ⅓ des bénéficiaires sont des chômeurs depuis 3 ans en moyenne.
    """)
    expander.image("img/situation_professionnelle.jpg")

    expander = st.expander("Situation financière")
    expander.markdown(
        """
        L’étude nous permet de constater qu’une majorité (51%) des bénéficiaires ont recours à l’aide alimentaire depuis moins d’un an et 35% depuis moins de 6 mois. Si la perte d’emploi, la maladie et la séparation sont toujours les trois premières raisons de l’aggravation de la situation financière des bénéficiaires, l’impact de la crise sanitaire est palpable. Ainsi, **12 % des répondants disent que leurs difficultés financières se sont aggravées à la suite de la crise sanitaire du Covid-19**.

La majorité (86% +2) ont un logement stable (dont 75% de locataires et 11% de propriétaires)

       """
    )
    expander.image("img/situation_financiere.jpg")
    expander.markdown("""
    71% des bénéficiaires de l’aide alimentaire vivent en dessous du seuil de pauvreté. Le logement est de loin leur 1er poste de dépenses (77%), les factures d'eau et d'électricité (51%, +3pts vs 2018) et l'alimentation (36%, -3pts vs 2018). L’aide alimentaire leur permet d’économiser, en moyenne, 92€ par mois, somme non négligeable.
 """)
    expander.image("img/dépenses.jpg")
    expander = st.expander("Etat de santé")
    expander.markdown("""
    L’état de santé des bénéficiaires témoigne d’une fragilité des situations : 82 % (+ 11 pts vs 2018) des personnes interrogées déclarent au moins un problème de santé. Les maux de dos (39%), les problèmes de vue (34%) et les problèmes dentaires (28%) constituent les 3 principaux problèmes de santé. Viennent ensuite l’arthrose (28%), les problèmes osseux (19%) et le surpoids (19%).

53% des bénéficiaires se disent sensibilisés à l’importance d’avoir une alimentation équilibrée. Pour 73%, l'aide alimentaire leur permet d'avoir une alimentation équilibrée et 60% considèrent qu'elle leur permet d'être en meilleure santé. 
    """)
    expander.image("img/etat_sante.jpg")

    expander = st.expander("Recours à l’aide alimentaire")
    expander.markdown("""
    Les facteurs qui déclenchent le recours à l’aide alimentaire sont multiples : perte d’emploi (26%), maladie (21%), séparation ou divorce (20%), ou encore endettement (22%). 

Plus de la moitié des bénéficiaires (52 %) se rendent à l’association d’aide alimentaire au moins une fois par semaine. La demande d'aide alimentaire se concentre sur trois catégories de produits à quasi égalité : les féculents (23%), les fruits et légumes (22%) et la viande et le poisson (22%). 

Ce recours à l’aide alimentaire n’est pas à isoler d’une demande d’accompagnement revendiqué par près de 66% des bénéficiaires. """)
    expander.image("img/recours_a_l_aide.jpg")


def main():
    action = initiation()
    if action == "A quoi sert ce site ?":
        pres_site()
    else:
        profil_beneficiaire()
