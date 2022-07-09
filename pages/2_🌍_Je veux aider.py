import streamlit as st
from app import driver
from outils.fonctions import get_resume_all_pages
import json
import streamlit.components.v1 as components


def initiation():
    """
    créer des composants du site
    :return:
    """
    global benevolat
    global stage
    global emploi
    global mecenat
    st.set_page_config(page_title="Je veux aider", page_icon="🌍", layout="wide")
    st.sidebar.image("img/image_tete.jpg")
    st.header("Les recuretements des Banques Alimentaires")

    col1, col2 = st.columns(2)
    benevolat = col1.button("BÉNÉVOLAT")
    stage = col1.button("STAGE/SERVICE CIVIQUE")
    emploi = col2.button("OFFRE D'EMPLOI")
    mecenat = col2.button("MÉCÉNAT DE COMPÉTENCES")


def ex_offre():
    placeholder = st.empty()
    placeholder.text("Récupération de données en cours, veuillez patienter...")
    driver.get("https://www.banquealimentaire.org/de-1000-missions-pres-de-chez-vous-2420?page=0")
    resume_liste = get_resume_all_pages()
    placeholder.text("")
    return resume_liste


def offre_par_cat(target: str):
    resume_liste = ex_offre()
    # créer le json
    json_dict = {
        "title": {
            "text": {
                "headline": "Calendrier offres",
                "text": target
            }},
        "events": []}
    for r in resume_liste:
        date = r[1]
        titre = r[2]
        article_url = r[3]
        categorie = r[5]
        if target == categorie:
            event = {}
            year, month, day = date.split("-")
            event["start_date"] = {"year": year, "month": month, "day": day}
            event["text"] = {"headline": f"<a href='{article_url}'>{titre}</a>"}
            json_dict["events"].append(event)
    jsondata = json.dumps(json_dict, indent=4, separators=(',', ': '))

    # créer timeline chart avec timelinejs3
    htmlcode = """
        <link title="timeline-styles" rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
        <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>
        <div id='timeline-embed' style="width: 95%; height: 400px; margin: 1px;"></div>
        <script type="text/javascript">
            var additionalOptions = {
                start_at_end: false, is_embed:true,
            }
            var timeline_json = """ + jsondata + """;
            timeline = new TL.Timeline('timeline-embed', timeline_json, additionalOptions);
        </script>
        """

    # afficher sur le site
    components.html(htmlcode, height=400)


if __name__ == "__main__":
    initiation()
    if benevolat:
        offre_par_cat("BÉNÉVOLAT")
    elif stage:
        offre_par_cat("STAGE/SERVICE CIVIQUE")
    elif emploi:
        offre_par_cat("OFFRE D'EMPLOI")
    elif mecenat:
        offre_par_cat("MÉCÉNAT DE COMPÉTENCES")
