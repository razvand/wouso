#!/usr/bin/env python

# coding=utf-8
# This has to be used from the wouso folder like so:
# PYTHONPATH=. python utils/import_questions

#
# Import races from CSV file. CSV file must contain two columns: name and
# title. Name is the race identifier, while title is the print information
# shown on the site.Separator is comma (',') and quote character is double
# quotes ('"').
#

import sys
import csv
from django.core.management import setup_environ

def init():
    import settings
    setup_environ(settings)


def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <file.csv>' %(sys.argv[0])
        print " CSV columns: name, title"
        sys.exit(1)

    try:
        init()
    except ImportError:
        print "No wouso/settings.py file. Maybe you can symlink the example file?"
        sys.exit(1)

    from wouso.core.user.models import Race

    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            name, title = row
            race, new = Race.objects.get_or_create(name=name)
            if new:
                print "Adding race", name
                race.title = title
                race.can_play = True
                race.save()
            else:
                print "Race %s already exists. Not adding."

if __name__ == "__main__":
    sys.exit(main())
