from .base import *

if os.getenv('TRAVIS', False):
    from .travis import *  # noqa

else:
    try:
        from .local import *
    except ImportError, exc:
        exc.args = tuple(['%s (did you rename settings/local.py-dist?)' % exc.args[0]])
        raise exc
