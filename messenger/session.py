# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time

class UserSession:
    """information de la session d'un utilisateur"""

    def __init__(self, date=None, msg=0, step=1, language='unknown', id_message_lg=False, debug=False, id_phase2=None):
        self.__msg = msg #nb de message
        self.__step = step
        if date is None:
            self.__date = datetime.now()
        else:
            self.__date = date
        self.__language = language
        self.__id_message_lg = id_message_lg
        self.__debug = debug
        self.__id_phase2 = id_phase2
        self.__code_phase2 = []
        self.__context = None

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
        self.__id_message_lg = False
        self.__id_phase2 = None
        self.__context = None

    def session_en_cours(self, date):
        return self.__date + timedelta(hours=1) > date

    def __str__(self):
        string = "Nombre de message : " + str(self.get_msg()) + "\n" \
                "étape : " + str(self.get_step()) + "\n" \
                "Date dernier message : " + str(
                self.get_date()) + "\n" \
                "Langue choisie : " + self.get_language() + "\n" \
                "id message choix lg :" + str(self.get_id_message_lg())
        return string


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
