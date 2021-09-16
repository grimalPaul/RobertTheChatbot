# -*- coding: utf-8 -*-
from robertBot import DiscordBot

"""
Pour charger depuis un fichier .env le token
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
"""

if __name__ == '__main__':
	monBot = DiscordBot()
	monBot.run('DISCORD_TOKEN')