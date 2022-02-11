# BigData
Projet BigData dépôt de script
Tom-Pierre Brégnac, Aymeric Faure, Maxime Feuillet, Paul Lemarquand
## Vous trouverez dans ce git :

# Nos scipts pour la visualisation des données (.ipynb)
La première partie représente notre visualisation et notre choix de paramètres

# Nos scipts locaux (étapes 1/2) dans scripts locaux
Le script principal est BigData.py, le dossier contient un clé pour aws et 
nos fonctions de cryptage et décryptage fonctionnant avec le fichier key.key (généré par key.py)

# Notre modèle de ML dans scipts vm
Le script principal est clasifieur.py, il utilise data.csv (upload par BigData.py), créé dataPredict.csv et data.json (qu'il push dans mongo atlas).
Le scipt transfer mongo contient la fonction permettant la connection à mongo (présent également dans clasifieur.py). 
Le fichier cron.cron est un fichier représentant le cron écrit dans la vm aws.
