import wikiquote
import random

nbquotes = 50  # nb max de quote qui seront renvoyés

def containsAnyInsult(text):
    with open("bad_words.txt") as file:
        insultes = file.readlines()
    return any(word in text for word in insultes)

def quote(label, language):
    if language == "EN":
        # enlever le EN à la fin
        label = label[:-3]
    elif language == "FR":
        label = label[3:]
    else:
        raise ValueError("Pas de langue adéquate", language)
    language = language.lower()
    if label_citation.get(label):
        if label_citation[label].get(language):
            theme = label_citation[label][language]
        else:
            raise KeyError("Pas de langue prévu", language, label)
    else:
        raise KeyError("Pas de citation prévu pour ce label", label)
    if theme == "quote_of_the_day":
        return wikiquote.quote_of_the_day(language)
    else:
        try:
            citation = wikiquote.quotes(page_title=theme, max_quotes=nbquotes, lang=language)
            listQuotes = list(filter(lambda x: len(x) < 200 and not(containsAnyInsult(x)), citation))
            if not (len(listQuotes)):
                listQuotes = list(filter(lambda x: len(x) < 350 and not(containsAnyInsult(x)), citation))
            if (len(listQuotes)):
                citationFinale = listQuotes[random.randrange(0, len(listQuotes))]
                print(citationFinale)
                return citationFinale
            else:
                print("Aucune citation valide avec le thème choisi")
                return None
        except (wikiquote.utils.NoSuchPageException, wikiquote.utils.DisambiguationPageException):
            print("Page non trouvée")
            return None
        except:
            print("autre Erreur")
            return None


label_citation = {
    "HUMEUR_JOIE": {"en": "joy"},
    "JOIE": {"fr": "joie"},
    "HUMEUR_COLERE": {"en": "anger"},
    "COLERE": {"fr": "colère"},
    "SURPRISE": {"fr": "surprise"},  # "en" : "surprise" Si on veut rajouter
    "HUMEUR_TRISTESSE": {"en": "sadness"},
    "PEUR": {"fr": "peur", "en": "fear"},
    "MAL": {"fr": "mal", "en": "evil"},
    "MERE": {"fr": "mère", "en": "mothers"},
    "PERE": {"fr": "père", "en": "fathers"},
    "VACANCES": {"fr": "vacances", "en": "holidays"},
    "FAMILLE": {"fr": "famille", "en": "family"},
    "ENFANT": {"en": "children"},
    "AMOUR": {"fr": "amour"},
    "LOVE": {"en": "love"},
    "SEXE": {"fr": "sexe", "en": "Human sexual activity"},
    "HUMANITE": {"fr": "humanité", "en": "human"},
    "MONDE": {"en": "world"},
    "DIEU": {"fr": "dieu", "en": "god"},
    "ISLAM": {"fr": "islam", "en": "islam"},
    "CHRISTIANISME": {"fr": "christianisme", "en": "christianity"},
    "AMI": {"fr": "amitié", "en": "friendship"},
    "ANIMAL": {"en": "animals"},
    "TRAVAIL": {"fr": "travail", "en": "work"},
    "SPORT": {"fr": "sport", "en": "sports"},
    "FOOTBALL": {"fr": "football", "en": "association football"},
    "CULTURE": {"fr": "culture", "en": "culture"},
    "LITTERATURE": {"fr": "littérature", "en": "literature"},
    "LECTURE": {"fr": "lecture", "en": "reading"},
    "MUSIQUE": {"fr": "musique", "en": "music"},
    "PAINTING": {"en": "painting"},
    "FILM": {"fr": "cinéma", "en": "film"},
    "ECOLOGIE": {"fr": "écologie", "en": "ecology"},
    "POLITIQUE": {"fr": "politique", "en": "politics"},
    "SOCIALISME": {"fr": "socialisme", "en": "socialism"},
    "COMMUNISME": {"fr": "communisme", "en": "communism"},
    "CAPITALISME": {"fr": "capitalisme", "en": "capitalism"},
    "ECONOMIE": {"fr": "économie", "en": "economics"},
    "CHINE": {"fr": "chine", "en" : "china"},
    "FRANCE": {"fr": "france", "en": "france"},
    "EUROPE": {"fr": "europe", "en": "europe"},
    "USA": {"fr": "États-Unis", "en": "United_States"},
    "TERRORISME": {"fr": "terrorisme", "en": "terrorism"},
    "ALCOOL": {"fr": "alcool", "en": "alcohol"},
    "DROGUE": {"fr": "drogue", "en": "drugs"},
    "MALADIE": {"fr": "santé", "en": "illness"},
    "DEPRESSION": {"fr": "dépression", "en": "depression"},
    "SOUFFRANCE": {"fr": "souffrance", "en": "suffering"},
    "AIDE": {"en": "help"},
    "PSYCHANALYSE": {"fr": "psychanalyse", "en": "psychoanalysis"},
    "REVE": {"fr": "Rêve", "en": "dreams"},
    "HUMOUR": {"fr": "humour", "en": "comedy"},
    "ALIMENTATION": {"fr": "alimentation", "en": "eating"},
    "NOURRITURE": {"en": "food"},
    "APPARENCE": {"fr": "beauté", "en": "beauty"},
    "JEUNESSE": {"fr": "jeunesse", "en": "youth"},
    "CONFIANCE-EN-SOI": {"en": "self-esteem"},
    "HARCELEMENT": {"fr": "harcèlement", "en": "bullying"},
    "XENOPHOBIE": {"fr": "xénophobie", "en": "racism"},
    "INTERNET": {"fr": "internet", "en": "internet"},
    "GOOGLE": {"fr": "google", "en": "google"},
    "ORDINATEURS": {"fr": "ordinateur", "en": "computers"},
    "ROBOT": {"en": "robot"},
    "CITATION": {"fr": "quote_of_the_day"}
}

if __name__ == '__main__':
    quote("FR_AMOUR", "FR")
    quote("CONFIANCE-EN-SOI_EN", "EN")
