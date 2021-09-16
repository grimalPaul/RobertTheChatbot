from flask import Flask, request, jsonify
from mongo import insert_intents, get_utters
from random import randint
from prediction import predictorFR, predictorEN
from function_wikiquote import quote

app = Flask(__name__)

sensibility = 0.1

relanceFR = [
    "FR_QUOI",
    "FR_REPEAT",
    "FR_REPEAT_INPUT"
]

relanceEN = [
    "QUOI_EN",
    "REPEAT_EN",
]


@app.route("/")
def hello_word():
    return "Hello_word"


@app.route('/prediction', methods=['POST'])
def prediction():
    req = request.get_json()
    language = req["language"]
    intents = req["intent"]
    context = req["context"]
    print(context)
    if language is None:
        raise ValueError("Language is false " + str(language))
    if intents is None:
        raise ValueError("Intents is Null")
    if language == 'FR':
        predict = predictorFR.predict(intents)
    elif language == 'EN':
        predict = predictorEN.predict(intents)
    else:
        print("error de language")
        raise ValueError("Language is false " + str(language))
    insert_intents(intents, predict[0:5], language)
    label = predict[0][0]
    if predict[0][1] < sensibility:
        if language == 'EN':
            label = 'DEFAULT_EN'
        else:
            label = 'FR_DEFAULT'
    # si c'est une relance on utilise l'ancien context
    if language == 'FR':
        if label in relanceFR and context is not None:
            label = context
    elif language == 'EN':
        if label in relanceEN and context is not None:
            label = context
    responses = get_utters(label, language)
    try:
        citation = quote(label, language)
    except ValueError:
        citation = None
    except KeyError:
        citation = None
    """
    error = f"label {predict[0:5]} \nintent {intents}" \
            f"\n response : {responses}" \
            f"language {language}" \
            f"\n citation : {citation}"
    """
    """
    code 0 : ni citation ni utters pour ce label
    code 1 : citation pour ce label
    code 2 : utters
    code 3 : utters + citation
    """
    if len(responses) != 0 and citation is not None:
        return jsonify({
            "response": responses[randint(0, (len(responses) - 1))],
            "proba": predict[0:5],
            "citation": citation,
            "code": 3,
            "context": label
        })
    elif citation is not None and len(responses) == 0:
        return jsonify({
            "response": "Error",
            "citation": citation,
            "proba": predict[0:5],
            "code": 1,
            "context": label
        })
    elif citation is None and len(responses) != 0:
        return jsonify({
            "response": responses[randint(0, (len(responses) - 1))],
            "citation": citation,
            "proba": predict[0:5],
            "code": 2,
            "context": label
        })
    else:
        return jsonify({
            "response": "Error",
            "citation": citation,
            "proba": predict[0:5],
            "code": 0,
            "context": label
        })
