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

 -e git://github.com/jbergantine/django-templatetags.git#egg=django_templatetags

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt

Configure the Project To Include the Application
================================================

Add to the project's settings.py file tuple of installed apps: ::

 'django_templatetags',