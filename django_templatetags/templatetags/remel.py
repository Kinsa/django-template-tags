from BeautifulSoup import BeautifulSoup

from django.template import Library, TemplateSyntaxError


register = Library()


def remel(value, arg):
	if len(arg.split()) > 1:
		raise TemplateSyntaxError("The 'remel' filter takes exactly one argument, the name of the single HTML element to be removed from the output.")
	def removeEl(soup, elname):
	    for el in soup.findAll(elname):
	        el.extract()

	bs = BeautifulSoup(value)
	removeEl(bs, arg)
	return bs

register.filter(remel)
