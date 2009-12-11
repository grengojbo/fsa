from django.template import Library
#import re

register = Library()

#r_nofollow = re.compile('<a (?![^>]*nofollow)')
#s_nofollow = '<a rel="nofollow" '

def tf(value):
    """
    return true or false
    """
    if (value == 0):
        return "False"
    else:
        return "True"

register.filter(tf)
