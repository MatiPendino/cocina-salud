from .base import *
from decouple import config

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

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
