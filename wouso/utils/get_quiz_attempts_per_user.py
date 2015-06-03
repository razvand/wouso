#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_quiz_attempts_per_user.py <username>

import sys
import csv
import os
import codecs
import re

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
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s <username>" % (sys.argv[0])
        sys.exit(1)

    username = sys.argv[1]
    qu = QuizUser.objects.get(nickname=username)
    utqlist = UserToQuiz.objects.filter(user=qu)
    for utq in utqlist:
        # Browse all QuizAttempt objects.
        qalist = QuizAttempt.objects.filter(user_to_quiz=utq)
        for qa in qalist:
            print "Quiz attempt on %s for quiz %s by user %s: %s" % (qa.date, qa.user_to_quiz.quiz, qa.user_to_quiz.user, qa.results)

if __name__ == "__main__":
    sys.exit(main())
