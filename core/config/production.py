from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'api.yourapp.com']

# this was in canteen backend like this.
# STATIC_URL = f'{config("STATIC_URL")}/static/'

# Security settings (example)
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Use PostgreSQL in production (example)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'calorie_db',
#         'USER': 'calorie_user',
#         'PASSWORD': '...',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }