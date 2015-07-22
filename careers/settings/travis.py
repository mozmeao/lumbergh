from . import base

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lumbergh_app',
        'USER': 'travis',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
        },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    },
}

DEBUG = TEMPLATE_DEBUG = False
DEV = False
ENGAGE_ROBOTS = True
SESSION_COOKIE_SECURE = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

HMAC_KEYS = {
    '2012-06-06': 'some secret',
}

from django_sha2 import get_password_hashers
PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)

# Make this unique, and don't share it with anybody. It cannot be blank.
SECRET_KEY = 'secret'
