import json

from jingo import register
from jingo_minify.helpers import get_js_urls


@register.function
def js_urls_json(bundle):
    """Return a JSON list of the URLs for the requested asset bundle."""
    return json.dumps(get_js_urls(bundle))
