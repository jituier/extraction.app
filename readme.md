## Application d'extraction de données: aide alimentaire

Cette applicaiton est conçue pour aider les personnes ayant difficulité de se nourrir pendant la crise sanitaire de la covid19. Les données sont issues du site officiel de l'association [Banque alimentaire](https://bapif.banquealimentaire.org/).


### Organisation interne

- extraction.py : application principale
- variables : les variables globales de configuraiton
- Pipfile : la liste de dépendances à télécharger
- chromedriver.exe : piloteur utilisé dans l'application

### Environnement du développement

        pipenv --python 3.7
### Lancement de l'applicaiton
Se déplacer dans le dossier extraction.app, et lancer la commande suivante:
        
        streamlit run extraction.py
La page streamlit s'afficher au serveur `localhost:8501`.
Exemple de requête pour tester: "paris".

### Fonctionnalités de l'application
- Récupérer la requête indiquée par l'utilisateur et chercher automatiquement sur le site de la Banque alimentaire;
- Afficher le titre, la date, la catégorie et l'url des articles trouvés sous forme d'une table triable par chaque colonne;
- Générer un graphique représentant la distribution de nombre de publications par an.