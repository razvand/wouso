#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_user_activities.py

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
from wouso.interface.activity.models import Activity
from django.db.models import Q

def main():
    if len(sys.argv) != 2:
        print >>sys.stderr, "%s username" % (sys.argv[0])
        sys.exit(1)

    try:
        p = Player.objects.get(nickname=sys.argv[1])
    except Exception, e:
        print >>sys.stderr, "No such player %s" % (sys.argv[1])
        sys.exit(1)

    activities = Activity.objects.filter(Q(user_from=p) | Q(user_to=p))
    for a in activities:
        print "%s %s %s %s" % (a.timestamp, a.user_from, a.user_to, a.message)

if __name__ == "__main__":
    sys.exit(main())
