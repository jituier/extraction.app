# urls
from selenium.common.exceptions import NoSuchElementException

mpa_url_banquealimentaire = "https://bapif.banquealimentaire.org/"
url_organisation="https://www.banquealimentaire.org/notre-organisation"
url_profil_beneficiaires = "https://www.banquealimentaire.org/le-profil-des-beneficiaires-de-laide-alimentaire-aux-banques-alimentaires"
url_processus = "https://www.banquealimentaire.org/trouver-de-laide"

# les classes du site MPA
class_accrche="field field--name-field-text-teaser field--type-string-long field--label-visually_hidden field__items"
mpa_search_form_id = "search-block-form--2"
mpa_search_form_classe_open = "search-block-form open"
mpa_search_submit_button_id = "edit-submit--3"
mpa_page_nav_class = "pager__items js-pager__items"
mpa_next_page_class = "pager__item pager__item--next"
mpa_result_class = "item-list"
mpa_result_list_class = "search-results node_search-results"
mpa_image_class = "image-style-search"
mpa_date_class = "date"
mpa_categorie_class = "category"
mpa_titre_class = "search-result__title"
mpa_no_result_notif = "Votre recherche n'a aucun résultat"
mpa_lire_la_suite_class = "read-more"

# xpath
xpath_accroche=f'//div[@class="{class_accrche}"]/div[@class="field__item"]'
# compteur du nombre de résultats
counter = 0