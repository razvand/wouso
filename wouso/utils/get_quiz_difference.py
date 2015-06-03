#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_quiz_difference.py

import codecs
import sys
import os

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

quiz_list = [
        { "name": "Chimie organică", "initial_id": 21, "final_id": 69, "sum": 0, "num": 0 },
        { "name": "Chimie anorganică", "initial_id": 22, "final_id": 70, "sum": 0, "num": 0 },
        { "name": "Mecanică", "initial_id": 39, "final_id": 65, "sum": 0, "num": 0 },
        { "name": "Termodinamică", "initial_id": 40, "final_id": 66, "sum": 0, "num": 0 },
        { "name": "Electricitate", "initial_id": 41, "final_id": 67, "sum": 0, "num": 0 },
        { "name": "Optică", "initial_id": 42, "final_id": 68, "sum": 0, "num": 0 },
        { "name": "Matematică", "initial_id": 43, "final_id": 52, "sum": 0, "num": 0 }
]

def main():
    for p in Player.objects.all():
        for q_idx in range(0, len(quiz_list)):
            q1 = Quiz.objects.get(id=quiz_list[q_idx]["initial_id"])
            q2 = Quiz.objects.get(id=quiz_list[q_idx]["final_id"])
            try:
                user_quiz1 = UserToQuiz.objects.filter(quiz=q1, user=p)
            except Exception, e:
                continue
            try:
                user_quiz2 = UserToQuiz.objects.filter(quiz=q2, user=p)
            except Exception, e:
                continue
            if not user_quiz1:
                continue
            if not user_quiz2:
                continue
            a = QuizAttempt.objects.filter(user_to_quiz=user_quiz1[0])
            if not a:
                continue
            a1 = a[0]
            a = QuizAttempt.objects.filter(user_to_quiz=user_quiz2[0])
            if not a:
                continue
            a2 = a[0]
            print '"%s","%s","%s","%.2f","%.2f"' %(quiz_list[q_idx]["name"],
                    p.race.title, p.full_name,
                    10.0 * a1.points / q1.points_reward,
                    10.0 * a2.points / q2.points_reward)
            quiz_list[q_idx]["sum"] += (10.0 * a2.points / q2.points_reward) - (10.0 * a1.points / q1.points_reward)
            quiz_list[q_idx]["num"] += 1

    for q_idx in range(0, len(quiz_list)):
        print '"%s","%.2f","%d","%.2f"' % (quiz_list[q_idx]["name"],
                quiz_list[q_idx]["sum"], quiz_list[q_idx]["num"],
                quiz_list[q_idx]["sum"] / quiz_list[q_idx]["num"])


if __name__ == "__main__":
    sys.exit(main())
