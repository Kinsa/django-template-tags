"""
Removes querystring, e.g. `?spam=eggs` from the end of a URL (or any other string)

Example usage:
<link rel="canonical" href="{{ request.build_absolute_uri|strip_querystring }}" />
"""

from django.template import Library

register = Library()


def strip_querystring(value):
    try:
        bits = value.split('?')[0]
        return bits
    except:
        return value


register.filter(strip_querystring)
