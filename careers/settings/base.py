from funfactory.settings_base import *


# Django Settings
##############################################################################

# Defines the views served for root URLs.
ROOT_URLCONF = 'careers.urls'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'careers.base',
    'careers.careers',
    'careers.university',

    'django.contrib.admin',

    'django_jobvite',
    'jingo_minify',
    'south',
]


# Third-party Libary Settings
##############################################################################

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
]

# Accepted locales
PROD_LANGUAGES = ('en-US')

# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'base': (
            'css/base.css',
            'js/libs/video-js/video-js.css',
            'js/libs/video-js/video-js-sandstone.css',
        ),
        'print': (
            'css/print.css',
        ),
        'careers': (
            'css/careers.css',
        ),
        'careers-ie8': (
            'css/careers-ie8.css',
        ),
        'university': (
            'css/university.css',
        ),
        'university-ie8': (
            'css/university-ie8.css',
        ),
        'position': (
            'css/position.css',
        ),
        'listings': (
            'css/listings.css',
        ),
        'listings-ie8': (
            'css/listings-ie8.css',
        ),
    },
    'js': {
        'global': (
            'js/libs/jquery-1.7.1.min.js',
            'js/libs/waypoints.min.js',
            'js/libs/modernizr.custom.96716.js',
        ),
        'common': (
            'js/libs/video-js/video.dev.js',
            'js/base.js',
        ),
        'google_analytics': (
            'js/ga.js',
        ),
        'google_analytics_events': (
            'js/ga_event-tracking.js',
        ),
        'careers': (
            'js/careers.js',
        ),
        'listings': (
            'js/listings.js',
        ),
        'filters': (
            'js/filters.js',
        ),
        'university': (
            'js/university.js',
        ),
        'university_links': (
            'js/university_links.js',
        ),
        'smallscreen': (
            'js/libs/jquery.carouFredSel-6.2.1-packed.js',
            'js/libs/jquery.touchSwipe.min.js',
        ),
        'ie8shims': (
            'js/libs/html5shiv-printshiv.js',
        ),
        'university-ie8': (
            'js/libs/video-js/video.dev.js',
            'js/university-ie8.js',
        ),
    }
}

# Testing configuration.
NOSE_ARGS = ['--logging-clear-handlers', '--logging-filter=-factory,-south']


# Careers-specific Settings
##############################################################################

# Goolge Analytics Code
GA_ACCOUNT_CODE = 'UA-36116321-8'

# URI of Jobvite job feed.
JOBVITE_URI = 'https://www.jobvite.com/CompanyJobs/Xml.aspx?c=qpX9Vfwa&cf=e'
