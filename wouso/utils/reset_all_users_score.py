#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/reset_user_score.py

import sys
import os

# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from wouso.core.user.models import Player
from wouso.core.scoring.models import History

def main():
    History.objects.all().delete()
    plist = Player.objects.all()
    for p in plist:
        p.points = 0
        p.level_no = 1
        p.max_level = 0
        p.last_seen = None
        p.save()

if __name__ == "__main__":
    sys.exit(main())
