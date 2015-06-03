#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_users_0_quiz.py

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
        print >>sys.stderr, "%s username" % (sys.argv[0])
        sys.exit(1)

    try:
        p = Player.objects.get(nickname=sys.argv[1])
    except Exception, e:
        print >>sys.stderr, "No such player %s" % (sys.argv[1])
        sys.exit(1)

    # Browse all QuizAttempt objects.
    qalist = QuizAttempt.objects.all()
    for qa in qalist:
        if qa.points == 0:
            _qal = QuizAttempt.objects.filter(user_to_quiz=qa.user_to_quiz)
            if len(_qal) == 1:
                if re.search("\[[0-9]+\]", qa.results) is None:
                    if qa.user_to_quiz.user.nickname == sys.argv[1]:
                        print "Quiz attempt on %s for quiz %s by user %s: %s" % (qa.date, qa.user_to_quiz.quiz, qa.user_to_quiz.user, qa.results)
                        qa.delete()

if __name__ == "__main__":
    sys.exit(main())
