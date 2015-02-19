#!/usr/bin/env python

# To test, run from parent folder using a command such as:
# PYTHONPATH=../:. python utils/reset_user_score.py

import sys
import os

# Setup Django environment.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from wouso.games.quiz.models import QuizUser, UserToQuiz, QuizAttempt

def main():
    QuizUser.objects.all().delete()
    UserToQuiz.objects.all().delete()
    QuizAttempt.objects.all().delete()

if __name__ == "__main__":
    sys.exit(main())
