import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
import time
from .. import toolkit as tk
import unicodedata
import redis
import json
from pprint import pprint
from multiprocessing import Process
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities








class ApplicationGUI(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.binary = FirefoxBinary('/usr/lib/firefox/firefox')
        cls._capabilities = DesiredCapabilities.FIREFOX.copy()
        cls.cap = DesiredCapabilities().FIREFOX
        cls.cap["marionette"] = False



        #cls._r = redis.StrictRedis(host='localhost', port=6379, db=0)
        #cls._db_path = cls._r.get('app_path')
        cls.apps = []
        cls.fixApps = {}
        cls.totalApps = 0
        cls.validApps = 0
        cls.bigj={}
    #@classmethod
    #def tearDownClass(cls):
        #cls.driver.quit()



    def setUp(self):
        self.driver = webdriver.Firefox(capabilities=self.cap, executable_path="/usr/local/bin/geckodriver.exe")
        self.driver.get('http://127.0.0.1:3000')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        time.sleep(1)



    @unittest.skip("demonstrating skipping")
    def test_A_hosting(self):
        title = unicodedata.normalize("NFKD", self.driver.title)
        self.assertEqual(title,'flight  /  pilot.jade')

    @unittest.skip("demonstrating skipping")
    def test_B_directory_listing_superficial(self):
        aside = self.driver.find_element_by_id('left-panel')
        navbox = aside.find_element_by_id('navBox')
        ul =  navbox.find_element_by_class_name('jarvis-menu-applied')
        list = ul.find_elements_by_tag_name('a')
        list2 = []
        for each in tk.get_directory('')['files']:
            list2.append(each['name'])
        for each in list:
            span = each.find_element_by_tag_name('span')
            #print span
            self.assertTrue(span.text in list2)

    def test_C_app_directory_listing_click_sample(self):
        aside = self.driver.find_element_by_id('left-panel')
        navbox = aside.find_element_by_id('navBox')
        ul = navbox.find_element_by_class_name('jarvis-menu-applied')
        list = ul.find_elements_by_tag_name('li')
        for each in list:
            lookup = each.find_element_by_tag_name('a').get_attribute('onclick')
            half_lookup = lookup.replace('session.getDirectoryListing(\'', '').replace('\', procDirectoryListing);', '')
            if half_lookup == '/apps':
                each.find_element_by_tag_name('a').click()
                time.sleep(1)
                ul = each.find_element_by_class_name('jarvis-menu-applied')
                ls = ul.find_elements_by_tag_name('li')
                ls = ls[1:(len(ls) / 4)-3]
                self.freeClicks(ls)
                time.sleep(1)

    @unittest.skip("demonstrating skipping")
    def test_C_app_directory_listing_click_partA(self):
        aside = self.driver.find_element_by_id('left-panel')
        navbox = aside.find_element_by_id('navBox')
        ul = navbox.find_element_by_class_name('jarvis-menu-applied')
        list = ul.find_elements_by_tag_name('li')
        for each in list:
            lookup = each.find_element_by_tag_name('a').get_attribute('onclick')
            half_lookup = lookup.replace('session.getDirectoryListing(\'', '').replace('\', procDirectoryListing);', '')
            if half_lookup =='/apps':
                each.find_element_by_tag_name('a').click()
                time.sleep(1)
                ul = each.find_element_by_class_name('jarvis-menu-applied')
                ls = ul.find_elements_by_tag_name('li')
                ls = ls[0:len(ls)/2]
                self.freeClicks(ls)
                time.sleep(1)

    @unittest.skip("demonstrating skipping")
    def test_C_app_directory_listing_click_partB(self):
        aside = self.driver.find_element_by_id('left-panel')
        navbox = aside.find_element_by_id('navBox')
        ul = navbox.find_element_by_class_name('jarvis-menu-applied')
        list = ul.find_elements_by_tag_name('li')
        for each in list:
            lookup = each.find_element_by_tag_name('a').get_attribute('onclick')
            half_lookup = lookup.replace('session.getDirectoryListing(\'', '').replace('\', procDirectoryListing);', '')
            if half_lookup =='/apps':
                each.find_element_by_tag_name('a').click()
                time.sleep(1)
                ul = each.find_element_by_class_name('jarvis-menu-applied')
                ls = ul.find_elements_by_tag_name('li')
                ls = ls[len(ls)/2:len(ls)]
                self.freeClicks(ls)
                time.sleep(1)

    @unittest.skip("demonstrating skipping")
    def test_D_recursive_clicks_on_applications(self):
        aside = self.driver.find_element_by_id('left-panel')
        navbox = aside.find_element_by_id('navBox')
        ul =  navbox.find_element_by_class_name('jarvis-menu-applied')
        list = ul.find_elements_by_tag_name('li')
        for each in list:
            lookup = each.find_element_by_tag_name('a').get_attribute('onclick')
            half_lookup = lookup.replace('session.getDirectoryListing(\'', '').replace('\', procDirectoryListing);', '')
            if half_lookup != '/apps':
                each.find_element_by_tag_name('a').click()
                time.sleep(1)
                ul = each.find_element_by_class_name('jarvis-menu-applied')
                ls = ul.find_elements_by_tag_name('li')
                self.freeClicks(ls)

    def freeClicks(self,list):
        for each in list:

            if  each.find_element_by_tag_name('a').get_attribute('href')!='http://127.0.0.1:3000/#':
                #print each.find_element_by_tag_name('a').get_attribute('href')
                ApplicationGUI.totalApps = ApplicationGUI.totalApps +  1
                slug = each.find_element_by_tag_name('a').get_attribute('href')
                try:
                    res = requests.get(slug)
                    #print res
                except:
                    pass
                if res.reason == 'OK' :
                    ApplicationGUI.validApps = ApplicationGUI.validApps + 1
                    self.apps.append(self.largen(slug))
                else:
                    self.fixApps[self.largen(slug)] = {'code':res.status_code,'err':res.reason}

                if list.index(each) == len(list)-1:
                    return
                else:
                    continue

            lookup = each.find_element_by_tag_name('a').get_attribute('onclick')
            half_lookup = lookup.replace('session.getDirectoryListing(\'', '').replace('\', procDirectoryListing);', '')
            op = tk.get_directory(half_lookup)
            #print half_lookup
            self.assertTrue(op['err']==None)
            self.assertTrue(tk.byteify(op['path'])==half_lookup)
            each.find_element_by_tag_name('a').click()
            time.sleep(1)
            ul = each.find_element_by_class_name('jarvis-menu-applied')
            ls = ul.find_elements_by_tag_name('li')
            # retry
            if len(ls)==0:
                each.find_element_by_tag_name('a').click()
                each.find_element_by_tag_name('a').click()
                time.sleep(10)
                ul = each.find_element_by_class_name('jarvis-menu-applied')
                ls = ul.find_elements_by_tag_name('li')
                if len(ls) == 0:
                    time.sleep(50)
                    ul = each.find_element_by_class_name('jarvis-menu-applied')
                    ls = ul.find_elements_by_tag_name('li')
            #print ls
            self.freeClicks(ls)
            time.sleep(2)

    @unittest.skip("demonstrating skipping")
    def test_E_instance_in_list(self):
        time.sleep(1)
        yis = self.driver.find_element_by_id('yamcs-instance-selected')
        self.assertTrue(yis.text=='Select')
        yis.click()
        ul = self.driver.find_element_by_id('yamcs-instance-list')
        a = ul.find_elements_by_tag_name('a')
        name_list = []
        for each in a:
            name_list.append(each.text)
        self.assertTrue('softsim' in name_list)


    def largen(self,link):
            parts = link.split(':3000')
            new_url = parts[0]+':3000/#'+parts[1]
            return new_url

    def nano(self,link):
        parts = link.split(':3000')
        return parts[1]

    def clean_nano(self,link):
        parts = link.split(':3000/#/')
        slugs = parts[1].split('/')
        name =''
        last = slugs[len(slugs)-1].split('.')
        last = last[0]
        for each in slugs[:len(slugs)-2]:
            name = name +'_'+str(each)
        name = name +'_'+last
        return name

    def tlm_nano(self,link):
        parts = link.split(':3000')
        names = parts[1]

    def getTlmRow(self,t):
        # assuming all tlm are placed in tables
        trow = t.find_element_by_xpath('..').find_element_by_xpath('..')
        try:
            th = trow.find_element_by_tag_name('th')
        except:
            th = None
        return [trow, th]

    def getEventCount(self):
        event_count = self.driver.find_element_by_id('EventCount').text
        return int(event_count)

    def clean_text(self,x):
        return str(x).lower().replace(' ', '_')

    @unittest.skip("demonstrating skipping")
    def test_F_select_instance(self):
        ul = self.driver.find_element_by_id('yamcs-instance-list')
        a = ul.find_elements_by_tag_name('a')

        for each in a:
            if each.text == 'softsim':
                each.click()
                break
        yis = self.driver.find_element_by_id('yamcs-instance-selected')
        self.assertTrue(yis.text == 'softsim')
        print  'apps : ',self.apps
        print  'fixapps : ',self.fixApps
        print  'totalapps : ',self.totalApps
        print  'validapps : ',self.validApps
        #time.sleep(5)
        #self.driver.implicitly_wait(3)
    def catpture_ubound_tlm(self):
        d = webdriver.Firefox(capabilities=self.cap, executable_path="/usr/local/bin/geckodriver.exe")
        d.get('http://127.0.0.1:3000')
        time.sleep(1)
        for each_app in self.apps:
            d.get(each_app)
            time.sleep(2)
            # before bind
            content = d.find_element_by_id('content')
            articles = content.find_elements_by_tag_name('article')
            title = self.clean_text(content.find_element_by_xpath(".//h1[@class='page-title txt-color-blueDark']").text)
            self.bigj[title]={}
            for i in range(len(articles)):
                try:
                    header = self.clean_text(articles[i].find_element_by_tag_name('header').find_element_by_tag_name('h2').text)
                    self.bigj[title][header] = {'before-bound':{},'after-bound':{},'cmd':{}}
                    tlm = articles[i].find_elements_by_xpath('.//span[@data-sage]')
                    for each in tlm:
                        tarr = self.getTlmRow(each)
                        tval = each.text
                        if tarr[1] != None:
                            thead = tarr[1].text
                            self.bigj[title][header]['before-bound'][thead] = tval
                except:
                    pass
        d.quit()
        time.sleep(1)

    #@unittest.skip("demonstrating skipping")
    def test_G_application_binding_tlm(self):
        self.catpture_ubound_tlm()
        yselec = self.driver.find_element_by_id('yamcs-instance-selected')
        yselec_parent = yselec.find_element_by_xpath('..')
        yselec_parent.click()
        ul = self.driver.find_element_by_id('yamcs-instance-list')
        a = ul.find_elements_by_tag_name('a')
        for each in a:
            if each.text == 'softsim':
                each.click()
                break
        time.sleep(5)
        for each_app in self.apps:
            self.driver.get(each_app)
            time.sleep(2)
            # after bind
            content = self.driver.find_element_by_id('content')
            articles = content.find_elements_by_tag_name('article')
            title = self.clean_text(content.find_element_by_xpath(".//h1[@class='page-title txt-color-blueDark']").text)
            passed_tlm_count = 0.0
            passed_cmd_count = 0.0
            total_tlm_count = 0.0
            total_cmd_count = 0.0
            bcount = 0.0
            total = 0.0
            for i in range(len(articles)):
                loc_passed_tlm_count = 0.0
                loc_passed_cmd_count = 0.0
                loc_total_tlm_count = 0.0
                loc_total_cmd_count = 0.0
                try:
                    #count = 0.0
                    header = self.clean_text(articles[i].find_element_by_tag_name('header').find_element_by_tag_name('h2').text)
                    cmd = articles[i].find_elements_by_xpath('.//button[@data-sage]')
                    tlm = articles[i].find_elements_by_xpath('.//span[@data-sage]')

                    for each in tlm:
                        try:
                            tarr = self.getTlmRow(each)
                            tval = each.text
                            if tarr[1] != None:
                                thead = tarr[1].text
                                if str(self.bigj[title][header]['before-bound'][thead])!=str(tval):
                                    loc_passed_tlm_count = loc_passed_tlm_count + 1
                                    passed_tlm_count = passed_tlm_count + 1
                                self.bigj[title][header]['after-bound'][thead] = str(tval)
                                loc_total_tlm_count = loc_total_tlm_count + 1
                                total_tlm_count = total_tlm_count + 1
                        except Exception, err:
                            #print err
                            pass

                    for each in cmd:
                        try:
                            context = each.get_attribute("data-sage")
                            context = json.loads(tk.byteify(context))
                            name = context['cmd']['name']
                            uuid = context['cmd']['uuid']
                            prev_event_count = self.getEventCount()
                            each.click()
                            each.click()
                            time.sleep(3)
                            work = 0



                            if self.getEventCount() > prev_event_count:
                                #print self.getEventCount(), ' > ', prev_event_count
                                self.bigj[title][header]['cmd'][uuid] = {'name': name, 'works': 1}
                                work = 1
                                loc_passed_cmd_count = loc_passed_cmd_count + 1
                                passed_cmd_count = passed_cmd_count + 1
                            else:
                                self.bigj[title][header]['cmd'][uuid] = {'name': name, 'works': 0}

                            for t in tlm:
                                tarr = self.getTlmRow(each)
                                tval = each.text
                                if tarr[1] != None:
                                    thead = tarr[1].text
                                    if self.bigj[title][header]['after-bound'][thead] != tval and self.bigj[title][header]['before-bound'][thead] == self.bigj[title][header]['after-bound'][thead]:
                                        #loc_passed_tlm_count = loc_passed_tlm_count + 1
                                        #passed_tlm_count = passed_tlm_count + 1
                                        if work != 1:
                                            self.bigj[title][header]['cmd'][uuid] = {'name': name, 'works': 1}
                                            work = 1
                                            loc_passed_cmd_count = loc_passed_cmd_count + 1
                                            passed_cmd_count = passed_cmd_count + 1
                                    else:
                                        self.bigj[title][header]['cmd'][uuid] = {'name': name, 'works': 0}

                            total_cmd_count = total_cmd_count +1
                            loc_total_cmd_count = loc_total_cmd_count + 1
                        except Exception, err:
                            #print err
                            pass




                    if loc_total_cmd_count==0 :
                        loc_passed_tlm_count=-1
                        loc_total_cmd_count=1
                    if loc_total_tlm_count==0:
                        loc_passed_cmd_count=-1
                        loc_total_tlm_count=1

                    self.bigj[title][header]['tlm-success-rate'] = loc_passed_tlm_count / loc_total_tlm_count  # float(count)/float(len(self.bigj[title][header]['before-bound'].keys()))
                    self.bigj[title][header]['passed-tlm'] = loc_passed_tlm_count
                    self.bigj[title][header]['total-tlm'] = loc_total_tlm_count
                    self.bigj[title][header]['cmd-success-rate'] = loc_passed_cmd_count / loc_total_cmd_count  # float(count)/float(len(self.bigj[title][header]['before-bound'].keys()))
                    self.bigj[title][header]['passed-cmd'] = loc_passed_cmd_count
                    self.bigj[title][header]['total-cmd'] = loc_total_cmd_count

                except Exception,err:
                    print err
                    pass
            if total_cmd_count == 0:
                total_cmd_count = 1
                passed_cmd_count= -1
                passed_tlm_count= -1
                total_tlm_count= 1
            if total_tlm_count == 0:
                total_cmd_count = 1
                passed_cmd_count = -1
                passed_tlm_count = -1
                total_tlm_count = 1
            self.bigj[title]['passed-tlm'] = passed_tlm_count
            self.bigj[title]['total-tlm'] = total_tlm_count
            self.bigj[title]['passed-cmd'] = passed_cmd_count
            self.bigj[title]['total-cmd'] = total_cmd_count
            self.bigj[title]['appscore'] = (passed_tlm_count+passed_cmd_count)/(total_cmd_count+total_tlm_count)


        pprint(tk.byteify(self.bigj))

    @unittest.skip("demonstrating skipping")
    def test_H_application_buttons_test(self):
        yselec = self.driver.find_element_by_id('yamcs-instance-selected')
        yselec_parent = yselec.find_element_by_xpath('..')
        yselec_parent.click()
        ul = self.driver.find_element_by_id('yamcs-instance-list')
        a = ul.find_elements_by_tag_name('a')
        for each in a:
            if each.text == 'softsim':
                each.click()
                break
        time.sleep(5)
        for each_app in self.apps:
            self.driver.get(each_app)
            time.sleep(5)
            # before bind
            content = self.driver.find_element_by_id('content')
            articles = content.find_elements_by_tag_name('article')
            title = self.clean_text(content.find_element_by_xpath(".//h1[@class='page-title txt-color-blueDark']").text)
            bcount = 0.0

            for i in range(len(articles)):
                try:
                    total = 0.0
                    b_count = 0.0

                    header = self.clean_text(articles[i].find_element_by_tag_name('header').find_element_by_tag_name('h2').text)
                    self.bigj[title][header]['cmds'] = {}
                    cmd = articles[i].find_elements_by_xpath('.//button[@data-sage]')
                    tlm = articles[i].find_elements_by_xpath('.//span[@data-sage]')
                    for each in cmd:
                        context = each.get_attribute("data-sage")
                        context = json.loads(tk.byteify(context))
                        #try:
                            #arg = context['cmd']['argument']
                            #continue
                        #except:
                            #pass
                        total = total +1
                        name = context['cmd']['name']
                        uuid = context['cmd']['uuid']
                        self.bigj[title][header]['cmds'][uuid] = {'name': name, 'works': 0}
                        prev_event_count = getEventCount()
                        each.click()
                        time.sleep(2)
                        works = 0

                        if getEventCount()>prev_event_count:
                            works = 1
                            self.bigj[title][header]['cmds'][uuid]['works']=1
                            b_count = b_count+1

                        count = 0.0
                        for t in tlm:
                            tarr = self.getTlmRow(each)
                            tval = each.text
                            if tarr[1] != None:
                                thead = tarr[1].text
                                if self.bigj[title][header]['after-bound'][thead] != tval and self.bigj[title][header]['before-bound'][thead] == self.bigj[title][header]['after-bound'][thead]:
                                    count = count + 1
                                    bcount = bcount +1
                                    if not work:
                                        self.bigj[title][header]['cmds'][uuid]['works'] = 1
                                        b_count = b_count + 1
                        self.bigj[title][header]['count']= self.bigj[title][header]['count']+ count
                        self.bigj[title][header]['bperc']= float(self.bigj[title][header]['count'])/float(len(self.bigj[title][header]['before-bound'].keys()))
                        print name, '  ', self.bigj[title][header]['count'], '    ', self.bigj[title][header]['bperc']
                    self.bigj[title][header]['b_count'] = b_count
                    self.bigj[title][header]['btnperc']= float(b_count)/float(total)

                except:
                    pass
                self.bigj[title]['count'] = self.bigj[title]['count'] + bcount
                self.bigj[title]['app_score'] = bcount / self.bigj[title]['total']



                        #tarr = self.getTlmRow(each)
                        #tval = each.text
                        #if tarr[1] != None:
                            #thead = tarr[1].text
                            #print self.bigj[title][header]['before-bound'][thead],' -- ',tval
                            #if str(self.bigj[title][header]['before-bound'][thead])!=str(tval):
                                #count = count + 1
                                #bcount = bcount + 1
                                #print count
                            #self.bigj[title][header]['after-bound'][thead] = tval
                            #print tval, '      ', thead
                    #self.bigj[title][header]['bperc']=float(count)/float(len(self.bigj[title][header]['before-bound'].keys()))
                    #total = total + float(len(self.bigj[title][header]['before-bound'].keys()))
                #except:
                    #pass
                #self.bigj[title]['app_score']=bcount/total

            pprint(tk.byteify(self.bigj))





    @unittest.skip("demonstrating skipping")
    def get_event_count(self):
        return int(self.driver.find_element_by_xpath('//b[@id=\'EventCount\']').text)

    def print_resources(self):
        print 'TOTAL APPS #  ',ApplicationGUI.totalApps
        print 'VALID APPS #  ',ApplicationGUI.validApps

    #def test_G_verify_telemetry(self):




if __name__ == '__main__':
    GUI = unittest.TestLoader().loadTestsFromTestCase(ApplicationGUI)
    Suite = unittest.TestSuite([GUI])
    unittest.TextTestRunner(verbosity=2).run(Suite)




