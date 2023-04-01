from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
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
}

STATIC_URL = 'static/'
STATICFILES_DIRS = ('static',)

