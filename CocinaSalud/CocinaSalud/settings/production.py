from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '192.168.0.165',
    '161.35.51.95',
    'cocinasalud.net',
    'www.cocinasalud.net',
    '*.cocinasalud.net',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CocinaSalud',
        'USER': 'root',
        'PASSWORD': config('DATABASE_PASSWORD')
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'