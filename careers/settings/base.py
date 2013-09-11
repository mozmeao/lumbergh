# Django settings file for careers

import os

from funfactory.settings_base import *

# Defines the views served for root URLs.
ROOT_URLCONF = 'careers.urls'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

# Accepted locales
PROD_LANGUAGES = ('de', 'en-US', 'es', 'fr',)


# def JINJA_CONFIG():
#    import jinja2
#    from django.conf import settings
#    config = {'extensions': ['tower.template.i18n', 'jinja2.ext.do',
#                             'jinja2.ext.with_', 'jinja2.ext.loopcontrols',
#                             'l10n_utils.template.l10n_blocks'],
#              'finalize': lambda x: x if x is not None else ''}
#    return config


# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'common': (
            'css/careers.css',
        ),
    },
    'js': {
        'common': (
            'js/libs/jquery-1.7.1.min.js',
            'js/careers.js',
        ),
    }
}

INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Example code. Can (and should) be removed for actual projects.
    'careers.base',
    'careers.careers',
    'django_jobvite',
    'south',
    'jingo_minify',
]


## Auth
PWD_ALGORITHM = 'bcrypt'
HMAC_KEYS = {
    #'2011-01-01': 'cheesecake',
}

# Jobvite URI
JOBVITE_URI = 'http://www.jobvite.com/CompanyJobs/Xml.aspx?c=qpX9Vfwa'
