from .base import *
from decouple import config

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_NAME'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
        'OPTIONS': {
            'sslmode': 'require',
            'options': '-c search_path=cocina'
        }
    }
}

# Whitenoise settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
INSTALLED_APPS += ['whitenoise.runserver_nostatic']
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [BASE_DIR.parent / 'static']

# S3 Configuration
AWS_ACCESS_KEY_ID = config('AMAZONWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AMAZONWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AMAZONWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False 
AWS_SESSION_TOKEN = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_REGION_NAME = config('AMAZONWS_S3_REGION_NAME')
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
        'OPTIONS': {
            'location': 'media',
        },
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
AWS_DEFAULT_ACL = None