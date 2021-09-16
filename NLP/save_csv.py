# -*- coding: utf-8 -*-

import csv


def save_csv(filename, intents, prediction, sep=','):
    with open(filename, "w+", newline='') as csvFile:
        header = ['intents', 'prediction', 'confirmed']
        writer = csv.DictWriter(csvFile, fieldnames=header)
        writer.writerow({
            'intents': intents,
            'prediction': prediction,
            'confirmed': 0,
        })
