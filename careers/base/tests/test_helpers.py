import json

from mock import patch
from nose.tools import eq_

from careers.base.helpers import js_urls_json
from careers.base.tests import TestCase


class JsUrlsJsonTests(TestCase):
    def test_basic(self):
        with patch('careers.base.helpers.get_js_urls') as get_js_urls:
            get_js_urls.return_value = ['g.js', 'h.js']
            urls = js_urls_json('bundle')

        get_js_urls.assert_called_with('bundle')
        eq_(json.loads(urls), ['g.js', 'h.js'])
