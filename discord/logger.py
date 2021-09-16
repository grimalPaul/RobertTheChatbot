#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://sametmax.com/ecrire-des-logs-en-python/
import logging
# from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(logging.DEBUG)
# on peut très bien mettre logging.WARN pour afficher uniquement les warnings je crois
# logger.(info|warn|debug|error|critical)

formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
"""Si l'on veut mettre les logs dans un fichier
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
"""

# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.info('Debug Bot go')
logger.warning('Testing %s', 'foo')
