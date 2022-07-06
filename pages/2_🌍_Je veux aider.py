import streamlit as st


def initiation():
    """
    créer des composants du site
    :return:
    """
    st.set_page_config(page_title="Je veux aider", page_icon="🌍")
    st.sidebar.image("img/image_tete.jpg")
    titre="Faire un ton==Chercher une offre de bénévolat"
    action=st.sidebar.radio("",options=titre.split("=="))


if __name__ == "__main__":
    initiation()