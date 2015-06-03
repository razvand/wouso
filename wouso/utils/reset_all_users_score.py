#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/reset_user_score.py

import codecs
import sys
import os
import datetime
import json

reload(sys)
sys.setdefaultencoding('utf8')

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from django.contrib.auth.models import User
from wouso.core.user.models import Race
from wouso.core.user.models import Player
from wouso.games.quiz.models import Quiz, QuizUser, UserToQuiz, QuizAttempt
from wouso.interface.activity.models import Activity
from wouso.core.god import God
from django.db.models import Q


def reset_player_score(p):
    activities = Activity.objects.filter((Q(user_from=p) | Q(user_to=p)) & Q(action='login') & Q(timestamp__gte=datetime.datetime(2015,5,25,17,0)))
    if len(activities) > 100:
        Activity.objects.filter((Q(user_from=p) | Q(user_to=p)) & Q(action='login') & Q(timestamp__gte=datetime.datetime(2015,5,25,17,0))).delete()

    activities = Activity.objects.filter(user_from=p)
    for a in activities:
        if 'Suită' in a.message:
            arguments = json.loads(a.arguments)
            a.delete(a.game, a.user_from, a.user_to, a.message_string, arguments)

    points = 42
    quizzes = UserToQuiz.objects.filter(user=p)
    for q in quizzes:
        if 'Suită' in q.quiz.name:
            q.delete()
            continue
        if q.best_attempt:
            points += q.best_attempt.points

    p.points = points
    p.level_no = God.get_level_for_points(points)
    p.save()


def main():
    for p in Player.objects.all():
        reset_player_score(p)

if __name__ == "__main__":
    sys.exit(main())
