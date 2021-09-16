# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time


# la date ne se met pas à jour


# on va créer un objet session avec en clé, l'id de l'utilisateur
# session = {"id_utilisateur" : {"msg" : 0, "step" : 1, "date" : datetime.datetime(2021, 4, 9, 11, 36, 14, 807832)]}
# session = {}

# session[user.id] = [0,1,datetime.now()]

class UserSession:
    """information de la session d'un utilisateur"""

    def __init__(self, date=None, msg=0, msg_jeu=0, step=1, language='unknown', id_message_lg=None, debug=False, id_phase2=None, id_jeu=None):
        self.__msg = msg #nb de message avant de passer en phase 2
        self.__msg_jeu = msg_jeu #nb de message dans la partie de jeu
        self.__step = step
        if date is None:
            self.__date = datetime.now()
        else:
            self.__date = date
        self.__language = language
        self.__id_message_lg = id_message_lg
        self.__debug = debug
        self.__id_phase2 = id_phase2 #Message auquel l'utilisateur répond
        self.__code_phase2 = [] #Nb de réactions possibles sous les messages
        self.__context = None
        self.__id_jeu = id_jeu
        self.__score_jeu_user = 0
        self.__score_jeu_bot = 0

    def set_context(self, context):
        self.__context = context

    def get_context(self):
        return self.__context

    def set_code_phase2(self, code_phase2):
        self.__code_phase2 = code_phase2

    def get_code_phase2(self):
        return self.__code_phase2

    def set_id_phase2(self, id_phase2):
        self.__id_phase2 = id_phase2

    def get_id_phase2(self):
        return self.__id_phase2

    def set_debug(self, state):
        self.__debug = state

    def get_debug(self):
        return self.__debug

    def get_msg(self):
        return self.__msg

    def get_step(self):
        return self.__step

    def get_date(self):
        return self.__date

    def get_language(self):
        return self.__language

    def get_id_message_lg(self):
        return self.__id_message_lg

    def set_id_message_lg(self, id_message_lg):
        self.__id_message_lg = id_message_lg

    def set_language(self, language='unknown'):
        self.__language = language

    def set_msg(self, msg=0):
        self.__msg = msg

    def set_step(self, step=1):
        self.__step = step

    def set_date(self, date=None):
        if date is None:
            self.__date = datetime.now()
        else:
            self.__date = date

    def inc_msg(self, n=1):
        self.__msg += n

    def set_default(self):
        self.__msg = 0
        self.__step = 1
        self.__id_message_lg = None
        self.__id_phase2 = None
        self.__context = None
        self.set_default_jeu()

    def session_en_cours(self, date):
        return self.__date + timedelta(hours=1) > date

    def __str__(self):
        string = "Nombre de message : " + str(self.get_msg()) + "\n" \
                "étape : " + str(self.get_step()) + "\n" \
                "Date dernier message : " + str(
                self.get_date()) + "\n" \
                "Langue choisie : " + self.get_language() + "\n" \
                "id message choix lg :" + str(
            self.get_id_message_lg()) + "\n" \
                "id message jeu :" + str(
            self.get_id_jeu())
        return string

    # Code pour gérer la phase de jeu
    def set_score_jeu_user(self, score_jeu_user):
        self.__score_jeu_user = score_jeu_user

    def get_score_jeu_user(self):
        return self.__score_jeu_user

    def inc_score_jeu_user(self, n=1):
        self.__score_jeu_user += n

    def set_score_jeu_user(self, score_jeu_bot):
        self.__score_jeu_bot = score_jeu_bot

    def get_score_jeu_bot(self):
        return self.__score_jeu_bot

    def inc_score_jeu_bot(self, n=1):
        self.__score_jeu_bot += n

    def set_id_jeu(self, id_jeu):
        self.__id_jeu = id_jeu

    def get_id_jeu(self):
        return self.__id_jeu

    def set_msg_jeu(self, msg_jeu=0):
        self.__msg_jeu = msg_jeu

    def get_msg_jeu(self):
        return self.__msg_jeu

    def inc_msg_jeu(self, n=1):
        self.__msg_jeu += n

    def set_default_jeu(self):
        self.__msg_jeu = 0
        self.__score_jeu_bot = 0
        self.__score_jeu_user = 0
        self.__id_jeu = None


if __name__ == '__main__':
    # Tester la classe
    u1 = UserSession()
    print(u1)
    time.sleep(1)
    u2 = UserSession()
    print(u2)
    time.sleep(2)
    u3 = UserSession()
    print(u3)
    print("moins d'une heure : ", u3.session_en_cours(datetime.now()))
