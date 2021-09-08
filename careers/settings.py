"""
Django settings for lumbergh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

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
    # Wagtail Career Apps
    'careers.home',

    # Wagtail Apps
    'wagtail.admin',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'bakery',
    'wagtailbakery',

    # Project specific apps
    'careers.base',
    'careers.careers',

    # Third party apps
    'django_jinja',
    'django_extensions',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)


ROOT_URLCONF = 'careers.urls'

WSGI_APPLICATION = 'careers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PG_NAME'),
        'USER': config('PG_USER'),
        'PASSWORD': config('PG_PASSWORD'),
        'HOST': config('PG_HOST'),
        'PORT': config('PG_PORT'),    
    }
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

BUILD_DIR = '/app/static-build'

BAKERY_VIEWS = (
	'wagtailbakery.views.AllPublishedPagesView',
)

WAGTAIL_SITE_NAME = 'Careers Site Admin'

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
    # 
    #
    # This is part of supporting Jinja Templates...
    # https://docs.wagtail.io/en/v2.2/advanced_topics/jinja2.html
    # 
    { 
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'extensions': [
                'wagtail.core.jinja2tags.core',
                'wagtail.admin.jinja2tags.userbar',
                'wagtail.images.jinja2tags.images',
            ],
            'context_processors': [
                'careers.base.context_processors.settings',
                'careers.base.context_processors.i18n',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'your_app_name', 'templates', 'your_app_name'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'careers.base.context_processors.settings',
                'careers.base.context_processors.i18n',
            ],
        }
    },
]

ENGAGE_ROBOTS = config('ENGAGE_ROBOTS', default=not DEBUG, cast=bool)

# Goolge Analytics Code
GA_ACCOUNT_CODE = config('GA_ACCOUNT_CODE', default=None)
GTM_ACCOUNT_CODE = config('GTM_ACCOUNT_CODE', default='GTM-MLM3DH')

GREENHOUSE_BOARD_TOKEN = config('GREENHOUSE_BOARD_TOKEN', default='mozilla')

DMS_BLOG_FETCH = config('DMS_BLOG_FETCH', default=None)
# allow local development to skip hitting the wordpress API on each page load
SKIP_POSTS = config('SKIP_POSTS', default=False, cast=bool)
