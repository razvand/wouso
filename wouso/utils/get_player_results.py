#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_player_results.py

import sys
import csv
import os
import wouso.utils.user_util

# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from django.contrib.auth.models import User
from wouso.core.user.models import Race
from wouso.core.user.models import Player

def main():
    ulist = User.objects.all()
    accounts_per_race_dict = {}
    for u in ulist:
        try:
            p = Player.objects.get(user__username=u.username)
        except:
            print >> sys.stderr, "No player for username %s." % (u.username)
            continue

        if not p:
            print "Player account for username %s not found." %(u.username)
            continue
        if not p.race:  # Player with no race (such as admin).
            continue

        print "%s,%s,%s,%s,%s,%d" % (u.username, u.first_name, u.last_name, p.race.title, p.last_seen, p.points)

if __name__ == "__main__":
    sys.exit(main())
