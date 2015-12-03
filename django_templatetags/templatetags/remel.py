from bs4 import BeautifulSoup
from django.template import Library, TemplateSyntaxError


register = Library()


def remel(value, arg):
    if len(arg.split()) > 1:
        raise TemplateSyntaxError(
            "The 'remel' filter takes exactly one argument, "
            "the name of the single HTML element to be removed from the output."
        )

    def remove_element(soup, elname):
        for el in soup.findAll(elname):
            el.extract()

    bs = BeautifulSoup(value)

    remove_element(bs, arg)

    return bs

register.filter(remel)
