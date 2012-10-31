=====================
 Django Template Tags
=====================

Installation from Source
========================

::

 $ git clone git@github.com:jbergantine/django-django-templatetags.git
 $ cd django-django-templatetags
 $ python setup.py install

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following line:

::

 -e git+git://github.com/jbergantine/django-templatetags.git#egg=django_templatetags

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

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

The most basic (and common) use of the tag is to call `{% nav [item] %}`,
where `[item]` is the item you want to check is selected.

By default, this tag creates a `nav` context variable. To use an
alternate context variable name, call `{% nav [item] for [var_name] %}`.

To use this tag across `{% block %}` tags (or other context-stacking
template tags such as `{% for %}`), call the tag without specifying an
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
that the tag only does anything if the `nav` context variable does not
exist. So only the first `{% nav %}` call found will ever be processed.

To create a sub-menu you can check against, dot-separate the item:

::

 {% nav "about_menu.info" %}

This will be pass for both `{% if nav.about_menu %}` and
`{% if nav.about_menu.info %}`.

widont Filter
`````````````

_From: http://djangosnippets.org/snippets/17/_

"Widows" are single words that end up on their own line, thanks to automatic line-breaks. This is an no-no in graphic design, and is especially unsightly in headers and other short bursts of text. This filter automatically replaces the space before the last word of the passed value with a non-breaking space, ensuring there is always at least two words on any given line. Usage is like so:

::

 {{ blog.entry.headline|widont }}
