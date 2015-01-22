"""
WSGI config for mldemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
#pylint: disable=invalid-name

import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(os.path.realpath(BASE_DIR))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mldemo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
