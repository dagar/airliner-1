import unittest
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
import time
from groundcontrol import toolkit as tk
import unicodedata
import redis
from pprint import pprint
from multiprocessing import Process
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
from StringIO import StringIO

def makeImage(global_img,element):
    location = content.location
    size = content.size
    img1 = Image.open(StringIO(global_img))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    img1 = img1.crop((int(left), int(top), int(right), int(bottom)))
    return img1


binary = FirefoxBinary('/usr/lib/firefox/firefox')
_capabilities = DesiredCapabilities.FIREFOX.copy()
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path="/usr/local/bin/geckodriver.exe")

driver.get('http://127.0.0.1:3000/#view/apps/ci/b_main.pug')
time.sleep(2)
yselec = driver.find_element_by_id('yamcs-instance-selected')
yselec_parent = yselec.find_element_by_xpath('..')
yselec_parent.click()
ul = driver.find_element_by_id('yamcs-instance-list')
a = ul.find_elements_by_tag_name('a')
for each in a:
    if each.text == 'softsim':
        each.click()
        break

def getEventCount():
    event_count = driver.find_element_by_id('EventCount')
    return int(event_count)

def getTlmRow(t):
    #assuming all tlm are placed in tables
    trow = t.find_element_by_xpath('..').find_element_by_xpath('..')
    try:
        th = trow.find_element_by_tag_name('th')
    except:
        th = None
    return [trow,th]

def clean_text(x):
   return  str(x).lower().replace(' ','_')



content = driver.find_element_by_id('content')
articles = content.find_elements_by_tag_name('article')
title = content.find_element_by_xpath(".//h1[@class='page-title txt-color-blueDark']").text
print '-----------------'
print title
print '-----------------\n\n\n'


state_store = {}
state_store[clean_text(title)] = {}

for i  in range(len(articles)):

    header =articles[i].find_element_by_tag_name('header').find_element_by_tag_name('h2').text
    state_store[clean_text(title)][clean_text(header)]={'tlm_unbound':{}}
    tlm=articles[i].find_elements_by_xpath('.//span[@data-sage]')
    cmd=articles[i].find_elements_by_xpath('.//button[@data-sage]')



    print '\t\t',header

    for each in tlm:

        tarr = getTlmRow(each)
        tval = each.text
        if tarr[1]!=None:
            thead = tarr[1].text
            #print tval, '      ', thead
            state_store[clean_text(title)][clean_text(header)]['tlm_unbound'][thead]=tval



    print '_______________________\n\n\n'

pprint(state_store)


"""
realtime = []
button_invoked=[]
semi_stationary = []
temp ={}
for e in range(len(tlm)):
    temp[e] = tlm[e].text


for e1 in range(len(cmd)):
    cmd[e1].click()
    time.sleep(3)
    for e2 in range(len(tlm)):
        if temp[e2]==tlm[e2].text:
            print temp[e2],'no change'
        else:
            print temp[e2],'change'
    for e3 in range(len(tlm)):
        temp[e3] = tlm[e3].text

driver.quit()
"""
driver.quit()