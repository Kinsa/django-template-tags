import re

from django import template


register = template.Library()

@register.filter(name='dumbquotes')
def dumbquotes(text):
    text = re.sub(r'(&ldquo;|&\#8220;|&rdquo;|&\#8221;)', '"', text)
    text = re.sub(r'(&lsquo;|&\#8216;|&rsquo;|&\#8217;)', "'", text)
    return text

@register.filter(name='dumbpunct')
def dumbpunct(text):
    text = re.sub(r'(&hellip;|&\#8230;)', '...', text)
    text = re.sub(r'(&amp;|&\#0038;|&\#038;|&\#38;)', "&", text)
    text = re.sub(r'(&mdash;|&\#8212;)', "---", text)
    text = re.sub(r'(&ndash;|&\#8211;)', "--", text)
    text = re.sub(r'(&nbsp;|&\#0160;|&\#160;)', " ", text)
    return text
