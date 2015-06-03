#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_duplicate_usertoquiz.py

import sys
import csv
import os
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from django.contrib.auth.models import User
from wouso.core.user.models import Player
from wouso.games.quiz.models import Quiz, QuizUser, UserToQuiz, QuizAttempt

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def main():
    utq_duplicates = []
    ulist = QuizUser.objects.all()
    for u in ulist:
        # Find UserToQuiz objects for each player.
        utqlist = UserToQuiz.objects.filter(user=u)

        # Browse UserToQuiz objects and look for duplicates.
        index = 1
        for utq in utqlist:
            for comp in utqlist[index:len(utqlist)]:
                if comp.quiz.id == utq.quiz.id:
                    print "Duplicate found. User/quiz %s, %s" % (utq.user, utq.quiz)
                    utq_duplicates.append(utq)
            index += 1

    for utq in utq_duplicates:
        print "user/quiz to remove %s, %s" % (utq.user, utq.quiz)
        utq.delete()

if __name__ == "__main__":
    sys.exit(main())
