from pymongo import MongoClient
import json

client = MongoClient('mongodb://user:password@mongodb:27017/')

# check si la configuration est bonne
db = client.robert
db.uttersEN.drop()
db.uttersFR.drop()

collist = db.list_collection_names()
if "uttersEN" not in collist:
    # charger les utters
    path = "uttersEN.json"
    with open(path) as json_data:
        data_dict = json.load(json_data)
        for i in data_dict["intents"]:
            db.uttersEN.insert_one({"label": i["tag"], "responses": i["responses"]})

if "uttersFR" not in collist:
    # charger les utters
    path = "uttersFR.json"
    with open(path) as json_data:
        data_dict = json.load(json_data)
        for i in data_dict["intents"]:
            db.uttersFR.insert_one({"label": i["tag"], "responses": i["responses"]})


def insert_intents(intents, prediction, langage):
    newData = {
        'intent': intents,
        'label': prediction[0][0],
        'Verified': False,
        'prediction': prediction[0:4]
    }
    if langage == 'EN':
        result = db.intentsEN.insert_one(newData)
        return True
    elif langage == 'FR':
        result = db.intentsFR.insert_one(newData)
        return True
    else:
        return False


def get_utters(label, langage):
    # find toutes les réponses avec le bon label
    if langage == 'EN':
        request = db.uttersEN.find({"label": label})
        responses = []
        for r in request:
            for rep in r["responses"]:
                responses.append(rep)
        return responses
    elif langage == 'FR':
        request = db.uttersFR.find({"label": label})
        responses = []
        for r in request:
            for rep in r["responses"]:
                responses.append(rep)
        return responses
    else:
        return None
