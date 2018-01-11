"""Views.py
the url.py file filters and routes a url to one of the functions in this module. These functions determine the reqested page
and sends a page in response.

Since we are dealing with jade/pug template files these files are compiled and generate HTML which are sent over the network.

Todo:
    * Only identify and serve files compatible inside django framework.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from toolkit import readJsonFromCloseCirlce
from logger import *


def index(r,a=None):
    """!
    Serves various files like pug and js.
    @param r: param 1
    @param a: param 2
    @return: Rendered Response
    """

    if a==None:
        logi('Requested index.pug')
        try:
            return render(r,'index.pug')
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'index.pug\'. Error: %s', err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err
            return HttpResponse(html)
    elif a.find('.js')!=-1:
        logi('Requested %s', str(a))
        try:
            return render(r, str(a))
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'%s.js\'. Error: %s', a, err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err
            return HttpResponse(html)
    else:
        logi('Requested %s', str(a + '.pug'))
        try:
            return render(r, str(a+'.pug'))
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'%s.pug\'. Error: %s',a,err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err 
            return HttpResponse(html)


def router(r,a,b,c=None,d=None):
    """!
    Serves various files like pug and js.
    @param r: param 1
    @param a: param 2
    @param b: param 3
    @param c: param 4
    @param d: param 5
    @return: Rendered Response
    """
    if c==None and d==None:
        try:
            json = readJsonFromCloseCirlce(str(a))
        except:
            json = 'NULL'
        logi('Requested %s', str(a + '/' + b + '.pug'))
        try:
            return render(r, str(a+'/'+b+'.pug'),{'obj':json})
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'%s\'. Error: %s', str(a+'/'+b+'.pug'), err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err
            return HttpResponse(html)


    elif d==None:
        try:
            json = readJsonFromCloseCirlce(str(a+'/'+b+'/'))
        except:
            json = 'NULL'
        logi('Requested %s', str(a + '/' + b + '/' + c + '.pug'))
        try:
            return render(r, str(a+'/'+b+'/'+c+'.pug'),{'obj':json})
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'%s\'. Error: %s',str(a+'/'+b+'/'+c+'.pug'),err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err
            return HttpResponse(html)

    else:
        try:
            json = readJsonFromCloseCirlce(str(a+'/'+b+'/'+c+'/'))
        except:
            json = 'NULL'
        logi('Requested %s', str(a + '/' + b + '/' + c + '/' + d + '.pug'))
        try:
            return render(r, str(a +'/'+b+'/'+c+'/'+d+ '.pug'),{'obj':json})
        except Exception, err:
            logw('Did not render requested file \'%s.pug\'.')
            logw('Insight on file \'%s\'. Error: %s', str(a +'/'+b+'/'+c+'/'+d+ '.pug'), err)
            html = "<html><body>Error Log: <br/> %s </body></html>" % err
            return HttpResponse(html)


def pug_router(r,a,b,c=None,d=None):
    """
     Serves various files like pug and js.
    @param r: param 1
    @param a: param 2
    @param b: param 3
    @param c: param 4
    @param d: param 5
    @return: Rendered Response
    """
    if c==None and d==None:
        return render(r, str(a+'/'+b))
    elif d==None:
        return render(r, str(a+'/'+b+'/'+c))
    else:
        return render(r, str(a +'/'+b+'/'+c+'/'+d))
