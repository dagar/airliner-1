# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..toolkit import *
import unittest
import websocket
import urllib
import time
import signal


class Test_Toolkit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        templc = launchConfig()
        cls.lc_obj = templc.get()
        cls.mode = cls.lc_obj['_applicationMode']
        cls.app_path = cls.lc_obj['_applicationPath']
        cls.db_conn = sqlite3.connect(cls.app_path + '/test_database', timeout=5)

    #@unittest.skip("skipping test_dateFormat")
    def test_dateFormat(self):
        self.assertEqual(type(getDate()),str)

    # @unittest.skip("skipping test_directoryScraping")
    def test_directoryScraping(self):
        self.assertEquals(get_directory('')['path'], '')
        self.assertNotEqual(get_directory('/flight')['path'],'/flidfght')
        self.assertEquals(get_directory('/apps/cs')['path'], '/apps/cs')
        self.assertEquals(get_directory('/flight')['path'], '/flight')
        self.assertRaises(OSError, get_directory, '/opt')
        self.assertRaises(OSError, get_directory, '/apps/cs/main.pug')
        self.assertRaises(OSError, get_directory, 'asda')
        self.assertRaises(AttributeError, get_directory, 54)

    #@unittest.skip("skipping test_bitefyUnicodeCorrection")
    def test_bitefyUnicodeCorrection(self):
        self.assertEquals(byteify(24), 24)
        self.assertEquals(byteify('hello'), 'hello')
        self.assertEquals(byteify({u'a':u'b'}), {'a':'b'})
        self.assertEquals(byteify(24), 24)

    # @unittest.skip("skipping launchConfig")
    def test_launchConfig(self):

        with open(self.app_path+'/scripts/launch_config.json') as f:
            config = json.load(f)
            self.assertTrue(self.lc_obj['_localAddress'] == config['pyliner']['address'])
            self.assertTrue(self.lc_obj['_yamcsPort'] == config['pyliner']['port'])
            self.assertTrue(self.lc_obj['_videoPort'] == config['pyliner']['video_port'])
            self.assertTrue(self.lc_obj['_adsbport'] == config['pyliner']['adsb_port'])
            self.assertTrue(self.lc_obj['_defaultInstance'] == config['pyliner']['default_instance'])
            self.assertTrue(self.lc_obj['_daphnePort'] == config['daphne_port'])
            self.assertTrue(self.lc_obj['_numberOfWorkers'] == config['number_of_workers'])
            self.assertTrue(self.lc_obj['_applicationMode'] == config['mode'])
            self.assertTrue(self.lc_obj['_applicationPath'] == config['app_path'])
            self.assertTrue(self.lc_obj['_loggingLevel'] == config['logging_level'])

    #@unittest.skip("skipping text_preprocessing")TODO
    def test_text_preprocessing(self):
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT input, output FROM TESTCASES WHERE mapping =\'PREPROCTLM\'')
        io_list = cursor.fetchall()
        for each in io_list:
            input = each[0]
            output = each[1]
            self.assertEquals(preProcess(input),output)

    @classmethod
    def tearDownClass(cls):
        cls.db_conn.close()


class Test_Instance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        templc = launchConfig()
        cls.lc_obj = templc.get()
        cls.mode = cls.lc_obj['_applicationMode']
        cls.app_path = cls.lc_obj['_applicationPath']
        cls.application_port = cls.lc_obj['_daphnePort']
        cls.db_conn = sqlite3.connect(cls.app_path + '/test_database', timeout=5)

    #@unittest.skip("demonstrating getinstance")
    def test_getinstance(self):
        expected = json.loads(eval(json.dumps(urllib.urlopen('http://127.0.0.1:8090/api/instances').read())))
        ch = channel_plugin('ws://127.0.0.1:'+str(self.application_port)+'/inst/')
        ch.send('INVOKE')
        c_actual = ch.rcv()
        #print expected
        #print c_actual
        self.assertTrue(expected==c_actual)

    @unittest.skip("skipping directoryListing as database is out dated need training.")
    def test_directoryListing(self):
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT input, output FROM TESTCASES WHERE mapping =\'DIR\'')
        io_list = cursor.fetchall()
        for each in io_list:
            input = each[0]
            output = json.loads(byteify(each[1]))
            ch = channel_plugin('ws://localhost:'+str(self.application_port)+'/dir/')
            ch.send(input)
            c_actual = ch.rcv()
            self.assertTrue(len(c_actual['files']) == len(output['files']))
            temp_hold_values = []
            for e in range(len(c_actual['files'])):
                temp_hold_values.append(c_actual['files'][e]['path'])
            temp_hold_values = byteify(temp_hold_values)
            for e in range(len(output['files'])):
                self.assertTrue(output['files'][e]['path'] in temp_hold_values)

    # @unittest.skip("skipping adsb")
    def test_adsb(self):
        ch = channel_plugin('ws://localhost:'+str(self.application_port)+'/adsb/')
        time.sleep(1)
        ch.send('INVOKE')
        c_actual = ch.rcv()
        self.assertTrue(type(c_actual)==list)
        time.sleep(2)
        for e in range(20):
            ch.send('KILL')
        time.sleep(1)
        if ch.rcv() == 'KILLED':
            self.assertTrue(1)
        ch.no_f_rcv()

    # @unittest.skip("skipping adsb")
    def test_vid(self):
        ch = channel_plugin('ws://localhost:'+str(self.application_port)+'/video/')
        time.sleep(1)
        ch.send('INVOKE')
        c_actual = ch.rcv()
        self.assertTrue(type(c_actual)==str)
        time.sleep(2)
        for e in range(20):
            ch.send('KILL')
        time.sleep(1)
        if ch.rcv() == 'KILLED':
            self.assertTrue(1)
        ch.no_f_rcv()





    @classmethod
    def tearDownClass(cls):
        cls.db_conn.close()
"""
class Test_Telemetry(unittest.TestCase):
    @classmethod
    #@unittest.skip("demonstrating skipping")
    def setUpClass(cls):

        cls._r = redis.StrictRedis(host='localhost', port=6379, db=0)
        cls._mode = int(cls._r.get('mode'))
        cls._db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#cls._r.get('app_path')
        cls._number_of_workers = cls._r.get('number_of_workers')
        cls._r.set('instance',cls._r.get('default_instance'))
        cls._conn = sqlite3.connect(cls._db_path + '/test_database', timeout=5)
        cls._ch = channel_plugin('ws://127.0.0.1:8000/tlm_s/')
        cls._sending_list =[]

    @classmethod
    #@unittest.skip("demonstrating skipping")
    def tearDownClass(cls):
        for each in range(int(cls._number_of_workers)):
            cls._ch.send('USALL')
        cls._conn.close()

    #@unittest.skip("demonstrating skipping")
    def test_telemetry_subscription(cls):

        cursor = cls._conn.cursor()
        cursor.execute('SELECT input FROM TESTCASES WHERE mapping =\'SUBTLM\'')
        tlm_list_of_tuples = cursor.fetchall()
        sub_names_sent =[]
        sub_names_recv = []
        c=0
        for e in tlm_list_of_tuples:
            name_sent = byteify(json.loads(byteify(e[0]))['tlm'][0])['name']
            if name_sent not in sub_names_sent:
                c+=1
                cls._ch.send(e[0])
                sub_names_sent.append(name_sent)
            else:
                continue
        while True:
            c_actual = cls._ch.rcv()
            list_of_params = eval(c_actual)['parameter']
            names = [byteify(e['id'])['name'] for e in list_of_params]
            for e in names:
                if e not in sub_names_recv:
                    sub_names_recv.append(e)
            sub_names_sent = list(set(sub_names_sent))
            #for every in sub_names_sent:
                #print '-----------------------------',every
            #for every in sub_names_recv:
                #print every
            #print len(sub_names_recv), '=?',len(sub_names_sent)
            if len(sub_names_sent) == len(sub_names_recv):
                break
        cls.assertTrue(set(sub_names_recv)==set(sub_names_sent))

    #@unittest.skip("demonstrating skipping")
    def test_telemetry_unsubscription(cls): #TODO:Implement this method at client side.

        cursor = cls._conn.cursor()
        cursor.execute('SELECT input FROM TESTCASES WHERE mapping =\'SUBTLM\'')
        tlm_list_of_tuples = cursor.fetchall()
        cls._sending_list = tlm_list_of_tuples
        while len(cls._sending_list)!=0:
            cls.send_unsubscription_signal(cls._sending_list)
            #cls.send_unsubscription_signal(cls._sending_list)
            #cls.send_unsubscription_signal(cls._sending_list)
            result = None
            with timeout(seconds=3):
                try:
                    result = cls._ch.rcv()
                except:
                    pass
            if result!=None:
                list = json.loads(json.dumps(eval(result)))['parameter']
                for e1 in list:
                    name =  e1['id']
                    tlm = '{\'tlm\':['+str(byteify(name))+']}'
                    tlm = (json.dumps(eval(tlm)),)
                    cls._sending_list.append(tlm)
            #print len(cls._sending_list), '=?', 0
        cls.assertTrue(cls._sending_list==[])

    def send_unsubscription_signal(cls,l):
        for e in l:
            for i in range(5):
                cls._ch.send('kill_tlm' + e[0])
            cls._sending_list.remove(e)

class  Test_Commanding(unittest.TestCase):
    @classmethod
    #@unittest.skip("demonstrating skipping")
    def setUpClass(cls):
        cls._r = redis.StrictRedis(host='localhost', port=6379, db=0)
        cls._mode = int(cls._r.get('mode'))
        cls._db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#cls._r.get('app_path')
        cls._number_of_workers = cls._r.get('number_of_workers')
        cls._r.set('instance', cls._r.get('default_instance'))
        cls._conn = sqlite3.connect(cls._db_path + '/test_database', timeout=5)
        cls._ch = channel_plugin('ws://127.0.0.1:8000/cmd_i/')
        cls._ch2 = channel_plugin('ws://127.0.0.1:8000/cmd_s/')
        #cls._sending_list = []

    @classmethod
    #@unittest.skip("demonstrating skipping")
    def tearDownClass(cls):
        cls._conn.close()

    #@unittest.skip("demonstrating skipping")
    def test_get_commanding_info(cls):
        cursor = cls._conn.cursor()
        cursor.execute('SELECT input,output FROM TESTCASES WHERE mapping =\'CMDINFO\'')
        cmd_list_of_tuples = cursor.fetchall()
        for e in cmd_list_of_tuples:
            cls._ch.send(e[0])
            result =  cls._ch.rcv()
            cls.assertEquals(e[1],result)
            cls.assertItemsEqual(e[1], result)

    #@unittest.skip("demonstrating skipping")
    def test_get_commanding_post(cls):
        cursor = cls._conn.cursor()
        cursor.execute('SELECT input,output FROM TESTCASES WHERE mapping =\'CMDPOST\'')
        cmd_list_of_tuples = cursor.fetchall()
        for e in cmd_list_of_tuples:
            cls._ch2.send(e[0])
            result = cls._ch2.rcv()
            #print result
            cls.assertEquals(byteify(e[1]), str(result["code"]))
            cls.assertItemsEqual(byteify(e[1]), str(result["code"]))
"""
# Testing Support Tools
class channel_plugin:
    def __init__(self,url):
        self.ws = websocket.WebSocket()
        self.ws.connect(url,timeout=3)

    def rcv(self):
        result = self.ws.recv()
        try:
            return json.loads(result)
        except:
            return result

    def no_f_rcv(self):
        self.ws.close()
        return None

    def send(self,msg):
        self.ws.send(msg)

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        print ''
        #print 'PROGRAM TIMED OUT!'
        #raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

if __name__ == '__main__':
    Toolkit = unittest.TestLoader().loadTestsFromTestCase(Test_Toolkit)
    INS_DIR = unittest.TestLoader().loadTestsFromTestCase(Test_Instance)
    TLM = unittest.TestLoader().loadTestsFromTestCase(Test_Telemetry)
    CMD = unittest.TestLoader().loadTestsFromTestCase(Test_Commanding)

    Suite = unittest.TestSuite([Toolkit])#,INS_DIR,TLM,CMD])

    slack = '\n\nRunning Tests for Commander....\n\n'
    #print slack
    unittest.TextTestRunner(verbosity=2).run(Suite)
