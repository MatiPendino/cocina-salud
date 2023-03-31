from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '161.35.123.98',
    '192.168.0.165'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CocinaSalud',
        'USER': 'mati',
    }
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "",
        "NAME": "cocina_salud",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}'''

STATIC_URL = 'static/'

