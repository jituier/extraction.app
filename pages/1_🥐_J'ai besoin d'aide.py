import streamlit as st
from outils.extraction import ex_processus, ex_articles

def initiation():
    """
    créer des composants du site
    :return:
    """
    st.set_page_config(page_title="J'ai Bbsoin d'aide", page_icon="🥐")
    st.sidebar.image("img/image_tete.jpg")

def processus():
    h3,text = ex_processus()
    st.header("Processus d'une'demande d'aide")
    for h in h3:
        expander = st.expander(h)
        expander.markdown(text.pop(0))

if __name__ == "__main__":
    action = initiation()
    processus()
    ex_articles()
