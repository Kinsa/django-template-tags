=====================
 Django Template Tags
=====================

Installation from Source
========================

::

 $ git clone git@github.com:Kinsa/django-templatetags.git
 $ cd django-django-templatetags
 $ python setup.py install

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following line:

::

 -e git+git://github.com/Kinsa/django-templatetags.git#egg=django_templatetags

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Testing
=======

::

 $ python setup.py test

With TOX

First, install Tox, then run the tests. This will test against the Django versions specified in the environments specified in the ``tox.ini`` file

::

 $ pip install tox
 $ tox

Configure the Project To Include the Application
================================================

Add to the project's settings.py file tuple of installed apps: ::

 'django_templatetags',

Usage
=====

fetch_content
`````````````

Returns a specific number of entries for a particular model. (If the model is sorted by date published they will be sorted that way hence the name get_latest_content.)

Example usage:

::

 {% load fetch_content %}
 {% get_latest_content application_name.model_name 5 as foo %}
 {% for bar in foo %}
     {{ bar.attribute }}
 {% endfor %}

Can also be used to return all entries for a particular model.

Example usage:

::

 {% load fetch_content %}
 {% get_all_content application_name.model_name as foo %}
 {% for bar in foo %}
     {{ bar.attribute }}
 {% endfor %}

nav
```

Handles navigation item selection.

Example usage:

::

 {# Set up the variable for use across context-stacking tags #}
 {% nav %} or {% nav for mynav %}

 {# Set the context so {{ nav.home }} (or {{ mynav.home }}) is True #}
 {% nav "home" %} or {% nav "home" for mynav %}

The most basic (and common) use of the tag is to call ``{% nav [item] %}``,
where `[item]` is the item you want to check is selected.

By default, this tag creates a ``nav`` context variable. To use an
alternate context variable name, call ``{% nav [item] for [var_name] %}``.

To use this tag across ``{% block %}`` tags (or other context-stacking
template tags such as ``{% for %}``), call the tag without specifying an
item.

Your HTML navigation template should look something like:

::

 {% block nav %}
     <ul class="nav">
         <li{% if nav.home %} class="selected"{% endif %}><a href="/">Home</a></li>
         <li{% if nav.about %} class="selected"{% endif %}><a href="/about/">About</a></li>
     </ul>
 {% endblock %}

To override this in a child template, you'd do:

::

 {% include "base.html" %}
 {% load nav %}

 {% block nav %}
     {% nav "about" %}
     {{ block.super }}
 {% endblock %}

This works for multiple levels of template inheritance, due to the fact
that the tag only does anything if the ``nav`` context variable does not
exist. So only the first ``{% nav %}`` call found will ever be processed.

To create a sub-menu you can check against, dot-separate the item:

::

 {% nav "about_menu.info" %}

This will be pass for both ``{% if nav.about_menu %}`` and
``{% if nav.about_menu.info %}``.

widont Filter
`````````````

From: http://djangosnippets.org/snippets/17/

"Widows" are single words that end up on their own line, thanks to automatic line-breaks. This is an no-no in graphic design, and is especially unsightly in headers and other short bursts of text. This filter automatically replaces the space before the last word of the passed value with a non-breaking space, ensuring there is always at least two words on any given line. Usage is like so:

::

 {% load widont %}
 {{ blog.entry.headline|widont }}


dumbquotes Filter
`````````````````

Replaces HTML or UTF-8 encoded double and single quotes (smart quotes) with their "plain text" (dumb quotes) equivalent.

::

 {% load dumb_text %}
 {{ object.attribute|dumbquotes }}


dumbpunct Filter
````````````````

Replaces HTML or UTF-8 encoded ellipsis, ampersands, em dashes, en dashes and non breaking spaces with the "plain text" equivalent.

::

 {% load dumb_text %}
 {{ object.attribute|dumbpunct }}


remel Filter
````````````

Sometimes ``|removetags:"spam"`` isn't enough. Sometimes you need to remove the HTML element and its contents both. For example a ``<figure>`` tag in a pargraph of content that's being used as an excerpt. The ``remel`` filter will do that.

The ``remel`` filter takes exactly one argument, the name of the HTML element to remove.

::

 {% load remel %}
 {{ object.attribute|remel:"element_name" }}

For example, take the following HTML, say it's the beginning of a blog post:

::

 <figure>
   <img src="spam.jpg" alt="Spam pressed onto rice and wrapped in nori." />
   <figcaption>Spam musubi is a popular Hawaiian snack.</figcaption>
 </figure>
 <h1>Just got back from Hawaii</h1>

Contained in an app in such a way that it is accessible in a template as:

::

 {{ blog.post }}

When filtered through ``remel`` to remove the ``<figure>`` element, as in:

::

 {{ blog.post|remel:"figure" }}

Will output:

::

 <h1>Just got back from Hawaii</h1>


strip_querystring Filter
````````````````````````

Removes querystring, e.g. `?spam=eggs` from the end of a URL (or any other string)

Example usage:

::

 <link rel="canonical" href="{{ request.build_absolute_uri|strip_querystring }}" />
