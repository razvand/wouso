#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/check_and_get_artifact_to_user.py

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
from django.db.models import Q
from wouso.core.scoring.models import Coin, Formula, History
from core.magic.models import Artifact, PlayerArtifactAmount
from wouso.core.god import God

def main():
    if len(sys.argv) != 3:
        print >>sys.stderr, "%s username artifact" % (sys.argv[0])
        sys.exit(1)

    try:
        p = Player.objects.get(nickname=sys.argv[1])
    except Exception, e:
        print >>sys.stderr, "No such player %s" % (sys.argv[1])
        sys.exit(1)

    artifact_name = sys.argv[2]
    if p.magic.has_modifier(artifact_name):
        print "has %s" % (artifact_name)
    else:
        print "no ach-head-start"

    artifact = God.get_artifact_for_modifier(artifact_name, p)
    result = p.magic.give_modifier(artifact_name)
    if result is not None:
        print "achieved %s" % (artifact_name)

if __name__ == "__main__":
    sys.exit(main())
