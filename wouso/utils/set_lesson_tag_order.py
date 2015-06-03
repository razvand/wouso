#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PYTHONPATH=../:. python utils/list_lessons.py

import sys
import os
import codecs


# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from wouso.interface.apps.lesson.models import Lesson, LessonTag, LessonCategory


def print_tag_lessons(tag):
    print " > Tag %s" % (tag)
    for l in Lesson.objects.filter(tag=tag):
        print "    > Lesson %s (id: %d)" % (l, l.id)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print >>sys.stderr, "%s tag order_string" % (sys.argv[0])
        sys.exit(1)

    tag_name = sys.argv[1]
    try:
        lt = LessonTag.objects.get(name=tag_name)
    except Exception, e:
        print >>sys.stderr, "No such tag %s" % (tag_name)
        sys.exit(1)

    if len(sys.argv) == 2:
        print_tag_lessons(lt)
        sys.exit(0)

    tag_name = sys.argv[1]
    tag_order_string = sys.argv[2]

    lt.order = tag_order_string
    lt.save()

    print "Lessons in tag %s" % (tag_name)
    for l in lt.get_lessons():
        print "     > Lesson: ", l

if __name__ == '__main__':
    sys.exit(main())
