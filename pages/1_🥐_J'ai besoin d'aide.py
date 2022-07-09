import streamlit as st
from selenium.webdriver.common.by import By

from app import driver
from outils.fonctions import get_resume_all_pages
from outils.variables import *
import json
import streamlit.components.v1 as components


def initiation():
    """
    créer des composants du site
    :return:
    """
    global action

    st.set_page_config(page_title="J'ai Bbsoin d'aide", page_icon="🥐", layout="wide")
    titre = "Processus d'une demande d'aide==Evénements prochains"
    action = st.sidebar.radio("", options=titre.split("=="))
    st.sidebar.image("img/image_tete.jpg")


def _ex_processus():
    driver.get(url_processus)
    noeuds_contenu = driver.find_elements(By.XPATH,xpath_processus_noeud_contenu)
    text = []
    section_titre = []
    for n in noeuds_contenu:
        if n.tag_name == "h3":
            section_titre.append(n.text)
            text.append('')
        elif n.tag_name == "p":
            text[-1] += n.text + "\n"
        elif n.tag_name == "li":
            text[-1] += "- " + n.text + "\n"
    return text, section_titre


def processus():
    text, section_titre = _ex_processus()
    st.header("Processus d'une'demande d'aide")
    for i in range(len(section_titre)):
        expander = st.expander(section_titre[i])
        expander.markdown(text[i])
    return


def _ex_evenements():
    driver.get(url_la_une)
    placeholder = st.empty()
    bar = st.progress(0)

    # sélectionner l'option "événement"
    driver.find_element(By.XPATH, xapth_option_articles).click()
    # cliquer le button de soumettre
    driver.find_element(By.ID, "edit-submit").submit()

    ret = get_resume_all_pages()

    return ret


def evenements():
    resumes = _ex_evenements()

    # créer le json
    json_dict = {
        "title": {
            "text": {
                "headline": "Calendrier des événements prochains",
                "text": ""
            }},
        "events": []}
    for a in resumes:
        event = {}
        image_url = a[0]
        date = a[1]
        year, month, day = date.split("-")
        titre = a[2]
        article_url = a[3]
        desc = a[4]
        event["media"] = {"url": image_url}
        event["start_date"] = {"year": year, "month": month, "day": day}
        event["text"] = {"headline": f"<a href='{article_url}'>{titre}</a>", "text": desc}
        json_dict["events"].append(event)
    jsondata = json.dumps(json_dict, indent=4, separators=(',', ': '))

    # créer timeline chart avec timelinejs3
    htmlcode = """
    <link title="timeline-styles" rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>
    <div id='timeline-embed' style="width: 95%; height: 800px; margin: 1px;"></div>
    <script type="text/javascript">
        var additionalOptions = {
            start_at_end: false, is_embed:true,
        }
        var timeline_json = """ + jsondata + """;
        timeline = new TL.Timeline('timeline-embed', timeline_json, additionalOptions);
    </script>
    """

    # afficher sur le site
    components.html(htmlcode, height=800)


if __name__ == "__main__":
    initiation()
    if action == "Processus d'une demande d'aide":
        processus()
    elif action == "Evénements prochains":
        evenements()
