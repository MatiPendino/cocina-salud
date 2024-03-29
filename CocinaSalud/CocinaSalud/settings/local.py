from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = ('static',)

