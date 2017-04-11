from django.conf import settings
from django.http import HttpResponseRedirect


class LocaleRedirectionMiddleware(object):
    """Remove the /en-US/ locale part from the URL.

    The sugardough based version of the app doesn't not enable the
    locale middleware for simplicity since the site is not localized.
    To avoid breaking old links that include /en-US/ locale
    identification string, this middleware will automatically convert
    them.

    """

    def process_request(self, request):
        if not request.path.startswith('/en-US/'):
            return

        url = request.get_full_path()[6:]
        return HttpResponseRedirect(url)


class HostnameMiddleware(object):
    def __init__(self):
        values = [getattr(settings, x) for x in ['HOSTNAME', 'DEIS_APP', 'DEIS_DOMAIN']]
        self.backend_server = '.'.join(x for x in values if x)

    def process_response(self, request, response):
        response['X-Backend-Server'] = self.backend_server
        return response
