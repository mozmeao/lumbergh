"""
Django settings for lumbergh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import platform

import dj_database_url
from decouple import Csv, config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.join(BASE_DIR, '..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# Application definition

INSTALLED_APPS = [
    # Project specific apps
    'careers.base',
    'careers.careers',
    'careers.university',

    # Third party apps
    'django_jinja',
    'django_extensions',
    # Django apps
    'django.contrib.staticfiles',
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
)

HOSTNAME = platform.node()
DEIS_APP = config('DEIS_APP', default=None)
DEIS_DOMAIN = config('DEIS_DOMAIN', default=None)
ENABLE_HOSTNAME_MIDDLEWARE = config('ENABLE_HOSTNAME_MIDDLEWARE',
                                    default=bool(DEIS_APP), cast=bool)

if ENABLE_HOSTNAME_MIDDLEWARE:
    MIDDLEWARE = (
        ('careers.base.middleware.HostnameMiddleware',) +
        MIDDLEWARE)


ROOT_URLCONF = 'careers.urls'

WSGI_APPLICATION = 'careers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=True, cast=bool)

USE_TZ = config('USE_TZ', default=True, cast=bool)

STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
STATIC_URL = config('STATIC_URL', '/static/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = config('MEDIA_URL', '/media/')

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.jinja',
            'newstyle_gettext': True,
            'context_processors': [
                'careers.base.context_processors.settings',
                'careers.base.context_processors.i18n',
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'careers.base.context_processors.settings',
            ],
        }
    },
]

ENGAGE_ROBOTS = config('ENGAGE_ROBOTS', default=not DEBUG, cast=bool)

# Goolge Analytics Code
GA_ACCOUNT_CODE = config('GA_ACCOUNT_CODE', default=None)
GTM_ACCOUNT_CODE = config('GTM_ACCOUNT_CODE', default='GTM-MLM3DH')

DEAD_MANS_SNITCH_URL = config('DEAD_MANS_SNITCH', default=None)

GREENHOUSE_BOARD_TOKEN = config('GREENHOUSE_BOARD_TOKEN', default='mozilla')

EVENTS_FILE = os.path.join(ROOT, 'university_events.yml')
