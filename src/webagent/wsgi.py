"""
WSGI config for webagent project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
path = '/var/www/grypar.com/src'
if path not in sys.path:
    sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"] = "webagent.settings" 

application = get_wsgi_application()
