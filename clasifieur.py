file = "data.csv"
# make a prediction with a ridge regression model on the dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from numpy import mean, median
from pandas import read_csv
from pandas import concat
import pandas as pd
import warnings
import pymongo
import json
import csv

warnings.filterwarnings("ignore")

# Lecture du fichier csv
df = pd.read_csv("33000-BORDEAUX_nettoye.csv")
# Création du set de test (80/20)
trainset = df.sample(frac=0.80)
# Paramètres choisis après visualisation des données 
X_train=trainset[["Capacite_accueil","NbChambres","frais_menage","Latitude","Longitude","Caution"]]
y_train=trainset[["PrixNuitee"]]
df2 = concat([df, trainset])
# On enlève les doublons
testset=df2.drop_duplicates(keep=False)
X_test=testset[["Capacite_accueil","NbChambres","frais_menage","Latitude","Longitude","Caution"]]
y_test=testset[["PrixNuitee"]]


#df2=df[["Capacite_accueil","NbChambres","seche_linge","frais_menage","Latitude","Longitude","Caution","PrixNuitee"]]
#data = df2.values
#X, y = data[:, :-1], data[:, -1]
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

model = Ridge(0.54, normalize=True, fit_intercept=True)
model.fit(X_train, y_train)

error = abs(model.predict(X_test)-y_test)
error = error[:].values

# Visualisation des erreurs et d'un graphe
#print("Erreur moyenne :",mean(error))
#print("Erreur medianne :",median(error))
#print("Erreur min :",min(error))
#print("Erreur max :",max(error))
#plt.scatter(model.predict(X_test),y_test)
#plt.show()
x = model.predict(X_test)
testset["Prix_Estime"] = model.predict(X_test)
testset = testset[["Capacite_accueil","NbChambres","frais_menage","Latitude","Longitude","Caution","Prix_Estime"]]
#export=testset.drop(["PrixNuitee"],axis=1)
#export=export.drop(["prix_nuitee"],axis=1)
export = testset
data_top = export.head(1) 

# Ecriture des données prédites dans un fichier .csv
f = open('./dataPredict.csv', 'w')
writer = csv.writer(f)
writer.writerow(data_top)
for i in range(1,len(export)) :
        writer.writerow(export.iloc[i])


# Connection à la base mongo (sur Atlas)
client = pymongo.MongoClient("mongodb+srv://bigdata:bigdata@rbnbdata.v5j0v.mongodb.net/airbnb2?retryWrites=true&w=majority")
# Récupération de la base airbnb
db = client.airbnb2
# Récupération de la collection predict
collec = db['predict2']
# Conversion du csv en json pour la fonction insert_one
dftojson = pd.read_csv('dataPredict.csv')
dftojson.to_json('data.json')
data = json.load(open('data.json'))
# Insertion des données dans la collection
x = collec.insert_one(data)

# Visualisation des données sur Mongo Charts