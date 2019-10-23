"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sa#z5t2gknxm37u18tx^=62^$%m&d^+%5@kqqmkv)09u26+6ms'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('APP_DEBUG')

ALLOWED_HOSTS = ['127.0.0.1','3.16.219.207', 'ec2-3-16-219-207.us-east-2.compute.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

START_APPS = [
    'shopper'
]
INSTALLED_APPS += START_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

POSTGRES_SERVICE = os.environ.get('POSTGRES_SERVICE')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_USER = os.environ.get('POSTGRES_USER')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': POSTGRES_SERVICE,
        'NAME': POSTGRES_DB,
        'PASSWORD': POSTGRES_PASSWORD,
        'PORT': POSTGRES_PORT,
        'USER': POSTGRES_USER
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOG_PATH = '/app/log/'
LOG_FILENAME = f'{datetime.datetime.now().strftime("%Y-%m-%d")}.log'
LOGGING = {
    'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
       'base': {
           'format': '%(asctime)s %(levelname)-8s %(name)-10s %(message)s',
       },
   },
   'handlers': {
       'console': {
           'class': 'logging.StreamHandler',
           'formatter': 'base',
       },
       'file': {
           'class': 'logging.handlers.RotatingFileHandler',
           'filename': f'{LOG_PATH}{LOG_FILENAME}',
           'backupCount': 3,
           'formatter': 'base',
       }
   },
   'loggers': {
       'django': {
           'handlers': ['file'],
           'level': os.getenv('APP_LOG_LEVEL', 'DEBUG'),  # change debug level as appropiate
           'propagate': True,
       },
       'django.request': {
           'handlers': ['console'],
           'propagate': True,
       },
       'django.server': {
           'handlers': ['console'],
           'propagate': True,
       },
       'django.template': {
           'handlers': ['console'],
           'propagate': True,
       },
       'django.db.backends': {
           'handlers': ['console'],
           'propagate': True,
       }
   },
}

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 0))
EMAIL_USE_TLS = True
DEFAULT_TO_EMAIL = os.environ.get('DEFAULT_TO_EMAIL', '').split(',')

# telegram bot setting. Please modify the info accordingly.
BOT_TOKEN = os.getenv('BOT_TOKEN',
                      '644028956:AAEWFSzP0iHrscifhtGImnFssYLwJfo2fEs')
BOT_NOTIFY_GROUP_ID = int(os.getenv('BOT_NOTIFY_GROUP_ID', -216542816))
