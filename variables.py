
url_organisation="https://www.banquealimentaire.org/notre-organisation"
url_processus = "https://www.banquealimentaire.org/trouver-de-laide"
url_la_une = "https://www.banquealimentaire.org/les-actualites-nationales-4"

# les classes
class_accroche="field field--name-field-text-teaser field--type-string-long field--label-visually_hidden field__items"
class_article_liste="entity-list-item"
mpa_next_page_class = "pager__item pager__item--next"
class_image="image-style-list"

# xpath
xpath_accroche=f'//div[@class="{class_accroche}"]/div[@class="field__item"]'
xpath_processus_noeud_contenu='//section[@id="scrollNav-2"]//*'
xapth_option_articles='//input[@class="form-checkbox" and @value="9"]'
xapth_next_page_url="//a[@rel='next']"
xpath_date="div//div[@class='field field--name-node-post-date field--type-ds field--label-hidden field__items']"
xpath_desc="div//div[@class='field field--name-field-text-teaser field--type-string-long field--label-hidden field__items']"
xpath_categorie="div//div[@class='field field--name-field-list-job-offer-type field--type-list-string field--label-visually_hidden field__items']//div[@class='field__item']"
xpath_last_page="//li[@class='pager__item pager__item--last ']//span[@aria-hidden='true']"

# text brut
pres_du_site=        """
        La précarité alimentaire est un problème universel qui ne cesse de s'accroître 
        depuis la crise sanitaire de Covid-19. Ainsi, ce site est destiné à aider les personne en précarité alimentaire
        de trouver les aides qui pourront leur servir pendant ce temps dur.
        Il permet de faciliter la navigation du site officiel de l'association 
        **Banque alimentaire**, qui est une organisation consacrée à lutter contre la précarité alimentaire en France
        ainsi que d'autres pays. 

        Le site est composé de trois pages:
        - La page d'accueil consiste à présenter les informations concernant le site lui-même
        et les profils des bénéficiaires de l'association Banques Alimentaires.
        
        - La page "🥐J'ai besoin d'aide'" est destinée aux ceux qui sont en besoin d'aider. Elle permet de 
            - Consulter le processus à suivre pour solliciter l'aide de l'association,
            - Suivre les événements organisés par l'associaiton sur un timeline;

        - La page "🌍Je veux aider" consiste à aider ceux qui veut s'agager dans la lutte contre la précarité alimentaire
        de trouver plus facilement une offre de stage, d'emploi ou de mécénat de compétences.

        """

