#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PYTHONPATH=../:. python utils/add_questions.py utils/sample-data/sample-questions.csv

import sys
import os
import codecs


# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from wouso.interface.apps.lesson.models import Lesson, LessonTag, LessonCategory

maps = {
    '1': 'Funcții',
    '2': 'Funcții',
    '3': 'Funcții',
    '4': 'Funcții',
    '5': 'Funcții',
    '6': 'Legile gazului ideal',
    '7': 'Legile gazului ideal',
    '8': 'Legile gazului ideal',
    '9': 'Principiul I al termodinamicii',
    '10': 'Principiul I al termodinamicii',
    '11': 'Principiul I al termodinamicii',
    '12': 'Principiul I al termodinamicii',
    '13': 'Principiul I al termodinamicii',
    '14': 'Principiul I al termodinamicii',
    '15': 'Principiul I al termodinamicii',
    '16': 'Funcții',
    '17': 'Funcții',
    '18': 'Funcții',
    '19': 'Funcții',
    '20': 'Ecuații',
    '21': 'Ecuații',
    '22': 'Numere reale și numere complexe',
    '23': 'Numere reale și numere complexe',
    '24': 'Numere reale și numere complexe',
    '25': 'Numere reale și numere complexe',
    '26': 'Numere reale și numere complexe',
    '27': 'Calcul diferențial',
    '28': 'Calcul diferențial',
    '29': 'Numere reale și numere complexe',
    '30': 'Calcul diferențial',
    '31': 'Calcul diferențial',
    '32': 'Calcul diferențial',
    '33': 'Calcul diferențial',
    '34': 'Calcul diferențial',
    '35': 'Calcul diferențial',
    '36': 'Calcul diferențial',
    '37': 'Calcul diferențial',
    '38': 'Substanțe chimice',
    '39': 'Substanțe chimice',
    '40': 'Substanțe chimice',
    '41': 'Substanțe chimice',
    '42': 'Substanțe chimice',
    '43': 'Substanțe chimice',
    '44': 'Substanțe chimice',
    '45': 'Echilibru chimic',
    '46': 'Echilibru chimic',
    '47': 'Echilibru chimic',
    '48': 'Echilibru chimic',
    '49': 'Echilibru chimic',
    '50': 'Noțiuni de termochimie',
    '51': 'Noțiuni de termochimie',
    '52': 'Noțiuni de termochimie',
    '53': 'Noțiuni de termochimie',
    '54': 'Aromatici',
    '55': 'Aromatici',
    '56': 'Aromatici',
    '57': 'Clase compuși',
    '58': 'Introducere în chimie organică',
    '59': 'Introducere în chimie organică',
    '60': 'Introducere în chimie organică',
    '61': 'Introducere în chimie organică',
    '62': 'Clase compuși',
    '63': 'Clase compuși',
    '64': 'Clase compuși',
    '65': 'Probleme de chimie organică',
    '66': 'Probleme de chimie organică',
}

def main():
    for key, value in maps.items():
        lesson = Lesson.objects.get(id=int(key))
        tag = LessonTag.objects.get(name=value)
        print 'Tagging lesson', lesson, 'with tag', tag
        lesson.tag = tag
        lesson.save()


if __name__ == '__main__':
    sys.exit(main())
