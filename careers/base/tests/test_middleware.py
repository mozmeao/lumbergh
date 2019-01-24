from unittest.mock import Mock

from django.http import HttpResponseRedirect
from django.test import RequestFactory

from careers.base.middleware import LocaleRedirectionMiddleware
from careers.base.tests import TestCase


class RedirectionTests(TestCase):
    def setUp(self):
        self.requestfactory = RequestFactory()
        self.response_mock = Mock()
        self.middleware = LocaleRedirectionMiddleware(self.response_mock)

    def test_locale_redirection(self):
        test_urls = [
            ('/en-US/', '/'),
            ('/en-US/foo', '/foo'),
            ('/en-US/foo/bar/', '/foo/bar/'),
        ]

        for requested_url, expected_url in test_urls:
            request = self.requestfactory.get(requested_url)
            response = self.middleware(request)
            assert isinstance(response, HttpResponseRedirect)
            assert response.url == expected_url

    def test_no_rediction_needed(self):
        request = self.requestfactory.get('/foo/bar/')
        response = self.middleware(request)
        assert isinstance(response, Mock)

    def test_preserve_params(self):
        request = self.requestfactory.get('/en-US/foo/bar/?foo=bar&yo=lo')
        response = self.middleware(request)
        assert 'foo=bar' in response.url
        assert 'yo=lo' in response.url
