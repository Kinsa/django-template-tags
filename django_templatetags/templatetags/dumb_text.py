import re

from django import template


register = template.Library()


@register.filter(name='dumbquotes')
def dumbquotes(text):
    text = re.sub(r'(&ldquo;|&\#8220;|&rdquo;|&\#8221;)', r'"', text)
    text = re.sub(r'(&lsquo;|&\#8216;|&rsquo;|&\#8217;)', r"'", text)
    return text


@register.filter(name='dumbpunct')
def dumbpunct(text):
    text = re.sub(r'(&hellip;|&\#8230;)', r'...', text)
    text = re.sub(r'(&amp;|&\#0038;|&\#038;|&\#38;)', r"&", text)
    text = re.sub(r'(&mdash;|&\#8212;)', r"---", text)
    text = re.sub(r'(&ndash;|&\#8211;)', r"--", text)
    text = re.sub(r'(&nbsp;|&\#0160;|&\#160;)', r" ", text)
    return text
