# =====================
# wsgi.py file begin

import os, sys
sys.path.append("/home/wouso/wouso-iulianr-fork.git/")
sys.path.append(os.path.normpath(os.path.dirname(__file__)))

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wouso.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# wsgi.py file end
# ===================
