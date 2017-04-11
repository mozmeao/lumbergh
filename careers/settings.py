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
import django_cache_url
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
    'raven.contrib.django.raven_compat',

    # Django apps
    'django.contrib.staticfiles',
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'careers.base.middleware.LocaleRedirectionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
)

HOSTNAME = platform.node()
DEIS_APP = config('DEIS_APP', default=None)
DEIS_DOMAIN = config('DEIS_DOMAIN', default=None)
ENABLE_HOSTNAME_MIDDLEWARE = config('ENABLE_HOSTNAME_MIDDLEWARE',
                                    default=bool(DEIS_APP), cast=bool)
if ENABLE_HOSTNAME_MIDDLEWARE:
    MIDDLEWARE_CLASSES = (
        ('snippets.base.middleware.HostnameMiddleware',) +
        MIDDLEWARE_CLASSES)


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
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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

# Django-CSP
CSP_DEFAULT_SRC = (
    "'self'",
    '*.cdn.mozilla.net',
)
CSP_FONT_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'http://*.mozilla.org',
    'https://*.mozilla.org',
)
CSP_IMG_SRC = (
    "'self'",
    "data:",
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'http://*.mozilla.org',
    'https://*.mozilla.org',
    'http://www.google-analytics.com',
    'https://www.google-analytics.com',
)
CSP_SCRIPT_SRC = (
    "'self'",
    "data:",
    'http://*.mozilla.org',
    'https://*.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'http://www.google-analytics.com',
    'https://www.google-analytics.com',
    'http://www.googletagmanager.com',
    'https://www.googletagmanager.com',
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    'http://*.mozilla.org',
    'https://*.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
)
CSP_REPORT_ONLY = config('CSP_REPORT_ONLY', default=False, cast=bool)
CSP_REPORT_ENABLE = config('CSP_REPORT_ENABLE', default=True, cast=bool)

if CSP_REPORT_ENABLE:
    CSP_REPORT_URI = config('CSP_REPORT_URI', default='/csp-violation-capture')

ANON_ALWAYS = True

ENGAGE_ROBOTS = config('ENGAGE_ROBOTS', default=not DEBUG, cast=bool)

# Goolge Analytics Code
GA_ACCOUNT_CODE = config('GA_ACCOUNT_CODE', default=None)
GTM_ACCOUNT_CODE = config('GTM_ACCOUNT_CODE', default='GTM-MLM3DH')

DEAD_MANS_SNITCH_URL = config('DEAD_MANS_SNITCH', default=None)

USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=not DEBUG, cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default='0', cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=False, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=False, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CACHES = {
    'default': config('CACHE_URL', default='locmem://', cast=django_cache_url.parse),
}

RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN', None),
    'release': config('GIT_SHA', None),
    'tags': {
        'server_full_name': '.'.join(x for x in [HOSTNAME, DEIS_APP, DEIS_DOMAIN] if x),
        'environment': config('SENTRY_ENVIRONMENT', ''),
        'site': '.'.join(x for x in [DEIS_APP, DEIS_DOMAIN] if x),
    }
}

GREENHOUSE_BOARD_TOKEN = config('GREENHOUSE_BOARD_TOKEN', default='mozilla')

EVENTS_FILE = os.path.join(ROOT, 'university_events.yml')
