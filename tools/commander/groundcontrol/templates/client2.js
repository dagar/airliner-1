//'use strict';



//Tools
var DEBUG = false;
var ERROR = true;
var INFO = true;

function _base64ToArrayBuffer(base64) {
    var binary_string =  window.atob(base64);
    var len = binary_string.length;
    var bytes = new Uint8Array( len );
    for (var i = 0; i < len; i++)        {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes.buffer;
}

function replaceAll(str, find, replace) {
            if (typeof str !='string'||typeof find !='string'||typeof replace !='string'){
                throw new TypeError('A non string argument is passed')
            }
            var st = str.toString();
            return st.replace(new RegExp(find, 'g'), replace);
        }
/*exempted*/
function introspectTlm(string_data){
    try{
        var clean_data1 = replaceAll(string_data.data,"\'", "\"")
        var clean_data2 = replaceAll(clean_data1,'True','true');
        var j = JSON.parse(clean_data2);
        var items = j['parameter']
        for(var i in items){
            console.log(items[i]['id']['name'])
        }
    }
    catch(e){
        throw new TypeError('Telemetry format mismatch')
    }

}

function getDate(format){
    var tempstore =new Date();

        if(format=='d'){
        return String(tempstore);
        }
        else if (format=='s'){
        return String(tempstore.getTime());
        }
        else{
        return String(tempstore);
        }
}

function log(logtype, message, specials){

    try{
        if(logtype == 'ERR' && ERROR){
            console.log(logtype+' - '+message+' - '+'[',specials,']' );
        }
        else if (logtype == 'INFO' && INFO){
            console.log(logtype+' - '+message+' - '+'[',specials,']' );
        }
        else if (logtype == 'DEBUG' && DEBUG){
            console.log(logtype+' - '+message+' - '+'[',specials,']' );
        }
    }
    catch(e){
        throw new TypeError('A non string argument was passed')
    }


}

function makeIterator(array) {
    var nextIndex = 0;
    return {
       next: function() {
           return nextIndex < (array.length) ?
               {value: array[nextIndex++], done: false} :
               {done: true};
       },
       id: function(){
        return nextIndex;
       },
       done: function(){
            if(nextIndex>=0 && nextIndex<array.length){return false;}
            else{return true;}
       },
       set: function(i){

        if(i<0 || i>array.length){
            throw new Error('index out of bound')
        }
        if(typeof i != 'number'){
            throw new Error('A non number argument was passed')
        }
        nextIndex = i;
       }
    };

}

function getSockets(obj){
    var ws_hold =[];
    Object.keys(obj).forEach(function(key,index) {
    if(obj[key] instanceof WebSocket){
            ws_hold.push(obj[key]);

        }

    });

    return ws_hold;



}
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

//---------------------------------------------------------------------------------------------------------------
/* Session Maintainance:
   A web socket function to establish instance specific communication between server and client.
   Initializes two websockets:
    1. receives instance list.
    2. Informs server about the instance selected. */
//---------------------------------------------------------------------------------------------------------------
var Session_Maintainance = function(){

    this.websocket = new WebSocket('ws://' + window.location.host + '/session');
    this.info = new WebSocket('ws://'+ window.location.host + '/cmd1');
    this.cmd = new WebSocket('ws://'+ window.location.host + '/cmd2');
    this.event = new WebSocket('ws://' + window.location.host + '/event');


    var self = this;
    this.instance_name = null;
    this.subscribers = [];
    this.queuedSubscribers = [];
    this.allSubscibers = [];
    this.activeSubscribers = [];
    this.toUnsubscribe= [];
    this.count_command_loads=1;
    this.CommandQueue = [];
    this.SendingQueue = [];
    this.superQ = {};
    this.ccount=0;
    this.graphic = document.getElementsByClassName('loadingGraphics');
    //this.status = document.getElementsByClassName('loadingText');





    /*unify*/
    this.websocket.onopen = function(){
        log('DEBUG','Connection open.','getInstanceList');

    };
    this.websocket.onclose = function(){
        log('DEBUG','Connection closed.','getInstanceList');
    };
    this.websocket.onerror = function(evt){
        log('ERR','Connection closed with error - '+String(evt),'getInstanceList');
    };
    /*getCommandInfo*/
    this.info.onopen = function (){
        log('DEBUG','Connection open.','getCommandInfo');
    }

    this.info.onclose = function (){
        log('DEBUG','Connection closed.','getCommandInfo');
    }
    this.info.onerror = function (){
        log('ERR','Connection closed.','getCommandInfo');
    }

    /*sendCommand*/
    this.cmd.onopen = function (){
        log('DEBUG','Connection open.','sendCommand');
    }

    this.cmd.onclose = function (){
        log('DEBUG','Connection closed.','sendCommand');
    }
    this.info.onerror = function (){
        log('ERR','Connection closed.','sendCommand');
    }

    /*event*/
    this.event.onopen = function (){
        log('DEBUG','Connection open.','getEvents');
        self.event.send('INVOKE');
        log('INFO','Message Sent.','getEvents');
    }

    this.event.onclose = function(){
        log('DEBUG','Connection closed.','getEvents');
    }
    this.event.onerror = function(){
        log('ERR','Connection closed.','getEvents');
    }

}
Session_Maintainance.prototype = {
    /*clean commanding queues*/


    loadGraphics:function(){
        var blur_level = 20
        var content = document.getElementById('content')
        content.style.webkitFilter='blur('+String(blur_level)+'px)'
        content.style.filter='blur('+String(blur_level)+'px)'
        var backup = this.graphic
        var x = this.graphic[0];
        if (x.style.display == 'none')
        {
           x.style.display = '';
        }
        else
        {
            x.style.display = 'none';
        }




        var spin = new TimelineMax();
        var loading = new TimelineMax({
            repeat: -1
        });

        spin.to($('.blade'), 0.6, {
            rotation: 360,
            repeat: -1,
            transformOrigin: '50% 50%',
            ease: Linear.easeNone
        });

        loading.to($('.loadingText'), 1, {
            opacity: 0,
            ease: Linear.easeNone
        })
        .to($('.loadingText'), 1, {
            opacity: 1,
            ease: Linear.easeNone
        });

        window.addEventListener('unload_animation', function (e) {
            spin.stop();
            loading.stop();
            x.style.display = 'none';
            for(var i =blur_level ; i<1; i--){
            content.style.webkitFilter='blur('+String(i)+'px)'
            content.style.filter='blur('+String(blur_level)+'px)'
            }
            content.style.webkitFilter=''
            content.style.filter=''
            this.graphic = backup

        });
        // example js to make a fade out when the page is done loading
         /*$(window).load(function() {
            $(".se-pre-con").fadeOut("slow");
        });*/

    },

    cleanSlate: function(){
        this.CommandQueue = [];
        this.SendingQueue = [];
        this.count=0;
        log('DEBUG','Clean slate executed.','commandCleanSlate')
    },

    RequestCmdDef: function(cmdObj, cb){
        var socket = this.info;
        var self = this;
        var cmdName = Object.keys(cmdObj)[0];

        if (!Object.keys(self.superQ).includes(cmdName)){

            socket.send(JSON.stringify({"op":"RequestCmdDef", "msg":cmdName ,'inst': this.instance_name}));
            return false;
        }
        else{
            try{

                var btn = cmdObj[cmdName][0];
                var jsn = cmdObj[cmdName][1];
                cb(self.superQ[cmdName],jsn,btn);
                //self.count_command_loads+=1
                //var st = 'Loading Commands ..... '+String(Math.round(self.count_command_loads*100/self.CommandQueue.length))+'%'+' EVENT : '+JSON.stringify(jsn)
                //console.log(st)

                return true;
            }
            catch(err){
                return true;
            }
        }
    },

    ProcessCmds: function(cb){

        var socket = this.info;
        var self = this;
        var cq = makeIterator(this.CommandQueue)
        var btn = null;
        var jsn = null;
        var Que_obj = null;
        var message = null;
        var i = 0;


        do{

            if(cq.done()){
                log('INFO','Commanding Queue processing complete.!','sendCommand');
                var evt = new CustomEvent('unload_animation', { detail: 'state' });
                window.dispatchEvent(evt);
                break;
            }

            Que_obj = cq.next().value;
            //sleep(5);

            /*self.count_command_loads+=1
            var st = '##########Loading ...  '+String(self.count_command_loads*100/self.CommandQueue.length)+'%'
            console.log(st)
            self.status.innerHTML = st*/
        } while(this.RequestCmdDef(Que_obj, cb) == true);

        socket.onmessage = function (event){
            /* Retrieve the object and call the callback. */
            var cmdName = Object.keys(Que_obj)[0];
            var btn = Que_obj[cmdName][0];
            var jsn = Que_obj[cmdName][1];
            self.superQ[cmdName]= event;

            cb(event,jsn,btn);
            var compute_p = Math.round(self.count_command_loads*100/self.SendingQueue.length)

            self.count_command_loads+=1
            var st = 'Loading Commands ..... <br/> Completed : '+String(compute_p)+'%'//+' <br/> Command : '+JSON.stringify(jsn['cmd']['name'])
            //console.log(st)
            document.getElementsByClassName('loadingText')[0].innerHTML = st
            if(compute_p>100){
               document.getElementsByClassName('loadingText')[0].innerHTML = 'Please Wait ....'
               this.count_command_loads=1;
            }

            do{
                if(cq.done()){
		            log('INFO','Commanding Queue processing complete.!','sendCommand');
		            var evt = new CustomEvent('unload_animation', { detail: 'state' });
                    window.dispatchEvent(evt);
                    break;
                }

                Que_obj = cq.next().value;
                /*self.count_command_loads+=1
                var st = '##########Loading ...  '+String(self.count_command_loads*100/self.CommandQueue.length)+'%'
                console.log(st)
                self.status.innerHTML = st*/
                //document.getElementsByClassName('loadingText')[0].innerHTML = 'Almost ready...'
            } while(self.RequestCmdDef(Que_obj, cb) == true);
        }

    },

    prepareCmds: function(message,jobj,btn){
        var lookup_obj = {}
        lookup_obj[message]=[btn,jobj]
        this.CommandQueue.push(lookup_obj);
        if(!this.SendingQueue.includes(message)){
            this.SendingQueue.push(message);
        }
    },

    sendCommand: function(name,args){
        var obj = {"name":name,"args":args}
        var message = JSON.stringify(obj)
        var socket = this.cmd;

        socket.onmessage = function (event){
           //log('DEBUG',event,'')
            log('INFO','Button feedback.',event);
        }

        if (socket.readyState == WebSocket.OPEN) {
//          #/console.log(message);
          socket.send(JSON.stringify({"op":"sendCommand", "msg":message,'inst': this.instance_name}));
        };

    },

    /*transmitCurrentInstance*/
    transmitCurrentInstance: function(message){
        var socket = this.websocket;
        var self = this

        /* Flush the queuedSubscribers queue, if there are any. */
        try{
            if (socket.readyState == WebSocket.OPEN) {
                if(self.queuedSubscribers.length > 0)
                {
                    log('INFO','Flushing queued subscribers.','transmitCurrentInstance');
                    self.queuedSubscribers.forEach(function(subscriber){
                        self.subscribeTelemetry(subscriber.message, subscriber.callback);
                    });
                }
            }
        }
        catch(e){
        //console.log('nothing');
        }


        socket.onmessage = function (event){
            log('INFO','Message received.'+event,'transmitCurrentInstance');
        }
        //sleep(2000).then(()=>{
        //console.log(socket.readyState);
        //console.log(this.websocket2.readyState);






        if (socket.readyState == WebSocket.OPEN) {
            //console.log('1112');

            log('INFO','Message sent.','transmitCurrentInstance');
            socket.send(JSON.stringify({"op":"bind_instance","msg":message}));
            this.instance_name=message;
            //console.log(socket);
            //console.log(this.websocket2);
            //console.log(message);
        };//});
    },


    subscribeTelemetry: function(msgObj,cb){
        var socket = this.websocket;
        var message = "";
        var self = this;
        self.allSubscibers.push(msgObj)
        /* If this msgObj is an object, stringify it. */
        if(typeof msgObj === 'object')
        {
            /* This is an object.  Stringify it. */
            message = JSON.stringify(msgObj);
        }
        else
        {
            /* This is not an object.  Its probably already
               stringify, so just use the string as is, but
               set msgObj to the JSON object so we can parse
               it later.
             */
            message = msgObj;
            msgObj = JSON.parse(message);
        }

        if (socket.readyState == WebSocket.OPEN){
            log('INFO','Message sent.','subscribeTelemetry');

            socket.send(JSON.stringify({"op":"subscribe_tlm","msg":message}));

            /* Store the subscription away so we can route the updates
             * to the callback later.  We could have received multiple
             * telemetry items, so store each one off individually.
             */
            msgObj.tlm.forEach(function(tlmItem){
                var subscription;

                /* First check to see if we've ever subscribed to this
                 * telemetry item.  This is so we can support sending updates
                 * to multiple subscriber callbacks for the same telemetry
                 * item.
                 */
                if(!(tlmItem.name in self.subscribers)){
                    /* This telemetry item has not been subscribed to.  Create
                     * an empty array with this key.
                     */
                    self.subscribers[tlmItem.name] = [];
                }

                /* Now push the new subscription onto the subscribers array. */
                self.subscribers[tlmItem.name].push({'callback': cb});
            });
        }
        else
        {
            log('INFO','Message queued.','subscribeTelemetry');
            this.queuedSubscribers.push({'message':message, 'callback':cb});
        }
        socket.onmessage = function (message2){
            log('INFO','Message received.','subscribeTelemetry');
            var fixedDataString = message2.data.replace(/\'/g, '"')
            fixedDataString = fixedDataString.replace(new RegExp('True', 'g'),'true');
            fixedDataString = fixedDataString.replace(new RegExp('False', 'g'),'false');
            var data = JSON.parse(fixedDataString);
            if(data.hasOwnProperty('parameter')) {
                data.parameter.forEach(function(param){
                    var tlmName = param.id.name;

                    if(tlmName in self.subscribers){
                        var subscriptions = self.subscribers[tlmName];
                        subscriptions.forEach(function(subscription){
                            subscription.callback(param);
                        });
                    }
                });
            }
            //this.subscribers[event.data.parameter.data.keys(obj).forEach(function(key,index) {
            //console.log(event);
            //cb(event);
        }
    },

    unSubscribeTelemetry: function(msgObj){
        var socket = this.websocket;
        var message = "";
        //console.log('/**********/');
        //console.log(msgObj);
        //console.log('/**********/');
        /* If this msgObj is an object, stringify it. */
        if(typeof msgObj === 'object')
        {
            /* This is an object.  Stringify it. */
            message = JSON.stringify(msgObj);
            //console.log(message);
        }
        else
        {
            /* This is not an object.  Its probably already
               stringify, so just use the string as is.
             */
            message = msgObj;
        }

        //var msg = 'kill_tlm'+message

        for(var i=0;i<2;i++){
        socket.send(JSON.stringify({"op":"unsubscribe_tlm","msg":message}));}



    },

    killAll: function(){
        var self = this;
        for(var i=0;i<20;i++){
        self.websocket.send(JSON.stringify({"op":"kill_all_tlm", "msg":"killmsg"}));
        }


    },

    unSubscribeAll: function(){
        var self = this;
        for(var i =0; i<self.allSubscibers.length;i++){
            var rem = self.allSubscibers.pop();
            self.unSubscribeTelemetry(rem);
            log('DEBUG','Unsubscribed to telemetry.','count'+String(i));
        }
    },

    eventSubscription: function(cb){
        var socket = this.event

        socket.onmessage = function (event){
            log('INFO','Message received.','getEvents');
            cb(event);
        }

    },

    eventKill:function(){
    var socket = this.event
    for(var i=0;i<20;i++){
        socket.send('KILLSWITCH');
        }
    },



}

//---------------------------------------------------------------------------------------------------------------
/* INSTANCE:
   A web socket function to establish instance specific communication between server and client.
   Initializes two websockets:
    1. receives instance list.
    2. Informs server about the instance selected. */
//---------------------------------------------------------------------------------------------------------------

var Instance = function(){
    this.websocket1 = new WebSocket('ws://' +window.location.host + '/inst');
    var self = this;
    /*getInstanceList*/
    this.websocket1.onopen = function(){
        log('DEBUG','Connection open.','getInstanceList');
        self.websocket1.send('INVOKE');
        self.websocket1.send('INVOKE');//backup1
        self.websocket1.send('INVOKE');//backup2
        log('INFO','Invoke Sent.','getInstanceList');
    };
    this.websocket1.onclose = function(){
        log('DEBUG','Connection closed.','getInstanceList');
    };
    this.websocket1.onerror = function(evt){
        log('ERR','Connection closed with error - '+String(evt),'getInstanceList');
    };

}

Instance.prototype = {
    /*getInstanceList*/
    getInstanceList: function (cb){
        var socket = this.websocket1;
        socket.onmessage = function (event){
            log('INFO','Message received.','getInstanceList');
            cb(event);
        }
    },
}
//---------------------------------------------------------------------------------------------------------------
/* DIRECTORY:
   A web socket function to establish directory specific communication between server and client.
   Initializes a websocket to retrive directory listing*/
//---------------------------------------------------------------------------------------------------------------

var Directory = function(){
    this.websocket = new WebSocket('ws://' + window.location.host + '/dir');
    var self = this;
    this.websocket.onopen = function(){
        log('DEBUG','Connection open.','getDirectoryList');
        self.websocket.send('');
        self.websocket.send('');//backup1
        self.websocket.send('');//backup2
        log('INFO','Message Sent.','getDirectoryList');
    }
    this.websocket.onclose = function(){
        log('DEBUG','Connection closed.','getDirectoryList');
    };
    this.websocket.onerror = function(evt){
        log('ERR','Connection closed with error - '+String(evt),'getInstanceList');
    };
}

Directory.prototype = {
    getDirectoryListing: function(message,cb){
        var socket = this.websocket;
        socket.onmessage = function (event){
            log('INFO','Message received.','getDirectoryList');
            cb(event);
        }
        if (socket.readyState == WebSocket.OPEN) {
            log('INFO','Message sent.','getDirectoryList');
            socket.send(message);
        };

    },

}

//---------------------------------------------------------------------------------------------------------------
/* COMMAND:
   A web socket function to establish command specific communication between server and client.
   Initialized web sockets to:
   1. Clean command object variables.
   2. Populate command object variables.
   3. Request command information.
   4. Send commands.*/
//---------------------------------------------------------------------------------------------------------------

//---------------------------------------------------------------------------------------------------------------
/* EVENT:
   A web socket function to establish event specific communication between server and client.
   Initializes web socket to receive events.*/
//---------------------------------------------------------------------------------------------------------------

var Event = function(){

    this.event = new WebSocket('ws://' + window.location.host + '/event');
    var self = this;

    this.event.onopen = function (){
        log('DEBUG','Connection open.','getEvents');
        self.event.send('INVOKE');
        log('INFO','Message Sent.','getEvents');
    }

    this.event.onclose = function(){
        log('DEBUG','Connection closed.','getEvents');
    }
    this.event.onerror = function(){
        log('ERR','Connection closed.','getEvents');
    }
}

Event.prototype = {

    eventSubscription: function(cb){
        var socket = this.event

        socket.onmessage = function (event){
            log('INFO','Message received.','getEvents');
            cb(event);
        }

    },

    kill:function(){
    var socket = this.event
    for(var i=0;i<20;i++){
        socket.send('KILLSWITCH');
        }
    },



}

//---------------------------------------------------------------------------------------------------------------
/* ADSB:
   A web socket function to establish adsb specific communication between server and client.
   Initializes web socket to receive video frames.*/
//---------------------------------------------------------------------------------------------------------------
var ADSB = function() {
        this.vid_subc = new WebSocket('ws://' + window.location.host + '/adsb');
        this.video_subscribers = {};
        var self = this;


        this.vid_subc.onopen = function (){
            log('DEBUG','Connection open.','getAdsbStream');
            self.vid_subc.send('INVOKE');//TODO
            log('INFO','Message Sent.','getAdsbStream');
        }

        this.vid_subc.onclose = function(){
            log('DEBUG','Connection closed.','getAdsbStream');
        }
        this.vid_subc.onerror = function(){
            log('ERR','Connection closed.','getAdsbStream');
        }

}
ADSB.prototype = {

    getAdsb:function(cb){
        var socket = this.vid_subc;
        var msg_count = 0;
        socket.onmessage = function (msg){

            //console.log(msg);
            msg_count += 1;
            log('INFO','Message received.','getAdsbStream');
            //console.log('client2.js ---  ',msg)
            var adsb_package = {};
            adsb_package.aircraft = JSON.parse(msg.data);
            adsb_package.messages = msg_count;
            adsb_package.now = getDate('s');
            cb(adsb_package);

        }



    },
    killAdsb:function(){
        var socket = this.vid_subc;
        for(var i=0;i<20;i++){
            socket.send('KILL');
            console.log('sent kill adsb');
            //socket.close();
        }

    },

}




//---------------------------------------------------------------------------------------------------------------
/* VIDEO:
   A web socket function to establish video specific communication between server and client.
   Initializes web socket to receive video frames.*/
//---------------------------------------------------------------------------------------------------------------
var Video = function() {
        this.vid_subc = new WebSocket('ws://' +window.location.host + '/video');
        this.video_subscribers = {};
        var self = this;

        this.vid_subc.onopen = function (){
            log('DEBUG','Connection open.','getVideoStream');
        }
        this.vid_subc.onclose = function(){
            log('DEBUG','Connection closed.','getVideoStream');
        }
        this.vid_subc.onerror = function(){
            log('ERR','Connection closed.','getVideoStream');
        }

}
Video.prototype = {

    getVideoStream:function(cb){
        var socket = this.vid_subc;
        socket.send('INVOKE');
        socket.onmessage = function (event){
            log('INFO','Message received.','getVideoStream');
            cb(event);
        }
    },

    killVideo:function(){
        var socket = this.vid_subc;
        for(var i=0;i<20;i++){
            socket.send('KILL');
            console.log('sent kill video');
        }

    },

    killVideoSocket:function(){
        var socket = this.vid_subc;
        socket.close();
    }

}



if(typeof module != 'undefined') {
    module.exports.getDate = getDate;
    module.exports.replaceAll = replaceAll;
    module.exports.introspectTlm = introspectTlm;
    module.exports.log = log;
    module.exports.makeIterator = makeIterator;
    module.exports.getSockets = getSockets;
    module.exports.Instance = Instance;
    module.exports.Directory = Directory;
    module.exports.Telemetry = Telemetry;
    module.exports.Command = Command;
    module.exports.Event = Event;
    module.exports.Video = Video;
    module.exports.Session = Session;
}
