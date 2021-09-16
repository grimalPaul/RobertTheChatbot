from flask import Flask, request, jsonify
import phase2_EN
import phase2_FR
from random import randint

app = Flask(__name__)

dicoFR = phase2_FR.DICO
dicoEN = phase2_EN.DICO
ecouteTokenFR = ["ROBOTIQUE", "AMOUR", "VIE"]
ecouteTokenEN = ["ROBOTIQUE_EN", "AMOUR_EN", "VIE_EN"]


@app.route('/')
def index():
    return 'hello world'


@app.route('/phase2', methods=['POST'])
def phase2():
    req = request.get_json()
    language = req["language"]
    code_msg = req["intent"]
    if language is None:
        raise ValueError("Language is false " + str(language))
    if code_msg is None:
        raise ValueError("code_msg is Null")
    #print("lg = ", language, "cd = ", code_msg)
    if language == 'FR':
        if code_msg == 'ECOUTE':
            code_msg = ecouteTokenFR[randint(0, (len(ecouteTokenFR) - 1))]
        elif code_msg == 'RANDOM':
            keys = list(dicoFR.keys())
            code_msg = keys[randint(0, (len(keys) - 1))]
        response = dicoFR[code_msg]
    else:
        if code_msg == 'ECOUTE_EN':
            code_msg = ecouteTokenEN[randint(0, (len(ecouteTokenEN) - 1))]
        elif code_msg == 'RANDOM_EN':
            keys = list(dicoEN.keys())
            code_msg = keys[randint(0, (len(keys) - 1))]
        response = dicoEN[code_msg]
    return jsonify({
        "response": response
    })
