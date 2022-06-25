import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import Counter

# importer variable globale
from variables import *



# chargement du driver de Chrome
driver = webdriver.Chrome()
# chargement de la page html du marmiton
driver.get(mpa_url_banquealimentaire)


def main():
    # création de l'interface initiale
    st.sidebar.image("https://www.marciatack.fr/wp-content/uploads/2015/06/lutte-contre-la-faim1.jpg")
    st.sidebar.title("Aide alimentaire")
    asso = st.sidebar.selectbox("Choisir l'association qui vous intéresse: ", ["Banque alimentaire", "Action contre la faim"])
    requete = st.text_input("Entrez votre requête: ")

    # procéder la requête

    # barre de progrès
    placeholder = st.empty()
    bar = st.progress(0)

    if requete:
        if asso == "Banque alimentaire":
            request(requete)
            df = get_results(placeholder, bar)
            if df is not None:
                # aller à la page suivante s'il elle existe et continue de parcourir
                suivante = next_page()
                while suivante:
                    driver.get(suivante)
                    df = pd.concat([df, get_results(placeholder, bar)])
                    suivante = next_page()
                df.set_index(["id"], inplace=True)
                st.success("Résultats trouvés: ")
                st.dataframe(df)
                graphique(list(df["date"]))
                bar.progress(100)

            else:
                # message d'une recherchce sans résultats pertinentsmessage d'une recherchce sans résultats pertinents
                st.warning("Désolée, aucun résultat pertinent a été trouvé.")
        else:
            st.warning("Le site choisi n'est pas encore supporté. Merci de choisir l'autre. ")


def request(requete: str):
    # faire afficher la barre de recherche
    js = f"document.getElementById('{mpa_search_form_id}').setAttribute('class','{mpa_search_form_classe_open}')"
    driver.execute_script(js)
    # renseigner la requête
    search_block = driver.find_element_by_id(mpa_search_form_id)
    input_area = search_block.find_element_by_xpath("//input")
    input_area.send_keys(requete)
    # envoyer
    submit_button = search_block.find_element_by_id(mpa_search_submit_button_id)
    submit_button.click()


def next_page():
    try:
        # page_nav_bar = driver.find_element_by_xpath(f"//nav/ul[@class='{mpa_page_nav_class}']")
        next_page_element = driver.find_element_by_xpath(f"//li[@class='{mpa_next_page_class}']")
        next_page_url = next_page_element.find_element_by_xpath("//a[@rel='next']").get_attribute('href')
        return next_page_url
    except NoSuchElementException:
        return None


def get_results(placeholder, bar):
    """
    :return: informations des résultats sous format de pd.DataFrame
    """
    ret = []
    global counter
    # récupérer la liste des items
    result_block = driver.find_element_by_xpath(f"//div[@class='{mpa_result_class}']")

    # recherchce sans résultats pertinents
    if result_block.text.startswith(mpa_no_result_notif):
        return None

    # récupérer touts les noeuds <li> de la liste des items
    result_list = result_block.find_elements_by_xpath(f"//ol[@class='{mpa_result_list_class}']//li")

    # construire les données à mettre dans DataFrame
    data = []
    for node in result_list:
        counter += 1
        placeholder.text(f"{counter} results récupérés")
        bar.progress(counter)
        # image_url = node.find_element_by_xpath(f"div//img[@class='{mpa_image_class}']").get_attribute("src")
        result_title = node.find_element_by_xpath(f"div//h3[@class='{mpa_titre_class}']").text
        date = std_date(node.find_element_by_xpath(f"div//time[@class='{mpa_date_class}']").text)
        try:
            categorie = node.find_element_by_xpath(f"div//p[@class='{mpa_categorie_class}']").text
        except:
            categorie = "Catégorie inconnue"
        articile_url = node.find_element_by_xpath(f"div//p[@class='{mpa_lire_la_suite_class}']/a").get_attribute("href")

        data.append([counter, result_title, date, categorie, articile_url])
    df = pd.DataFrame(data, columns=['id', 'titre', 'date', 'catégorie', 'url'])
    return df


def graphique(liste_dates: list):
    """générer le graphique"""
    cnt = Counter()
    for i in range(len(liste_dates)):
        # liste_dates[i]=liste_dates[i][:4]
        cnt[liste_dates[i][:4]] += 1
    char_data=pd.DataFrame(dict(cnt),index=["nombre_pub"]).T
    st.line_chart(char_data)


def std_date(a_date):
    """une fonction permettant de normaliser les dates pour qu'elles soient triables"""
    dico = {'JAN': 1, 'FÉV': 2, 'MAR': 3, 'AVR': 4, 'MAI': 5, 'JUIN': 6, 'JUIL': 7, 'AOÛ': 8, 'SEP': 9, 'OCT': 10,
            'NOV': 11, 'DÉC': 12}
    _ = a_date.split()
    return str(datetime.datetime(int(_[2]), dico[_[1]], int(_[0])))[:10]


if __name__ == '__main__':
    main()
