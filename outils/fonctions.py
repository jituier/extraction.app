import datetime

import streamlit as st
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from app import driver
from outils.variables import *


def next_page():
    try:
        next_page_element = driver.find_element(By.XPATH, f"//li[@class='{mpa_next_page_class}']")
        next_page_url = next_page_element.find_element(By.XPATH, xapth_next_page_url).get_attribute('href')
        return next_page_url
    except NoSuchElementException:
        return None


def std_date(a_date):
    """une fonction permettant de normaliser les dates pour qu'elles soient triables"""
    dico = {'JAN': 1, 'FÉV': 2, 'MAR': 3, 'AVR': 4, 'MAI': 5, 'JUIN': 6, 'JUIL': 7, 'AOÛ': 8, 'SEP': 9, 'OCT': 10,
            'NOV': 11, 'DÉC': 12}
    _ = a_date.strip().split()
    return str(datetime.datetime(int(_[2]), dico[_[1]], int(_[0])))[:10]


def _always_get_element_by_xpath(node, xpath: str):
    try:
        return node.find_element(By.XPATH, xpath)
    except:
        return ''


def _always_get_element_by_class_name(node, class_name):
    try:
        return node.find_element_by(By.CLASS_NAME, class_name)
    except:
        return ''


def _get_resume_unit():
    ret = []
    articles_liste = driver.find_elements(By.CLASS_NAME, class_article_liste)
    for node in articles_liste:

        image = _always_get_element_by_class_name(node, class_image)
        if image:
            image = image.get_attribute("src")

        date = _always_get_element_by_xpath(node, xpath_date)
        if date:
            date = date.text
            date = std_date(date)

        titre_object = _always_get_element_by_xpath(node, "div//h2/a")
        if titre_object:
            titre = titre_object.text

        url = titre_object
        if url:
            url = url.get_attribute("href")

        desc = _always_get_element_by_xpath(node, xpath_desc)
        if desc:
            desc = desc.text

        categorie = _always_get_element_by_xpath(node, xpath_categorie)
        if categorie:
            categorie = categorie.text

        ret.append((image, date, titre, url, desc, categorie))
    return ret


def get_resume_all_pages():
    """ renvoie une liste de tuples (image, date, titre, url, desc, categorie)"""
    # compter le nb de pages
    try:
        nb_page = int(driver.find_element(By.XPATH, xpath_last_page).text)
    except:
        nb_page = 1

    # initier le bar de progres
    placeholder = st.sidebar.empty()
    bar = st.sidebar.progress(0)

    page_no = 1
    ret = _get_resume_unit()
    placeholder.text(f"page 1/{nb_page}")
    bar.progress(int((page_no / nb_page) * 100))
    # changer de page
    suivant = next_page()
    while suivant:
        page_no += 1
        driver.get(suivant)
        suivant = next_page()
        ret.extend(_get_resume_unit())
        placeholder.text(f"page {page_no}/{nb_page}")
        bar.progress(int((page_no / nb_page) * 100))
    st.sidebar.markdown("recherche finie")
    return ret
