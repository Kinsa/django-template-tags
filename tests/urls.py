import django

from django.conf.urls import url
from django.views.generic import TemplateView


if django.VERSION < (1, 9):
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        url(
            r'^$', TemplateView.as_view(template_name='home.html'), name='home'
        ),
        url(
            r'^about/$',
            TemplateView.as_view(template_name='about.html'), name='about'
        ),
    )
else:
    urlpatterns = [
        url(
            r'^$', TemplateView.as_view(template_name='home.html'), name='home'
        ),
        url(
            r'^about/$',
            TemplateView.as_view(template_name='about.html'), name='about'
        ),
    ]
