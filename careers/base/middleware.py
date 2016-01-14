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
