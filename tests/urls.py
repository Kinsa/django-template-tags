import django

from django.urls import re_path
from django.views.generic import TemplateView


if django.VERSION < (1, 9):
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        url(
            r'^$', TemplateView.as_view(template_name='home.html'), 
            name='home'
        ),
        url(
            r'^about/$',
            TemplateView.as_view(template_name='about.html'), 
            name='about'
        ),
        url(
            r'^strip-querystring-test/$',
            TemplateView.as_view(template_name='strip_querystring_filter_test_template.html'), 
            name='strip-querystring-test'
        ),
    )
else:
    urlpatterns = [
        re_path(
            r'^$', TemplateView.as_view(template_name='home.html'), 
            name='home'
        ),
        re_path(
            r'^about/$',
            TemplateView.as_view(template_name='about.html'), 
            name='about'
        ),
        re_path(
            r'^strip-querystring-test/$',
            TemplateView.as_view(template_name='strip_querystring_filter_test_template.html'), 
            name='strip-querystring-test'
        ),
    ]