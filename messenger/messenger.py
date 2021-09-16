from flask import Flask, request
from random import randint, choice
from pymessenger.bot import Bot, requests
from session import UserSession
from datetime import datetime
import time

#from logger import logger

app = Flask(__name__)
ACCESS_TOKEN = "EAAKQFQuGG9wBAHwxa5LIt0vG6cPNFsY9GEX5rWYNBiZAuITYLPrt7GY12yJdRhC46Cp5X5GEKQlcNr3z8ZATGCAGy1Tf9gz4EmIqzVqGIb9H3x422AGvRASs6GBgoEowqZBBz4J2cAy4r9FR9XqbRorOOpk5MMRXnpN9YEzKuZAVGyWCJxTS"
VERIFY_TOKEN = "BotOn1928010280183892"
bot = Bot(ACCESS_TOKEN)

# Gestion des sessions utilisateurs
session = {}

language = ["FR", "EN"]
prefix = "!"
list_command = ["!start", "!debug", "!phase2", "!robert", "!help"]
code_reponse = ['A', 'B', 'C', 'D']
answers_phase2 = ['A', 'B', 'C', 'D']
start = ['INTRO', 'INTRO_EN']
end = ['FIN', 'FIN_EN']
max_msg_phase1 = 10
list_code = {
    0: "pas de citation pas d'utters",
    1: "citation pour ce label",
    2: "utters",
    3: "utters + citation"
}

message_error = [
    "*Bzzzzz Bzzzz*, je ne me sens pas bien, j'ai eu un bug.\nMais ca va mieux, nous pouvons reprendre ! ❤️",
    "*Bzzzzz Bzzzz*, something happened... I bugged.\nSorry I'm tired.\nBut let's continue. I feel better ! ❤️",
    "*Bzzzzz Bzzzz* Houston, we have a problem 🛸 I need to reboot...\n....\n....\n....\nREBOOT...OK"
]

msg_help = "List of commands :\n" \
           "____\n" \
           "🔮 !start\n" \
           " 🇬🇧 If you want to start just type !start\n" \
           " 🇫🇷 Si tu veux commencer tu n'as plus qu'à taper !start\n" \
           "____\n" \
           "⚙ !debug\n" \
           " 🇬🇧 If you want to see more info about my answer and our conversation type !debug \n" \
           " 🇫🇷 Si tu veux voir plus d'informations sur notre conversation et mes réponses tape !debug"


def get_time(timestamp: int):
    """
    Convert timestamp to date
    Args:
        timestamp:

    Returns: datetime object

    """
    return datetime.fromtimestamp(timestamp / 1000.0)


def get_message_error(reboot=False, language=None):
    if reboot:
        return message_error[2]
    elif language == 'FR':
        return message_error[0]
    else:
        return message_error[1]


def convert_json(message, language, context=None):
    """
    Construit un dictionnaire au format compréhensible pour l'API NLP
    celui ci pourra être converti en json

    Args:
        message: string
        language: string

    Returns:
        dictionnaire

    """
    json_file = {
        'language': language,
        'intent': message,
        'context': context
    }
    return json_file


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        # logger.debug(f"OUTPUT = {output}")
        # logger.debug(f"OUTPUT ENTRY = {output['entry']}")
        for event in output['entry']:
            if event.get('messaging') or event.get('standby'):
                if event.get('messaging'):
                    messaging = event['messaging']
                else:
                    messaging = event['standby']
            else:
                return "Non exploitable"
            for message in messaging:
                # on commence par vérifier si nouvel utilisateur
                time = None
                if message.get('timestamp'):
                    time = get_time(message['timestamp'])
                if not message.get('sender'):
                    return "Pas d'utilisateur"
                else:
                    user_id = message['sender']['id']
                    # Si utilisateur déjà connu
                    if user_id in session:
                        # vérifier si possède une langue
                        if session[user_id].get_language() == "unknown":
                            # pas de langue, voir si la personne a choisi une langue via bouton
                            if message.get('message').get('quick_reply') and message["message"]['quick_reply'][
                                'payload'] in language:
                                # la personne a donc cliqué sur un bouton pour sélectionner une langue
                                session[user_id].set_id_message_lg(False)
                                session[user_id].set_language(message["message"]['quick_reply']['payload'])
                                if message["message"]['quick_reply']['payload'] == "FR":
                                    send_message(user_id, "Parfait, de quoi veux-tu parler ?")
                                    return "Debut de la conversation FR"
                                else:
                                    send_message(user_id, "Great! What do you want to talk about ?")
                                    return "Debut de la conversation EN"
                            else:
                                # Il n'a pas sélectionner de langue on va donc insister
                                session[user_id].set_id_message_lg(True)
                                return whichLanguage(user_id)
                        else:
                            # l'utilisateur possède une langue c'est OK
                            # On regarde si c'est un bouton qui a été cliqué et si oui si on est en phase 2
                            if session[user_id].get_step() == 2 \
                                    and message.get('message').get('quick_reply') \
                                    and message["message"]['quick_reply']['payload'] in answers_phase2:
                                # Gestion de la phase 2
                                phase2Buttons(user_id, message["message"]['quick_reply']['payload'])
                                session[user_id].set_date(time)
                                # logger.debug("Gestion de la phase 2")
                                return "Gestion de la phase 2"
                            elif message.get('message') and message['message'].get('text') and not message.get(
                                    'message').get('quick_reply'):
                                # on a un message
                                if message['message']['text'] in list_command:
                                    if '!start' in message['message']['text']:
                                        session[user_id].set_default()
                                        session[user_id].set_language()
                                        session[user_id].set_id_message_lg(True)
                                        return whichLanguage(user_id)
                                    elif '!debug' in message['message']['text']:
                                        if session[user_id].get_debug():
                                            session[user_id].set_debug(False)
                                            send_message(user_id, "DebugMode : Off")
                                        else:
                                            session[user_id].set_debug(True)
                                            send_message(user_id, "DebugMode : On")
                                        return 'success'
                                    elif '!phase2' in message['message']['text']:
                                        return start_phase2(user_id)
                                    elif '!help' in message['message']['text']:
                                        send_message(user_id, msg_help)
                                        return 'success'
                                    else:
                                        # pour les autres commandes
                                        return 'success'
                                session_en_cours = session[user_id].session_en_cours(time)
                                if session_en_cours:
                                    session[user_id].inc_msg()
                                else:
                                    # si session plus en cours on remet à 0 les messages
                                    session[user_id].set_msg()
                                session[user_id].set_date(time)
                                if session[user_id].get_msg() > max_msg_phase1 and session[user_id].get_step() != 2:
                                    return start_phase2(user_id)
                                elif session[user_id].get_step() == 1:
                                    # Gestion de la phase 1 de manière classique
                                    phase1(user_id, message['message']['text'])
                                    return "success"
                                else:
                                    # utilisateur a écrit alors que phase 2
                                    if session[user_id].get_language() == 'FR':
                                        rep = f"Appuie sous les boutons "
                                        code_reponse_oublie = [code_reponse[i] for i in
                                                               range(len(session[user_id].get_code_phase2()))]
                                        for i in code_reponse_oublie:
                                            rep += i + " "
                                        rep += "situés sous mon message pour continuer. Si vraiment tu veux me reboot, entre "
                                        rep += list_command[0] + "."
                                        if not session_en_cours:
                                            rep = "Nous n'avions pas terminé notre conversation...\n" + rep
                                        arg = [[i, i] for i in
                                               code_reponse_oublie]
                                        sendButtons(user_id, rep, arg)
                                        return "success"
                                    elif session[user_id].get_langage() == 'EN':
                                        rep = "Don't forget to press the emojis "
                                        code_reponse_oublie = [code_reponse[i] for i in
                                                               range(len(session[user_id].get_code_phase2()))]
                                        for i in code_reponse_oublie:
                                            rep += i + " "
                                        rep += " Under the message to continue. If you really want to start over just type "
                                        rep += list_command[0] + "."
                                        if not session_en_cours:
                                            rep = "We haven't finish our little talk...\n" + rep
                                        arg = [[i, i] for i in
                                               code_reponse_oublie]
                                        sendButtons(user_id, rep, arg)
                                        return "success"
                                    else:
                                        pass
                            else:
                                # S'il clique sur une bouton alors que pas en phase 2
                                # obsolete ci dessous avec les quick_replies
                                if session[user_id].get_step() != 2 \
                                        and message.get('message').get('quick_reply') \
                                        and message["message"]['quick_reply']['payload'] in answers_phase2:
                                    return "success"
                                # si c'est une photo etc il faudra le gérer
                                # TODO: GERER LES AUTRES CAS QUI PEUVENT ARRIVER
                                return "success"
                    # sinon on l'ajoute et demande langue
                    else:
                        session[user_id] = UserSession(
                            date=time,
                            id_message_lg=True
                        )
                        return whichLanguage(user_id)


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!",
                        "We're greatful to know you :)"]
    # return selected item to the user
    return choice(sample_responses)


# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def whichLanguage(recipient_id):
    msg = "Choose your language! Click on 🇬🇧 for English, 🇫🇷 for French \n" \
          "____\n" \
          "Choisis ta langue ! Clique sur 🇬🇧 pour anglais, sur 🇫🇷 pour français\n" \
          "____\n" \
          "Type !start to choose another language if you get the wrong button\n"
    arg = [["🇫🇷", "FR"], ["🇬🇧", "EN"]]
    return sendButtons(recipient_id, msg, arg)


def sendButtons(recipient_id, text, arg):
    payload = {
        'recipient': {
            'id': recipient_id
        },
        "messaging_type": "RESPONSE",
        'message': {
            "text": text,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": i[0],
                    "payload": i[1]
                } for i in arg
            ]

        }
    }
    bot.send_raw(payload)
    return "sucess"


def phase2_progress(user_id, json):
    """
    Gestion de la phase 2

    Args:
        user_id: User
        json: dictionnaire, permet de faire la requete à l'api phase2

    Returns:

    """
    '''pour test 
    msg = {"response": [
        ["AH GENIAL !"],
        [
            ["Vas y je t'écoute", "ECOUTE"],
            ["Je m'ennuie déjà...", "SAOULE"]
        ]
    ]}
    '''
    # r = requests.post('http://127.0.0.1:5002/phase2', json=json, timeout=5)
    r = requests.post('http://phase2:5002/phase2', json=json, timeout=5)
    msg = r.json()
    rep = msg['response'][0]
    # logger.debug(f"rep = {rep}")
    ans = msg['response'][1]
    if ans[0][1] in end:
        session[user_id].set_default()
        for sentence in rep:
            time.sleep(int(len(sentence) / 30))
            send_message(user_id, sentence)
        session[user_id].set_language()
        whichLanguage(user_id)
        return "Fin de la phase 2, on recommence"
    code_phase2 = []
    for i in range(len(ans)):
        code_phase2.append(ans[i][1])
    session[user_id].set_code_phase2(code_phase2)
    arg = [[code_reponse[i], answers_phase2[i]] for i in range(len(code_phase2))]
    for sentence in rep:
        time.sleep(int(len(sentence) / 30))
        send_message(user_id, sentence)
    for i in range(len(ans)):
        send_message(user_id, f"{code_reponse[i]} ) {ans[i][0]}")
    if session[user_id].get_language() == 'FR':
        sendButtons(user_id, "Clique sur un bouton ci-dessous", arg)
    else:
        sendButtons(user_id, "Click on a button below", arg)


def phase2Buttons(user_id, code):
    '''
    Voir quel bouton a été cliqué
    Args:
        user_id: id
        code: code reponse utilisé

    Returns:

    '''
    idx = 4
    if code == answers_phase2[0]:
        idx = 0
    elif code == answers_phase2[1] and len(session[user_id].get_code_phase2()) >= 2:
        idx = 1
    elif code == answers_phase2[2] and len(session[user_id].get_code_phase2()) >= 3:
        idx = 2
    elif code == answers_phase2[3] and len(session[user_id].get_code_phase2()) >= 4:
        idx = 3
    if idx != 4:
        try:
            json = convert_json(session[user_id].get_code_phase2()[idx],
                                session[user_id].get_language())
            phase2_progress(user_id, json)
        except:
            send_message(user_id, get_message_error(reboot=True))
            session[user_id].set_default()


def start_phase2(user_id):
    session[user_id].set_step(2)
    # Debut de la phase 2
    try:
        if session[user_id].get_language() == 'FR':
            idx = 0
        else:
            idx = 1
        json = convert_json(start[idx],
                            session[user_id].get_language())
        phase2_progress(user_id, json)
        return "success"
    except:
        print("Error")
        # logger.debug("Erreur de demarrage de la phase 2")
        send_message(user_id, get_message_error(reboot=True))
        session[user_id].set_default()
        return "Erreur pour le démarrage de la phase 2"


def phase1(user_id, message):
    '''
    Gestion de la phase 1

    Args:
        user_id:

    Returns:

    '''
    json = convert_json(
        message,
        session[user_id].get_language(),
        session[user_id].get_context()
    )
    try:
        '''pour test 
        msg = {
            "response": "la Réponse",
            "proba": "12",
            "citation": "La citation",
            "code": 3,
            "context": "CONTEXT"
        }
        '''
        r = requests.post('http://api_nlp:5000/prediction', json=json, timeout=50)
        # r = requests.post('http://127.0.0.1:5000/prediction', json=json, timeout=100)
        msg = r.json()
        # logger.debug(f"message = {msg}")
        code = msg["code"]
        context = msg["context"]
        # logger.debug(f"code associé = {code}")
        # logger.debug(f"code associé = {context}")
        rep = ""
        if code == 3:
            userChoice = randint(1, 10)
            if userChoice < 3:
                rep = msg["response"]
            else:
                rep = msg["citation"]
        elif code == 2:
            rep = msg["response"]
        elif code == 1:
            rep = msg["citation"]
        elif code == 0:
            rep = get_message_error(reboot=False, language=session[user_id].get_language())
        session[user_id].set_context(context)
        if session[user_id].get_debug():
            rep = rep + "\n-------Proba------\n"
            for i in msg['proba']:
                rep += str(i) + "\n"
            rep += "contexte : " + context + "\n"
            rep += "\n-------Code réponse------\n"
            rep += str(code) + " : " + list_code[code]
    except ConnectionError as c:
        rep = get_message_error(reboot=False, language=session[user_id].get_language())
        if session[user_id].get_debug():
            rep += "\n-------Error------\n"
            rep += "Error get_nlp" + str(c)
    except TimeoutError as t:
        rep = get_message_error(reboot=False, language=session[user_id].get_language())
        if session[user_id].get_debug():
            rep += "\n-------Error------\n"
            rep += "Error timeout" + str(t)
    except ValueError as e:
        rep = get_message_error(reboot=False, language=session[user_id].get_language())
        if session[user_id].get_debug():
            rep += "\n-------Error------\n"
            rep += "Error label " + str(e)
    except:
        rep = get_message_error(reboot=False, language=session[user_id].get_language())
        if session[user_id].get_debug():
            rep += "\n-------Error------\n"
            rep += "Unknown Error"
    if session[user_id].get_debug():
        rep += "\n-------Session------\n" + str(session[user_id])
    send_message(user_id, rep)
