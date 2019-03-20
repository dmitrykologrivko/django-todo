import re

from django.conf.urls import url
from django.core.exceptions import ImproperlyConfigured
from django.views.static import serve


def static(prefix, view=serve, **kwargs):
    """
    Helper function to return a URL pattern for serving files.

    This is function as a workaround for django.conf.urls.static
    to serve static content in debug and production modes.
    """
    if prefix and '://' in prefix:
        return []
    elif not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
    ]
