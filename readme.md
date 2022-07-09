## Application d'extraction de données: aide alimentaire

Cette applicaiton est conçue pour aider les personnes ayant difficulité de se nourrir pendant la crise sanitaire de la covid19. Les données sont issues du site officiel de l'association [Banque alimentaire](https://bapif.banquealimentaire.org/).



### Environnement du développement
        pipenv --python 3.7
Ce projet n'a pas de fichier requirements.txt car les dépendances sont déjà listées dans Pipfile.
### Lancement de l'applicaiton
Se déplacer dans le dossier extraction.app, et lancer la commande suivante:
        
        streamlit run Accueil.py
La page streamlit s'afficher au serveur `localhost:8501`.
Exemple de requête pour tester: "paris".

### Fonctionnalités mises à jour 26/juillet 
- Créer un site multipages avec streamlit 1.10.0 et une bar de navigation à gauche. Cependant cette nouvelle structure n'est pas compatible avec d'anciennes versions, ce qui conduit à l'affichage incorrect de certaines pages. Le bon affichage du site aurait du être comme suivant :
![page_accueil](img/page_accueil.png).

- la présentation du site et de la source des données
Ajouter une page pour décrire les fonctionnalités prévues de ce site. L'article de la présentation du profil de l'association a été scrappé via selenium et est présenté sur la page sous format des streamlit.Expander.

- ajouter le résumé sur le profil des bénéficiaires

- pour aider les gens cherchant de l'aide, j'ai ajouté une page décrivant le processus à suivre pour poser une demande d'aide. Les données sont également scrappées.

-Déplacement de la bare de recherche sur la bare à côté. Cela permettrait d'y accéder plus facilement et de mieux profiter des espaces. Le fonctionnement de la barre de recherche est hérité de la première version du projet déposé.  



source :

timeline_json_format : https://timeline.knightlab.com/docs/json-format.html#json-slide
timelineJS3: https://github.com/NUKnightLab/TimelineJS3
intégréer timeline avec js:https://timeline.knightlab.com/docs/instantiate-a-timeline.html