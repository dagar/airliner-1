"""Consumer.py is the final destination of all websocket routing that happens in django. Each incoming message is picked
up by one of the several workers and gets routed to respective function call in this file. The worker executes the function
passing the message as parameter. The response is written in the received message itself and put back on the channel/socket.
"""

## swiss-knife
import toolkit as tk
from logger import *
import urllib,json,os,psutil,requests,time,socket,base64,ast
from django.core.cache import cache
from channels import Group
from channels.generic import BaseConsumer
from channels.sessions import channel_session
from websocket import create_connection
from multiprocessing import Process
from pprint import pprint
import inspect
import time,random,redis_lock
from static.proto import web_pb2,pvalue_pb2
## datastores
import redis,sqlite3
import sys

reload(sys)
sys.setdefaultencoding('utf8')

redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)## Initialize redis caching database

mode = 2#int(redis_cache.get('mode'))## Initialize mode defined in launch_config.json
app_path = redis_cache.get('app_path')## Initialize test database path defined in launch_config.json
number_of_workers = redis_cache.get('number_of_workers')## Initialize number or parallel workers defined in launch_config.json
defaultInstance= 'softsim'#redis_cache.get('default_instance')## Initialize default instance defined in launch_config.json
address = '127.0.0.1'#redis_cache.get('address')## Initialize address to pyliner/yamcs defined in launch_config.json
port = 8090#redis_cache.get('port')## Initialize port to pyliner/yamcs defined in launch_config.json
video_socket = None## An empty variable which will be later used to store the video-udp socket object.
video_port = 3001#int(redis_cache.get('video_port'))## Initialize video port to pyliner/yamcs defined in launch_config.json.
adsb_port =8080
sock_map = {}## A dictionary to store websockets which connect backend, mapped with unique id in message object.
proc_map = {}## A dictionary to store processes which push telemetry to frontend, mapped with unique id in message object.
test_sampling_frequency = (1.0/10)## The number of samples collected everytime the `push` function yields data
sock_map_e = {}## A dictionary to store websockets which connect backend, mapped with unique id in message object.
proc_map_e = {}## A dictionary to store processes which push telemetry to frontend, mapped with unique id in message object.
adsb_proc = []
vid_proc = []



class session_maintainance(BaseConsumer):
    sock_map = {}  ## A dictionary to store websockets which connect backend, mapped with unique id in message object.
    proc_map = {}  ## A dictionary to store processes which push telemetry to frontend, mapped with unique id in message object.
    inst =[]
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    channel_session = True
    method_mapping = {
        u'websocket.connect': "connect",
        u'websocket.disconnect': "disconnect",
        u'websocket.receive': "recv_handle",
    }

    def connect(self,message):
        message.reply_channel.send({'accept': True})
        logi('Connected to session maintainance instance.')

    def disconnect(self,message):
        my_instance = str(message.channel_session['instance'])
        Group(my_instance).discard(message.reply_channel)
        message.reply_channel.send({'close': True})

    def recv_handle(self,message):
        client_reply_channel = message.content['reply_channel']
        obj = tk.byteify(json.loads(message.content['text']))
        if  obj['op'] == 'bind_instance':
            # check if client is already in the broadcast group
            if client_reply_channel not in Group(obj['msg']).channel_layer.group_channels(obj['msg']):
                message.channel_session['instance'] = obj['msg']
                Group(obj['msg']).add(message.reply_channel)
                logd('client %s has been added to broadcast group of %s.',client_reply_channel,obj['msg'])
            else:
                logw('Client %s already bound to broadcast group %s',client_reply_channel,obj['msg'])
        elif obj['op'] == 'subscribe_tlm' :
            tlm_obj = json.loads(obj['msg'])
            tlm_slug = str(tlm_obj['tlm'][0]['name'])
            my_instance = str(message.channel_session['instance'])
            #with redis_lock.Lock(self.r, 'mylock1'):

                #if my_instance not in self.r.keys():
                    #self.r.set(my_instance,'{}')#initialize k:tlm_slug v:array of listeners
                #loc_cache = json.loads(self.r.get(my_instance))
                #print loc_cache
                #if tlm_slug not in loc_cache.keys():
                    #loc_cache[tlm_slug] = [client_reply_channel]#initialize k:tlm_slug v:array of listeners
                    #print 'cached', tlm_slug ,len(loc_cache)
                    #pprint (loc_cache)
                    #print self.inst,len(self.inst)
                    #self.r.set(my_instance, json.dumps(loc_cache))

            psr = web_pb2.ParameterSubscriptionRequest()
            id = psr.id.add()
            id.name = str(tk.byteify(tlm_obj['tlm'][0]['name']))
            #sr = pvalue_pb2.ParameterValue()
            wscm = web_pb2.WebSocketClientMessage()
            wscm.protocolVersion = 1
            wscm.sequenceNumber = 0
            wscm.resource = "parameter"
            wscm.operation = "subscribe"
            wscm.data = psr.SerializeToString()
            #id = sr.id.add()

            #psr.data = sr.SerializeToString()
            #temp = '{"parameter":"subscribe", "data":{"list":' + str(tk.byteify(tlm_obj['tlm'])) + '}}'
            #temp = temp.replace("\'", "\"")
            #to_send = '[1,1,0,' + str(temp) + ']'
            if client_reply_channel not in sock_map.keys():
                try:
                    ws = create_connection('ws://' + str(address) + ':' + str(port) + '/' + my_instance + '/_websocket')
                    sock_map[client_reply_channel] = ws
                    sock_map[client_reply_channel].send_binary(wscm.SerializeToString())
                    #sock_map[client_reply_channel].send(to_send)
                    process = Process(target=self.push,args=(sock_map[client_reply_channel],my_instance,client_reply_channel))
                    process.start()
                    proc_map[client_reply_channel] = process.pid
                    logd('New push process has been created with pid %s.',str(process.pid))
                except Exception, err:
                    loge('Encountered error while creating a process. Error: %s',err)
                    pass
            else:
                try:
                    sock_map[client_reply_channel].send_binary(wscm.SerializeToString())
                    logd('Client %s is now [SUBSCRIBE] to %s bound to instance %s',client_reply_channel,obj['msg'],message.channel_session['instance'])
                except Exception, err:
                    ## TODO: safely log error, unit test required
                    loge('[SUBSCRIBE] error occured for client %s on item %s for instance %s. Error: %s',client_reply_channel,obj['msg'],message.channel_session['instance'],err)
                    pass
                #else:

                    #loc_cache[tlm_slug].append(client_reply_channel)
                    #pprint(loc_cache)
                    #c = 1
                    #for e in loc_cache.keys():
                        #if len(loc_cache[e])==2:
                            #c+=1
                    #print c
                    #print 'missing',tlm_slug
                    #self.r.set(my_instance, json.dumps(loc_cache))
                    #time.sleep(random.randint(1, 5) / 100)

                #print '******',deserialized[my_instance][tlm_slug], len(deserialized[my_instance][tlm_slug])
                #self.r.set('activeSubscriptions', json.dumps(deserialized))
                #self.r.set('activeSubscriptions', json.dumps(deserialized))
                #self.r.set('activeSubscriptions', json.dumps(deserialized))
                #logw('No need SUBSCRIBE for client %s on item %s for instance %s',client_reply_channel,obj['msg'],message.channel_session['instance'])
        elif obj['op'] == 'unsubscribe_tlm':
            my_instance = str(message.channel_session['instance'])
            tlm_obj = json.loads(obj['msg'])
            tlm_slug = str(tlm_obj['tlm'][0]['name'])
            #my_instance = str(message.channel_session['instance'])
            #with redis_lock.Lock(self.r, 'mylock2'):
            # remove listener
            #pprint(deserialized)
            #pprint(deserialized)
            #pprint(deserialized)
            #pprint(deserialized)
            try:
                temp = '{"parameter":"unsubscribe", "data":{"list":' + str(tk.byteify(tlm_obj['tlm'])) + '}}'
                temp = temp.replace("\'", "\"")
                to_send = '[1,1,0,' + str(temp) + ']'
                #print tlm_slug,'----us--', deserialized[my_instance][tlm_slug]
                ## sending unsubscribe signal to pyliner/yamcs
                #for each in sock_map.keys():
                sock_map[client_reply_channel].send(to_send)
                logw('[UNSUBSCRIBE] attempt made for client %s on item %s for instance %s.',client_reply_channel, obj['msg'], message.channel_session['instance'])
                #self.r.set(my_instance, json.dumps(loc_cache))
            except Exception, err:
                #print 'attempt-remove [', tlm_slug, client_reply_channel, ']'
                #pprint(deserialized)
                #print len(deserialized[my_instance].keys())
                logw('Did not [UNSUBSCRIBE] this time for client %s on item %s for instance %s. Error: %s',client_reply_channel, obj['msg'], message.channel_session['instance'], err)

        elif obj['op'] == 'kill_all_tlm':
            try:
                to_kill_pid = proc_map[client_reply_channel]
                to_kill = psutil.Process(to_kill_pid)
                to_kill.kill()
                del proc_map[client_reply_channel]
                del sock_map[client_reply_channel]
                logw('[TLMKILL] attempt made for client %s on process %s for instance %s.',client_reply_channel, str(to_kill_pid), message.channel_session['instance'])
            except:
                ## TODO: safely log error, unit test required
                logw('[TLMKILL] attempt made was UNSUCCESSFUL for client %s on process %s for instance %s.',client_reply_channel, str(to_kill_pid), message.channel_session['instance'])
                pass
            #deserialized = json.loads(self.r.get('activeSubscriptions'))
            #print 'deserialized'



    def push(self,websocket_obj,inst_name,id):
        """!
        A non-busy forever loop pushes telemetry to client.
        @param websocket_obj:  websocket object
        @return: void
        """
        while True:
            try:
                result = websocket_obj.recv()
                wrd = web_pb2.WebSocketServerMessage()
                wrd.ParseFromString(result)
                if str(wrd.type) != '2':
                    print '--------'
                    print  wrd,'\n',result,'\n',type(wrd),'\n',wrd.type,'\n',wrd.reply
                    print '--------'
                    Group(inst_name).send({'text': base64.b64encode(result)})

            except Exception, err:
                loge('Push error occured while trying to push messages to client. Error %s',err)
                break
            ## avoids busy-while-loop
            time.sleep(0.01)



def tlm_connect( message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """

    Group('tlm_bc').add(message.reply_channel)
    Feedback = json.dumps("OK")
    message.reply_channel.send({'accept': True, 'text':Feedback})
    tk.log('Instance', 'Connected.', 'INFO')
def tlm_disconnect( message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    Feedback = json.dumps("ENDOK")
    message.reply_channel.send({'close': True, 'text':Feedback})
    Group('tlm_bc').discard(message.reply_channel)
    tk.log('Instance', '(Dis)connected.', 'INFO')
def getTelemetry( message):
    """!
    Takes the telemetry message object and either sends a subscribe or unsubscribe signal to pyliner/yamcs.
    Creates or destroys `push` processes based on signal received.
    @param message: telemetry message object is sent from the client.
    @return: void
    """
    message_client_id = message.content['reply_channel']
    ## clean text
    message_text = tk.byteify(message.content['text'])
    ## unsubscribe signal
    if message_text.find('kill_tlm') != -1:
        try:
            msg = message_text.replace('kill_tlm', '')
            msg_text_obj = json.loads(msg)
            temp = ' {"parameter":"unsubscribe", "data":{"list":' + str(tk.byteify(msg_text_obj['tlm'])) + '}}'
            temp = temp.replace("\'", "\"")
            to_send = '[1,1,0,' + str(temp) + ']'
            ## Train
            test_db_wrapper(message_text,'null','KILTLM','unsubscribe telemetry')
            ## sending unsubscribe signal to pyliner/yamcs
            sock_map[message_client_id].send(to_send)
            tk.log('Instance', '[UNSUBSCRIBED] - '+message_client_id+' - '+msg, 'DEBUG')
        except:
            ## TODO: safely log error, unit test required
            tk.log('Instance', '[ERR - UNSUBSCRIBED] - ' + message_client_id + ' - ' + message_text, 'ERROR')
            pass
    ## kill all processes
    elif message_text.find('USALL')!=-1:
        try:
            to_kill_pid = proc_map[message_client_id]
            to_kill = psutil.Process(to_kill_pid)
            to_kill.kill()
            del proc_map[message_client_id]
            del sock_map[message_client_id]
            tk.log('Instance', '[KILLED] - ' + str(to_kill_pid), 'DEBUG')

        except:
            ## TODO: safely log error, unit test required
            tk.log('Instance', '[ERR - KILLED] - NA', 'ERROR')
            pass
    ## Subscribe signal
    ## Send message, start a system process, store current data in a local dict.
    elif message_text.find('tlm')!=-1:
        msg_text_obj = json.loads(message_text)
        temp = ' {"parameter":"subscribe", "data":{"list":' + str(tk.byteify(msg_text_obj['tlm'])) + '}}'
        temp = temp.replace("\'", "\"")
        to_send = '[1,1,0,' + str(temp) + ']'
        ## Train
        test_db_wrapper(message_text, 'null', 'SUBTLM', 'subscribe telemetry')
        ## One time per application cycle.
        if message_client_id not in sock_map.keys():
            try:
                client_id = message.content['reply_channel']
                #print client_id
                #ws = create_connection('ws://' + str(address) + ':' + str(port) + '/' + redis_cache.get('instance') + '/_websocket')
                ws = create_connection('ws://127.0.0.1:8090/softsim/_websocket')

                #print ws
                sock_map[client_id] = ws
                #msg_map[message_client_id] = message
                sock_map[message_client_id].send(to_send)



                #print client_id
                #print sock_map
                #Feedback = json.dumps("OK")
                #message.reply_channel.send({'text': Feedback})
                process = Process(target=push1,args=(sock_map[message_client_id],))
                process.start()
                proc_map[client_id] = process.pid
                tk.log('Instance', '[PROCESS] - ' + str(process.pid) , 'DEBUG')
            except Exception as e:
                ## TODO: safely log error, unit test required
                tk.log('Instance', '[ERR - PROCESS] - '+str(e)+' -  ' + message_client_id + ' - ' + message_text, 'ERROR')
                pass
        ## If already a socket is created then continue and use that socket
        else:
            try:
                sock_map[message_client_id].send(to_send)
                tk.log('Instance', '[SUBSCRIBED] - ' + message_client_id + ' - ' + message_text, 'DEBUG')
            except:
                ## TODO: safely log error, unit test required
                tk.log('Instance', '[ERR - SUBSCRIBED] - ' + message_client_id + ' - ' + message_text, 'DEBUG')
                pass
def push1( websocket_obj):
    """!
    A non-busy forever loop pushes telemetry to client.
    @param websocket_obj:  websocket object
    @return: void
    """
    freq_count = 1
    while True:
        #try:
            result = websocket_obj.recv()
            ## If result is not a ACK signal, in YAMCS case ACK looks like `[1,2,x]`
            if result != '[1,2,0]' :
                result2 = tk.preProcess(result)
                """INTROSPECTION PURPOSE ONLY"""
                e_list =  json.loads(json.dumps(ast.literal_eval(result2)))
                #for e in e_list['parameter']:
                #    print '-------------------',e['id']['name']
                #"""
                ## gets telemetry once every 10 loops
                if test_sampling_frequency*freq_count == 1 :
                    ## Train
                    test_db_wrapper(result, result2, 'PREPROCTLM', 'preprocess telemetry before sending')
                    freq_count = 1
                freq_count+=1
                try:
                    #message.reply_channel.send({'text': result2})
                    Group('tlm_bc').send({'text': result2})
                    #print result2
                except:
                    time.sleep(1)
                    #message.reply_channel.send({'text': result2})
                    Group('tlm_bc').send({'text': result2})
        #except Exception as e:
            #tk.log('Instance', 'Not able to push messages to client. Process killed. Error = '+str(e), 'ERROR')
            #break
        ## avoids busy-while-loop
        #time.sleep(0.01)



def cmd1_connect( message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    Feedback = json.dumps("OK")
    message.reply_channel.send({'accept': True, 'text':Feedback})
    tk.log(defaultInstance,'Commanding connected to  client','INFO')
def cmd1_disconnect( message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    Feedback = json.dumps("ENDOK")
    message.reply_channel.send({'close': True, 'text':Feedback})
    tk.log('defaultInstance', 'Commanding (dis)connected from client', 'INFO')
def cmd2_connect( message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    Feedback = json.dumps("OK")
    message.reply_channel.send({'accept': True, 'text': Feedback})
    tk.log(defaultInstance,'Commanding connected to  client','INFO')
def cmd2_disconnect( message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    Feedback = json.dumps("ENDOK")
    message.reply_channel.send({'close': True, 'text': Feedback})
    tk.log('defaultInstance', 'Commanding (dis)connected from client', 'INFO')
def test_db_wrapper(input,output,code,desc):
    """!
    This is a hook to record inputs and subsequent outputs that are generated by Command.
    @param input: a string object before a certain process is applied on it.
    @param output: a string object after the process is applied on it.
    @param code: a user defined string, categorizes various database entries.
    @param desc: description of the process that is applied on the input.
    @return: void
    """
    if mode == 0:
        try:
            conn = sqlite3.connect(app_path + '/test_database', timeout=5)
            tk.collectTestCases(conn, code, input, output, desc)
            conn.commit()
            conn.close()
            tk.log('Train', 'Item inserted in database.', 'DEBUG')
        except:
            ## TODO: safely log error, unit test required
            tk.log('Train', 'NA', 'ERROR')
            pass
def getCommandInfo( message):
    """!
    Takes the command message object and requests commanding information from pyliner/yamcs.
    @param message: command message object is sent from the client.
    @return: void
    """
    message_text = message.content['text']
    ## got handshake
    if message_text == 'HS':
        message.reply_channel.send({'text': 'HSOK'})
    ## got command object
    else:
        if defaultInstance!='None':
            response = urllib.urlopen('http://' + str(address) + ':' + str(port) + '/api/mdb/'+ str(defaultInstance)+'/commands'+message_text)
        else:
            response = urllib.urlopen('http://' + str(address) + ':' + str(port) + '/api/mdb/'+ redis_cache.get('default_instance')+'/commands'+message_text)
        data = json.loads(json.dumps(response.read()))
        data = data.replace("\"", "\'")
        ## Train
        test_db_wrapper(message_text, data, 'CMDINFO', 'commanding information')
        message.reply_channel.send({'text':data})
def postCommand( message):
    """!
    Takes the command message object and posts it to pyliner/yamcs.
    @param message: command message object is sent from the client.
    @return: void
    """
    message_text = message.content['text']
    to_post = json.loads(message_text)
    url=''
    if defaultInstance!='None':
        url = 'http://' + str(address) + ':' + str(port) +'/api/processors/' + str(defaultInstance) + '/realtime/commands' + to_post['name'] + '?nolink'
    else:
        url = 'http://' + str(address) + ':' + str(port) +'/api/processors/' + redis_cache.get('default_instance') + '/realtime/commands' + to_post['name'] + '?nolink'
    ## preparing post header
    msg = '{"sequenceNumber": 0,"origin": "user@my-machine","assignment":'+ str(json.dumps(to_post['args']))+',"dryRun": false}'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    r = requests.post(url=url, data=msg, headers = headers)
    ## Train
    test_db_wrapper(message_text, r.status_code, 'CMDPOST', 'sending commands')
    got = r.text
    redis_cache.set('t_btn_cnt',str((int(redis_cache.get('t_btn_cnt'))+1)))
    op = json.dumps({"cmd":got,"code":r.status_code})
    message.reply_channel.send({'text': op})





def tid_connect( message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    message.reply_channel.send({'accept': True})
def tid_disconnect( message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    message.reply_channel.send({'close': True})
def setDefaultInstance(message):
    """!
    Upon an instance being selected on the application, this method is called; which updates redis cache
    whith the latest instance.
    @param message: message contains active instance name.
    @return: void
    """
    name = message.content['text']
    defaultInstance = name
    redis_cache.set('instance',name)








def eve_connect(message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    message.reply_channel.send({'accept': True})
def eve_disconnect(message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    message.reply_channel.send({'close': True})
def getEvents(message):
    """!
    Upon receipt of invoke signal this function generates a process which pushes live event feeds to client.
    Upon receipt of kill signal the fucntion will kill the running process.
    @param message: event message object is sent from the client.
    @return: void
    """
    message_text = message.content['text']
    client_id = message.content['reply_channel']
    ## when invoke signal is received
    if message_text == 'INVOKE':
        data = '[1, 1, 1, {"events": "subscribe"}]'
        ws = None
        if defaultInstance == 'None':
            ws = create_connection('ws://' + address + ':' + str(port) + '/'+redis_cache.get('default_instance')+'/_websocket')
        else:
            ws = create_connection('ws://' + address + ':' + str(port) + '/'+defaultInstance+'/_websocket')
        ws.send(data)
        t = Process(target=push, args=(ws, message))
        t.start()
        proc_map_e[client_id] = t.pid
        sock_map_e[client_id] = ws

    # when kill signal is received
    elif message_text =='KILLSWITCH':
        try:
            us_sock = sock_map_e[client_id]
            data = '[1, 1, 1, {"events": "unsubscribe"}]'
            us_sock.send(data)
            tk.log('Event', '[UNSIBSCRIBED] - ' + client_id+' events', 'DEBUG')
        except:
            ## TODO: safely log error, unit test required
            tk.log('Event','Unable to unsubscribe.','ERROR')
            pass
        try:
            to_kill_pid = proc_map_e[client_id]
            print '****', to_kill_pid, proc_map_e
            to_kill = psutil.Process(to_kill_pid)
            to_kill.kill()
            tk.log('Event', '[KILLED] - ' + to_kill_pid, 'DEBUG')
        except:
            ## TODO: safely log error, unit test required
            tk.log('Event', 'Unable to kill.', 'ERROR')
            pass
def push(websocket_obj,message_obj):
    """!
    A non-busy forever loop pushes events to client.
    @param websocket_obj:  websocket object
    @param message_obj:  message object
    @return: void
    """
    while True:
        result = websocket_obj.recv()
        ## If result is not a ACK signal, in YAMCS case ACK for events looks like `[1,4,x]`
        if result.find('[1,4,')!=-1 :
            #result = tk.preProcess(result)


            message_obj.reply_channel.send({'text': result})
            message_obj.reply_channel.send({'text': result})
            message_obj.reply_channel.send({'text': result})
            tk.log('Event', 'BOUND', 'INFO')
            print message_obj.reply_channel.__dict__
            print result
        ## avoids busy-while-loop
        time.sleep(0.01)




# independent channels
def inst_connect(message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    message.reply_channel.send({'accept': True})

def inst_disconnect(message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    message.reply_channel.send({'close': True})

def getInstanceList(message):
    """!
    This function is invoked by the client. Upon such an event, an instance list is requested from
    pyliner/yamcs which is forwarded to client.
    @param message: invoke signal sent from client
    @return: void
    """
    name = message.content['text']
    response = urllib.urlopen('http://' + str(address) + ':' + str(port) + '/api/instances')
    data = json.loads(json.dumps(response.read()))
    message.reply_channel.send({'text': data})
    logi('Instances list is sent.')

def dir_connect(message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    message.reply_channel.send({'accept': True})

def dir_disconnect(message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    message.reply_channel.send({'close': True})

def directoryListing(message):
    """!
    Takes the file or directory name in the  message object, scrapes file system and sends out a json to client
    which has sub-directories listed.
    @param message: message object with directory or file name is sent from the client.
    @return: void
    """
    name = message.content['text']
    response = tk.get_directory(name)
    data = json.dumps(response)
    ## Train
    #test_db_wrapper(name, data,'DIR','obtain directory listing')
    message.reply_channel.send({'text': data})
    logi('Directory list under \' %s \' is sent.',name)

def adsb_connect(message):
    """!
        Accepts request and establishes a connection with client.
        @param message: connection request from client, this message will connection headers.
        @return: void
        """
    message.reply_channel.send({'accept': True})

def adsb_disconnect(message):
    """!
       Accepts disconnection message and disconnects with client.
       @param message: disconnection request from client, this message will disconnection headers.
       @return: void
       """
    message.reply_channel.send({'close': True})

def getAdsb(message):

    text = message.content['text']
    client_reply_channel = message.content['reply_channel']
    if text == 'INVOKE':
        if len(Group('adsb').channel_layer.group_channels('adsb'))!=0:
            Group('adsb').add(message.reply_channel)
        else:
            process = Process(target=adsbPush, args=(message,))
            process.start()
            adsb_proc.append(process.pid)
            logi('New adsb-push process has been [Created] with pid %s.', str(process.pid))
    elif text == 'KILL':
        if len(Group('adsb').channel_layer.group_channels('adsb')) > 1 :
            #print client_reply_channel
            Group('adsb').discard(message.reply_channel)
        elif client_reply_channel in Group('adsb').channel_layer.group_channels('adsb'):
            for each in adsb_proc:
                to_kill = psutil.Process(each)
                to_kill.kill()
                adsb_proc.remove(each)
                logi('Adsb-push process has been [Killed] with pid %s.', str(each))

def adsbPush(message):
    """!
    A non-busy forever loop pushes telemetry to client.
    @param websocket_obj:  websocket object
    @return: void
    """
    while True:
        try:
            response = urllib.urlopen('http://' + str(address) + ':' + str(adsb_port) + '/dump1090/data.json')
            data = json.loads(json.dumps(response.read()))
            Group('adsb').send({'text': data})
            #message.reply_channel.send({'text': data})
            logd('ads-b packet is sent.')

        except Exception, err:
            loge('Adsb-push error occured while trying to push messages to client. Error %s', err)
            break
        ## avoids busy-while-loop
        time.sleep(1)

def vid_connect( message):
    """!
    Accepts request and establishes a connection with client.
    @param message: connection request from client, this message will connection headers.
    @return: void
    """
    message.reply_channel.send({'accept': True})

def vid_disconnect( message):
    """!
    Accepts disconnection message and disconnects with client.
    @param message: disconnection request from client, this message will disconnection headers.
    @return: void
    """
    message.reply_channel.send({'close': True})

def getVideo(message):
    """!
    Invokes a continuous looping function which will push video images to client.
    @param message: invoke message from client.
    @return: void
    """
    text = message.content['text']

    client_reply_channel = message.content['reply_channel']
    print text,'   ',client_reply_channel
    if text == 'INVOKE':
        if len(Group('video').channel_layer.group_channels('video'))!=0:
            Group('video').add(message.reply_channel)
        else:
            process = Process(target=VideoThroughUDP, args=(message,))
            process.start()
            Group('video').add(message.reply_channel)
            vid_proc.append(process.pid)
            logi('New video-push process has been [Created] with pid %s.', str(process.pid))
    elif text == 'KILL':
        #print len(Group('video').channel_layer.group_channels('video'))
        #print (Group('video').channel_layer.group_channels('video'))
        #print vid_proc
        if len(Group('video').channel_layer.group_channels('video')) > 1 :
            #print client_reply_channel
            Group('video').discard(message.reply_channel)


        elif client_reply_channel in Group('video').channel_layer.group_channels('video'):

            for each in vid_proc:
                to_kill = psutil.Process(each)
                to_kill.kill()
                vid_proc.remove(each)
                Group('video').discard(message.reply_channel)
                logi('video-push process has been [Killed] with pid %s.', str(each))

    #name = message.content['text']
    #VideoThroughUDP(message)


def VideoThroughUDP(msg_obj):
    """!
    Binds with UDP port and forwards image data as and when received from pyliner/yamcs.
    @param msg_obj: ivoke message passed as parameter in `getVideo' function.
    @return: void
    """
    ## UDP
    video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    video_socket.bind(('', video_port))
    video_frame_counter = 0

    while True:
        try:
            ## buffer size is 65527 bytes
            data, addr = video_socket.recvfrom(65527)
            b64_img = base64.b64encode(data)
            video_frame_counter = video_frame_counter + 1
            Group('video').send({'text': b64_img})
            #msg_obj.reply_channel.send({'text': b64_img})
            #logi('video frame #%s is sent.', video_frame_counter)
            #video_frame_counter = video_frame_counter + 1
            # yield b64_img


        except Exception, err:
            loge('Video-push error occured while trying to push messages to client. Error %s', err)
            break
        ## avoids busy-while-loop
        time.sleep(0.01)








class MyCache:
    """!
   Loads launch variable to cache
    """
    def __init__(self):
        """!
        Initializes globally required variables from redis cache and other data structures that are helpful in tracking
        messages when the instance of this class is called in a multiprocess setting (or with multiple workers).
        """
        ## Initialize redis caching database
        self.redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)


    def initialize(self):
        """!
        Initializes redis cache with lauch variables which will persist through out the application.
        And performs certain housekeeping tasks.
        @return: void
        """

        for key in self.redis_cache.keys():
            self.redis_cache.delete(key)
        try:
            with open(os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/scripts/launch_config.json') as file:
                config = json.load(file)

                self.redis_cache.set('default_instance', config['pyliner']['default_instance'])
                self.redis_cache.set('address', config['pyliner']['address'])
                self.redis_cache.set('port', config['pyliner']['port'])
                self.redis_cache.set('video_port', config['pyliner']['video_port'])
                self.redis_cache.set('adsb_port', config['pyliner']['adsb_port'])
                #cache.set('activeSubscriptions','{}')
                self.redis_cache.set('number_of_workers', config['number_of_workers'])
                self.redis_cache.set('mode', config['mode'])
                self.redis_cache.set('app_path', config['app_path'])
                #self.redis_cache.set('vid_clients', 0)  # TODO: REMOVE THIS
                self.redis_cache.set('t_btn_cnt',0)#TODO: REMOVE THIS

                ## clean test database, table
                """
                if int(self.redis_cache.get('mode')) == 0:
                    conn = sqlite3.connect(self.redis_cache.get('app_path') + '/test_database', timeout=5)
                    c = conn.cursor()
                    ex = 'delete from TESTCASES'
                    c.execute(ex)
                    conn.commit()
                    conn.close()
                """
            logi('Preloading redis datastore is complete.')
        except Exception as e:
            ## TODO: safely log error, unit test required
            logw('Preloading redis datastore failed with error %s',e)
            pass

