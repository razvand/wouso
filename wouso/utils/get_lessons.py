#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/get_lessons.py

import sys
import os
import codecs


# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from wouso.interface.apps.lesson.models import Lesson, LessonTag, LessonCategory


def main():
    for lc in LessonCategory.objects.all():
        print " > Category: ", lc
        for lt in lc.get_tags:
            print "     > Tag: ", lt
            for l in lt.get_lessons():
                print "         > Lesson: ", l

if __name__ == '__main__':
    sys.exit(main())
