# -*- coding: utf-8 -*-

# from dotenv import load_dotenv
# 
# #va permettre de cacher le token
# load_dotenv(dotenv_path = 'config')
import random
import time

import requests

import discord
from discord import DMChannel
from discord.ext import commands
from message_style import *
from session import UserSession

# a utiliser pour activer les logs
# from logger import logger

prefix = "!"
list_command = ["!start", "!debug", "!phase2", "!robert", "!help"]
code_reponse = ['🇦', '🇧', '🇨', '🇩']
code_jeu = ['👊', '✋', '✌']
code_echap = '❌'
start = ['INTRO', 'INTRO_EN']
end = ['FIN', 'FIN_EN']
max_msg_phase1 = 10
max_msg_jeu = 5
list_code = {
    0: "pas de citation pas d'utters",
    1: "citation pour ce label",
    2: "utters",
    3: "utters + citation"
}

message_error = [
    "*Bzzzzz Bzzzz*, je ne me sens pas bien, j'ai eu un bug.\nMais ca va mieux, nous pouvons parler d'autre chose ! ❤️",
    "*Bzzzzz Bzzzz*, something happened... I bugged.\nSorry I'm tired.\nBut let's speak about something else. I feel better ! ❤️",
    "*Bzzzzz Bzzzz* Houston, we have a problem 🛸 I need to reboot...\n....\n....\n....\nREBOOT...OK"
]

# words that Robert will detect
keyword = [
    "robot",
    "robots",
    "bot",
    "chatbot",
    "robert",
    "bob",
    "bots",
    "chatbots"
]

intrusionMessage = "🇬🇧 I think you're talking about me or about a friend of mine. Let's have a talk.\n\n" \
                   "🇫🇷 J'ai l'impression que tu parles de moi ou d'un ami à moi. Ayons une petite conversation"

game_context = {"FR": ["FR_DEPRESSION", "FR_TRISTESSE", "FR_AMI", "FR_JOUER"],
                "EN": ["AMI_EN", "HUMEUR_TRISTESSE_EN", "JOUER_EN"]}

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


def iskeyword(message):
    """
    Verifie si un mot clés est présent dans la phrase
    Args:
        message: string

    Returns:
        true si le mot est dans la liste, false sinon

    """
    for word in keyword:
        if word in message.lower().split():
            return True
    return False


class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix)
        # ensemble des sessions des utilisateurs
        session = {}
        self.__session = session
        # ensemble des commandes du Bot
        self.add_command(commands.Command(self.appel, name="start"))
        self.add_command(commands.Command(self.debug, name="debug"))
        self.add_command(commands.Command(self.phase2, name="phase2"))
        self.add_command(commands.Command(self.robert, name="robert"))
        self.remove_command('help')
        self.add_command(commands.Command(self.help, name="help"))

    @staticmethod
    async def on_ready():
        print('Bot is ready!')

    async def on_message(self, message):
        """
        Fonction qui va s'occuper de gérer l'action que doit faire Robert si un message
        est envoyé sur un channel sur lequel il est présent ou un message en DM

        Args:
            message: tous les messages que robert peut lire sont détectés (channel, DM, etc)

        Returns:

        """

        # Ne pas détecter ses propres messages
        if message.author == self.user:
            return
        # Si le message est une commande, appliquer la commande
        if message.content in list_command:
            await self.process_commands(message)
        # Sinon gestion du message
        else:
            # check if DMmessage
            user = message.author
            channel = message.channel
            # si DM message
            if isinstance(channel, DMChannel):
                # verification que l'utilisateur a une session
                if user.id in self.__session:
                    # verification que l'utilisateur a choisi un langage
                    if self.__session[user.id].get_language() == "unknown":
                        ctx = await self.get_context(message)
                        await self.appel(ctx)
                        return
                    session_en_cours = self.__session[user.id].session_en_cours(message.created_at)
                    if session_en_cours:
                        self.__session[user.id].inc_msg()
                    else:
                        # si session plus en cours on remet à 0 les messages
                        self.__session[user.id].set_msg()
                    self.__session[user.id].set_date(message.created_at)
                    #Si on a atteint le nombre max de msg de la phase 1
                    if self.__session[user.id].get_msg() > max_msg_phase1 and self.__session[user.id].get_step() == 1:
                        self.__session[user.id].set_step(2)
                        print(str(self.__session[user.id]))
                        try:
                            async with channel.typing():
                                if self.__session[user.id].get_language() == 'FR':
                                    idx = 0
                                else:
                                    idx = 1
                                json = convert_json(start[idx],
                                                    self.__session[user.id].get_language())
                                await self.phase2_progress(user, json)
                        except:
                            print("Error")
                            print("Bug de la phase 2")
                            await DMChannel.send(user, get_message_error(reboot=True))
                            self.__session[user.id].set_default()
                            return
                else:
                    self.__session[user.id] = UserSession(message.created_at)
                    ctx = await self.get_context(message)
                    await self.appel(ctx)
                    return
                # phase 1
                if self.__session[user.id].get_step() == 1:
                    async with channel.typing():
                        json = convert_json(
                            message.content,
                            self.__session[user.id].get_language(),
                            self.__session[user.id].get_context()
                        )
                        try:
                            r = requests.post('http://api_nlp:5000/prediction', json=json, timeout=50)
                            #r = requests.post('http://127.0.0.1:5000/prediction', json=json, timeout=100)
                            msg = r.json()
                            """
                            msg = {"code": 2, "context": "FR_TRISTESSE",
                                   "response": "Test", "citation": "Test",
                                   "proba": [1.0]}
                            """
                            # logger.debug(f"message = {msg}")
                            code = msg["code"]
                            context = msg["context"]

                            #logger.debug(f"code associé = {code}")
                            #logger.debug(f"code associé = {context}")

                            if code == 3:
                                choice = random.randint(1, 10)
                                if choice < 6:
                                    if (context in game_context[self.__session[user.id].get_language()] and choice < 3) \
                                            or context == "FR_JOUER" or context == "JOUER_EN":
                                        if self.__session[user.id].get_language() == 'FR':
                                            rep = "Et si on jouait à Pierre, papier, ciseaux ?" \
                                                  " Le jeu se déroule en 5 manches. Si jamais tu souhaites quitter le jeu avant, " \
                                                  "tu peux le faire en cliquant sur l'emoji " + code_echap
                                        else:
                                            rep = "What about playing a little game of rock, paper, scissors ? " \
                                                  "The game will take place in 5 rounds. If you want to leave before the end, " \
                                                  "feel free to do so by clicking on the emoji " + code_echap
                                        self.__session[user.id].set_step(3)
                                        message_jeu = await DMChannel.send(user, rep)
                                        self.__session[user.id].set_id_jeu(message_jeu.id)
                                        self.__session[user.id].set_date(message_jeu.created_at)
                                        for i in range(len(code_jeu)):
                                            await message_jeu.add_reaction(code_jeu[i])
                                        await message_jeu.add_reaction(code_echap)
                                        self.__session[user.id].inc_msg_jeu()
                                    else:
                                        rep = msg["response"]
                                else:
                                    rep = msg["citation"]
                            elif code == 2:
                                choice = random.randint(1, 10)
                                if (context in game_context[self.__session[user.id].get_language()] and choice < 5)\
                                        or context == "FR_JOUER" or context == "JOUER_EN":
                                    if self.__session[user.id].get_language() == 'FR':
                                        rep = "Pour y remédier, je te propose de jouer à pierre, papier, ciseaux." \
                                        " Le jeu se déroule en 5 manches. Si jamais tu souhaites quitter le jeu avant, " \
                                        "tu peux le faire en cliquant sur l'emoji " + code_echap
                                    else:
                                        rep = "What about playing a little game of rock, paper, scissors ? " \
                                        "The game will take place in 5 rounds. If you want to leave before the end, " \
                                        "feel free to do so by clicking on the emoji " + code_echap
                                    self.__session[user.id].set_step(3)
                                    message_jeu = await DMChannel.send(user, rep)
                                    self.__session[user.id].set_id_jeu(message_jeu.id)
                                    self.__session[user.id].set_date(message_jeu.created_at)
                                    for i in range(len(code_jeu)):
                                        await message_jeu.add_reaction(code_jeu[i])
                                    await message_jeu.add_reaction(code_echap)
                                    self.__session[user.id].inc_msg_jeu()
                                else:
                                    rep = msg["response"]
                            elif code == 1:
                                rep = msg["citation"]
                            elif code == 0:
                                rep = get_message_error(reboot=False, language=self.__session[user.id].get_language())
                            self.__session[user.id].set_context(context)
                            if self.__session[user.id].get_debug():
                                rep = rep + "\n-------Proba------\n"
                                for i in msg['proba']:
                                    rep += str(i) + "\n"
                                rep += "contexte : " + context + "\n"
                                rep += "\n-------Code réponse------\n"
                                rep += str(code) + " : " + list_code[code]
                        except ConnectionError as c:
                            rep = get_message_error(reboot=False, language=self.__session[user.id].get_language())
                            if self.__session[user.id].get_debug():
                                rep += "\n-------Error------\n"
                                rep += "Error get_nlp" + str(c)
                        except TimeoutError as t:
                            rep = get_message_error(reboot=False, language=self.__session[user.id].get_language())
                            if self.__session[user.id].get_debug():
                                rep += "\n-------Error------\n"
                                rep += "Error timeout" + str(t)
                        except ValueError as e:
                            rep = get_message_error(reboot=False, language=self.__session[user.id].get_language())
                            if self.__session[user.id].get_debug():
                                rep += "\n-------Error------\n"
                                rep += "Error label " + str(e)
                        except:
                            rep = get_message_error(reboot=False, language=self.__session[user.id].get_language())
                            if self.__session[user.id].get_debug():
                                rep += "\n-------Error------\n"
                                rep += "Unknown Error"
                        if self.__session[user.id].get_debug():
                            rep += "\n-------Session------\n" + str(self.__session[user.id])
                    if self.__session[user.id].get_step() == 1:
                        await DMChannel.send(user, rep)
                # phase2
                elif self.__session[user.id].get_step() == 2:
                    if self.__session[user.id].get_language() == 'FR':
                        rep = f"Appuie sous les boutons "
                        for i in code_reponse:
                            rep += i + " "
                        rep += "situés sous mon message pour continuer. Si vraiment tu veux me reboot, entre "
                        rep += list_command[0] + "."
                        if not (session_en_cours):
                            rep = "Nous n'avions pas terminé notre conversation...\n" + rep
                        await DMChannel.send(user, rep)
                    elif self.__session[user.id].get_langage() == 'EN':
                        rep = "Don't forget to press the emojis "
                        for i in code_reponse:
                            rep += i + " "
                        rep += " Under the message to continue. If you really want to start over just type "
                        rep += list_command[0] + "."
                        if not (session_en_cours):
                            rep = "We haven't finish our little talk...\n" + rep
                        await DMChannel.send(user, rep)
                    else:
                        pass
                #jeu
                elif self.__session[user.id].get_step() == 3:
                    if self.__session[user.id].get_language() == 'FR':
                        rep = "Appuie sur les boutons " + code_jeu[0] + " " \
                              + code_jeu[1] + " " \
                              + code_jeu[2] + " " \
                              + "situés sous mon message pour continuer. Si tu ne veux pas jouer, appuie sur " \
                              + code_echap + "."
                        await DMChannel.send(user, rep)
                    elif self.__session[user.id].get_langage() == 'EN':
                        rep = "Don't forget to press the emojis " + code_jeu[0] + " " \
                              + code_jeu[1] + " " \
                              + code_jeu[2] + \
                              " Under the message to continue. If you don't want to play, press on " \
                              + code_echap + "."
                        await DMChannel.send(user, rep)
                    else:
                        pass
            else:
                # dans general
                if iskeyword(message.content):
                    embed = discord.Embed(
                        description=intrusionMessage,
                        color=0x0000ff)
                    if user.id in self.__session:
                        if not self.__session[user.id].session_en_cours(message.created_at):
                            await channel.send(f"{user.mention} 👀 I saw you")
                            await DMChannel.send(user, embed=embed)
                    else:
                        await channel.send(f"{user.mention} 👀 I saw you")
                        await DMChannel.send(user, embed=embed)

    async def on_raw_reaction_add(self, payload):
        """
        Fonction qui va écouter si un utilisateur pose une réaction sur un des messages postées
        Detecte réaction même si message pas dans le cache
        https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_raw_reaction_add#discord.on_raw_reaction_add

        Args:
            payload: RawReactionActionEvent

        Returns:

        """
        # Detecte reaction même si message pas dans le cache
        # Ne pas détecter nos propres réactions
        if self.get_user(payload.user_id) == self.user:
            return
        channel = self.get_channel(payload.channel_id)
        if isinstance(channel, DMChannel):
            user = channel.recipient
            # si reaction au message qui demande la langue, on regarde la langue
            if payload.message_id == self.__session[user.id].get_id_message_lg():
                if payload.emoji.name == '🇬🇧':
                    self.__session[user.id].set_id_message_lg(None)
                    self.__session[user.id].set_language('EN')
                    await DMChannel.send(user, "Great! What do you want to talk about ?")
                elif payload.emoji.name == '🇫🇷':
                    self.__session[user.id].set_id_message_lg(None)
                    self.__session[user.id].set_language('FR')
                    await DMChannel.send(user, "Parfait, de quoi veux-tu parler ?")

            # si reaction au message de jeu, on envoie le choix à la fonction associée
            if payload.message_id == self.__session[user.id].get_id_jeu():
                if payload.emoji.name == code_echap:
                    self.__session[user.id].set_step(1)
                    self.__session[user.id].set_default_jeu()
                    print(str(self.__session[user.id]))
                    try:
                        async with channel.typing():
                            if self.__session[user.id].get_language() == 'FR':
                                rep = "J'espère que tu t'es bien amusé ! Est-ce que tu souhaites me parler d'autre chose ?"
                            else:
                                rep = "I hope you enjoyed our party ! Do you want to talk to me about something else ?"
                            await DMChannel.send(user, rep)
                    except:
                        print("Error")
                        print("Bug de la phase 1")
                        await DMChannel.send(user, get_message_error(reboot=True))
                        self.__session[user.id].set_default()
                        return
                else:
                    self.__session[user.id].inc_msg_jeu()
                    await self.game_progress(user, payload.emoji.name)
                    #Si on était en train de jouer et que l'on doit repasser en phase 1
                    if self.__session[user.id].get_msg_jeu() > max_msg_jeu and self.__session[user.id].get_step() == 3:
                        self.__session[user.id].set_step(1)
                        self.__session[user.id].set_default_jeu()
                        print(str(self.__session[user.id]))
                        try:
                            async with channel.typing():
                                if self.__session[user.id].get_language() == 'FR':
                                    rep = "J'espère que tu t'es bien amusé ! Est-ce que tu souhaites me parler d'autre chose ?"
                                else:
                                    rep = "I hope you enjoyed our party ! Do you want to talk to me about something else ?"
                                await DMChannel.send(user, rep)
                        except:
                            print("Error")
                            print("Bug de la phase 1")
                            await DMChannel.send(user, get_message_error(reboot=True))
                            self.__session[user.id].set_default()
                            return

            # Si reaction à un message de la phase 2, on traite pour la phase 2
            if payload.message_id == self.__session[user.id].get_id_phase2():
                idx = 4
                if payload.emoji.name == code_reponse[0]:
                    idx = 0
                elif payload.emoji.name == code_reponse[1] and len(self.__session[user.id].get_code_phase2()) >= 2:
                    idx = 1
                elif payload.emoji.name == code_reponse[2] and len(self.__session[user.id].get_code_phase2()) >= 3:
                    idx = 2
                elif payload.emoji.name == code_reponse[3] and len(self.__session[user.id].get_code_phase2()) >= 4:
                    idx = 3
                if idx != 4:
                    try:
                        async with channel.typing():
                            # print("code", self.__session[user.id].get_code_phase2()[idx])
                            json = convert_json(self.__session[user.id].get_code_phase2()[idx],
                                                self.__session[user.id].get_language())
                            await self.phase2_progress(user, json)
                    except:
                        await DMChannel.send(user, get_message_error(reboot=True))
                        self.__session[user.id].set_default()

    async def appel(self, ctx):
        """
        Commande pour que Robert nous contacte en DM et nous demande notre langue
        Args:
            ctx: discord.ext.commands.Context

        Returns:

        """
        user = ctx.message.author

        msg = "Hi I'm Robert, the chatbot whom you can confide in and who will cheer you up! Choose your language! Click on 🇬🇧 for English, 🇫🇷 for French \n" \
              "Bonjour, c'est moi Robert, le chatbot à qui tu peux confier tes problèmes et qui te redonnera le moral ! Choisis ta langue ! Clique sur 🇬🇧 pour anglais, sur 🇫🇷 pour français" \
              "\nPour changer de langue, retape la commande " + list_command[0] + \
              "\nTo change language just type " + list_command[0]
        """
        msg = "Message de test" \
        "\nPour changer de langue, retape la commande " + list_command[0] + \
        "\nTo change language just type " + list_command[0]
        """
        message = await DMChannel.send(user, msg)
        # print(message.content)
        await message.add_reaction("🇫🇷")
        await message.add_reaction("🇬🇧")
        # print("message id :", message.id)
        if user.id in self.__session:
            self.__session[user.id].set_default()
            self.__session[user.id].set_language()
            self.__session[user.id].set_id_message_lg(message.id)
        else:
            self.__session[user.id] = UserSession(date=message.created_at, id_message_lg=message.id)

    async def debug(self, ctx):
        """
        Activer un mode debug pour voir le fonctionnement de Robert

        Args:
            ctx: discord.ext.commands.Context

        Returns:

        """
        if ctx.message.author.id not in self.__session:
            self.__session[ctx.message.author.id] = UserSession(date=ctx.message.created_at)
        if self.__session[ctx.message.author.id].get_debug():
            self.__session[ctx.message.author.id].set_debug(False)
            await ctx.send("DebugMode : Off")
        else:
            self.__session[ctx.message.author.id].set_debug(True)
            await ctx.send("DebugMode : On")

    async def help(self, ctx):
        """
        Voir les commandes
        Args:
            ctx: discord.ext.commands.Context

        Returns:

        """
        embed = discord.Embed(
            title="List of commands",
            description=
            "🇬🇧 I have 3 commands : !start, !robert and !debug"
            "\n🇫🇷 J'ai 3 commandes : !start, !robert et !debug",
            color=0x0000ff)
        embed.add_field(name="!start",
                        value=" If you want to start just type !start.\n"
                              "Si tu veux commencer tu n'as plus qu'à taper !start.",
                        inline=False)
        embed.add_field(name="!robert",
                        value="If you want some informations about me just type !robert. \n"
                              "Si tu veux des informations sur moi tape !robert.",
                        inline=False)
        embed.add_field(name="!debug",
                        value="If you want to see more info about my answer and our conversation type !debug \n"
                              "Si tu veux voir plus d'informations sur notre conversation et mes réponses tape !debug.",
                        inline=False)
        await ctx.send(embed=embed)

    async def phase2(self, ctx):
        """
        Commande pour forcer le départ de la phase 2 immédiatemment

        Args:
            ctx: discord.ext.commands.Context

        Returns:

        """
        # print("commande tapée")
        user = ctx.message.author
        message = ctx.message
        channel = ctx.channel
        if user.id in self.__session:
            if self.__session[user.id].get_language() == "unknown":
                ctx = await self.get_context(message)
                await self.appel(ctx)
                return
            self.__session[user.id].set_msg(max_msg_phase1)
            self.__session[user.id].set_date(message.created_at)
            # print('debut phase 2')
            self.__session[user.id].set_step(2)
            try:
                async with channel.typing():
                    if self.__session[user.id].get_language() == 'FR':
                        idx = 0
                    else:
                        idx = 1
                    json = convert_json(start[idx],
                                        self.__session[user.id].get_language())
                    await self.phase2_progress(user, json)
            except:
                # print("Error")
                # print("Bug de la phase 2")
                await DMChannel.send(user, get_message_error(reboot=True))
                self.__session[user.id].set_default()
        else:
            self.__session[user.id] = UserSession(message.created_at)
            ctx = await self.get_context(message)
            await self.appel(ctx)

    async def phase2_progress(self, user, json):
        """
        Gestion de la phase 2

        Args:
            user: User
            json: dictionnaire, permet de faire la requete à l'api phase2

        Returns:

        """
        # r = requests.post('http://127.0.0.1:5002/phase2', json=json, timeout=5)
        r = requests.post('http://phase2:5002/phase2', json=json, timeout=5)
        msg = r.json()
        rep = msg['response'][0]
        bot_answer = ""
        for sentence in rep:
            bot_answer += sentence + " "
        ans = msg['response'][1]
        if ans[0][1] in end:
            await DMChannel.send(user, bot_answer)
            self.__session[user.id].set_default()
            self.__session[user.id].set_language()
            time.sleep(5)
            msg = "Choose your language! Click on 🇬🇧 for English, 🇫🇷 for French \n" \
                  "Choisis ta langue ! Clique sur 🇬🇧 pour anglais, sur 🇫🇷 pour français" \
                  "\nPour changer de langue, retape la commande " + list_command[0] + \
                  "\nTo change language just type " + list_command[0]
            message = await DMChannel.send(user, msg)
            self.__session[user.id].set_id_message_lg(message.id)
            await message.add_reaction("🇫🇷")
            await message.add_reaction("🇬🇧")
            return
        code_phase2 = []
        for i in range(len(ans)):
            code_phase2.append(ans[i][1])
        self.__session[user.id].set_code_phase2(code_phase2)
        message_phase2 = await DMChannel.send(user, content=bot_answer, embed=phase2_embed(ans))
        self.__session[user.id].set_id_phase2(message_phase2.id)
        self.__session[user.id].set_date(message_phase2.created_at)
        for i in range(len(ans)):
            await message_phase2.add_reaction(code_reponse[i]) #Ajout des emojis sous le message

    async def game_progress(self, user, user_choice):
        """
        Gestion du jeu

        Args:
            user: User

        Returns:

        """
        choice = random.randint(0, 2)
        if user_choice == code_jeu[0]: #Joueur a joué pierre
            if choice == 1:
                self.__session[user.id].inc_score_jeu_bot()
            elif choice == 2:
                self.__session[user.id].inc_score_jeu_user()
        if user_choice == code_jeu[1]: #Joueur a joué feuille
            if choice == 0:
                self.__session[user.id].inc_score_jeu_user()
            elif choice == 2:
                self.__session[user.id].inc_score_jeu_bot()
        elif user_choice == code_jeu[2]: #Joueur a joué ciseau
            if choice == 0:
                self.__session[user.id].inc_score_jeu_bot()
            elif choice == 1:
                self.__session[user.id].inc_score_jeu_user()
        ans = code_jeu[choice]
        if self.__session[user.id].get_language() == 'FR':
            ans += "\n SCORE :\n" +\
                   "Robert : " + str(self.__session[user.id].get_score_jeu_bot()) \
                   + "\nToi : " + str(self.__session[user.id].get_score_jeu_user())
            if self.__session[user.id].get_msg_jeu() <= max_msg_jeu:
                ans += "\n Pierre, papier, ciseau ! ..."
        else:
            ans += "\n SCORE :\n" + \
                   "Robert : " + str(self.__session[user.id].get_score_jeu_bot()) \
                   + "\nYou : " + str(self.__session[user.id].get_score_jeu_user())
            if self.__session[user.id].get_msg_jeu() <= max_msg_jeu:
                ans += "\n Rock, paper, scissors ! ..."
        message_jeu = await DMChannel.send(user, ans)
        self.__session[user.id].set_id_jeu(message_jeu.id)
        self.__session[user.id].set_date(message_jeu.created_at)
        if self.__session[user.id].get_msg_jeu() <= max_msg_jeu:
            for i in range(len(code_jeu)):
                await message_jeu.add_reaction(code_jeu[i])
            await message_jeu.add_reaction(code_echap)
        
    @staticmethod
    async def robert(ctx):
        """
        Commande pour avoir les informations sur Robert

        Args:
            ctx: discord.ext.commands.Context

        Returns:

        """

        embed = discord.Embed(
            title="Robert your personal development chatbot, Robert ton chatbot de développement personnel",
            description=
            "🇬🇧 Hi I'm Robert, the chatbot whom you can confide in and who will cheer you up! Talk to me as you would to a normal person and I'll help you work your problems out. Don't be afraid if you have to click on emojis on some of my messages, it's so that I can fully understand you.\n"
            "\n🇫🇷 Bonjour, c'est moi Robert, le chatbot à qui tu peux confier tes problèmes et qui te redonnera le moral ! Je suis là pour toi, parle moi comme si j'étais un être humain."
            " Si je te demande de réagir à l'un de mes messages, c'est pour mieux échanger."
            " Dans ce cas, sélectionne l'émoji de ton choix parmi ceux qui s'affichent sous le message.",
            color=0x0000ff)
        embed.add_field(name="!start",
                        value=" If you want to start just type !start.\n"
                              "Si tu veux commencer tu n'as plus qu'à taper !start.",
                        inline=False)
        embed.add_field(name="!robert",
                        value=" If you ever want this message to show up again just type !robert. \n"
                              "Si tu veux revoir ce message il te suffit de taper !robert.",
                        inline=False)
        embed.add_field(name="!help",
                        value=" If you want to see all my commands clearly type !help. \n"
                              "Si tu veux voir toutes mes commandes tape !help.",
                        inline=False)
        await ctx.send(embed=embed)
