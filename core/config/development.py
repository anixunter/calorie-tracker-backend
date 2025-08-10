from decouple import config
from .base import *

# Override base settings
DEBUG = config('DEBUG', default=True, cast=bool)

# Convert ALLOWED_HOSTS to list
import os
allowed_hosts = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts.split(',')]

# Optional: Console email backend for dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar (imported below)
INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    INSTALLED_APPS = [
        'debug_toolbar',
    ] + INSTALLED_APPS

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

    # Debug Toolbar settings
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    }