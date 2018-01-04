from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django import template
from django.http import HttpResponse


register = template.Library()

@register.filter(name='multi')
def multiply(x, y):
    # you would need to do any localization of the result here
    result = (float(x)*float(y))
    return result

@register.filter(name='hex')
def convertToHex(x):
    # you would need to do any localization of the result here
    result = hex(int(x))
    return str(result)

@register.filter(name='Hex8')
def convertTohex8(x):
    # you would need to do any localization of the result here
    result = hex(int(x)).format()
    return '0x' + result[2:].zfill(8)
