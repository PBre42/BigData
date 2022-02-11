## Projet Big Data Script final
# Tom-Pierre Brégnac - Maxime Feuillet - Paul Lemarquand - Aymeric Faure
# Ce script contient toutes les étapes à effectuer

import os
import time
import encryption as Encrypt
import json
import pymongo
import pandas as pd


# Etape 0
#
#
#

# Etape 1
# On récupère le fichier csv en local
os.system('hadoop fs -get /tmp/data/data.csv data.csv')

# Encryptage symétrique des données
# Possible mais non utilisé car ssh suffisant
Encrypt.encrypt('data.csv')

# Création de la VM AWS ?


# Connection en SSH à une VM AWS Linux
# Upload du fichier 
os.system('scp -i bigdatakey.pem data.csv ec2-user@ec2-3-84-36-53.compute-1.amazonaws.com:~')

# Les données sont traitées par le modèle d'apprentissage dans la VM
# Un cron déclenche le script à la mise à jour du fichier et pousse les données dans Mongo
