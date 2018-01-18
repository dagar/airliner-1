'use strict';



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


function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

//---------------------------------------------------------------------------------------------------------------
/* Session Maintainance:
   A web socket function to establish instance specific communication between server and client.
   Initializes two websockets:
    1. receives instance list.
    2. Informs server about the instance selected. */
//---------------------------------------------------------------------------------------------------------------
var Session_Maintainance = function(){
    try{
        this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    }
    catch(e){
        this.ws_scheme="ws"
    }
    try{
        this.websocket = new WebSocket(this.ws_scheme+'://' + window.location.host + '/session');
    }
    catch(e){
        this.websocket = new WebSocket(this.ws_scheme+'://localhost:8000/session');
    }
    var self = this;
    this.instance_name = null;
    this.subscribers = [];
    this.queuedSubscribers = [];
    this.allSubscibers = [];
    this.activeSubscribers = [];
    this.toUnsubscribe= [];
    this.count=0;



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

}
Session_Maintainance.prototype = {



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
            //this.instance_name=message;
            //console.log(socket);
            //console.log(this.websocket2);
            //console.log(message);
        };//});
    },


    subscribeTelemetry: function(msgObj,cb){


        var socket = this.websocket;
        var c = this.count;
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
        //var pb = dcodeIO.P
        var wssm=null
        var wsrd=null
        var wssd=null
        var wsed=null
        var psr=null
        var ci =null


        protobuf.load("/static/proto/web.proto",function(err,root){

            console.log(err);
            wssm = root.lookupType("web.WebSocketServerMessage");
            /*wsrd = wssm.lookupType("web.WebSocketReplyData");
            wssd = wssm.lookupType("web.WebSocketSubscriptionData");
            wsed = wssm.lookupType("web.WebSocketExceptionData");
            psr = wssm.lookupType("web.ParameterSubscriptionResponse");
            ci = wssm.lookupType("web.ConnectionInfo");*/
            console.log('success');

            socket.onmessage = function (message2){


                var obj  = wssm.toObject(atob(message2.data), {
                    enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                });
                /*
                var obj1 = wsrd.toObject(atob(message2.data), {
                    enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                });
                var obj2 = wssd.toObject(atob(message2.data), {
                   enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                });
                var obj3 = wsed.toObject(atob(message2.data), {
                   enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                 });
                var obj4 = psr.toObject(atob(message2.data), {
                    enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                });
                var obj5 = ci.toObject(atob(message2.data),{
                    enums: String,  // enums as string names
                    longs: String,  // longs as strings (requires long.js)
                    bytes: String,  // bytes as base64 encoded strings
                    defaults: true, // includes default values
                    arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
                    objects: true,  // populates empty objects (map fields) even if defaults=false
                    oneofs: true    // includes virtual oneof fields set to the present field's name
                });*/
                //console.log(_base64ToArrayBuffer(message2.data))
                log('INFO','Message received.','subscribeTelemetry');
                c = c+1
                console.log('COUNT : ',c,'   OBJ : ',obj);/*
                console.log(obj1);
                console.log(obj2);
                console.log(obj3);
                console.log(obj4);
                console.log(obj5);*/




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
        });
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



}

//---------------------------------------------------------------------------------------------------------------
/* INSTANCE:
   A web socket function to establish instance specific communication between server and client.
   Initializes two websockets:
    1. receives instance list.
    2. Informs server about the instance selected. */
//---------------------------------------------------------------------------------------------------------------

var Instance = function(){
    try{
    this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    }
    catch(e){
    this.ws_scheme="ws"
    }
    try{
    this.websocket1 = new WebSocket(this.ws_scheme+'://' + window.location.host + '/inst');
    }
    catch(e){
    this.websocket1 = new WebSocket(this.ws_scheme+'://localhost:8000/inst');
    }
    var self = this;



    /*getInstanceList*/
    this.websocket1.onopen = function(){
        log('DEBUG','Connection open.','getInstanceList');
        self.websocket1.send('INVOKE');
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
    try{
    this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    this.websocket = new WebSocket(this.ws_scheme+'://' + window.location.host + '/dir');
    }
    catch(e){
    this.websocket = new WebSocket('ws://localhost:8000/dir');
    }
    var self = this;

    this.websocket.onopen = function(){
        log('DEBUG','Connection open.','getDirectoryList');
        self.websocket.send('');
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
var Command =function(){
    try{
    this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    this.info = new WebSocket(this.ws_scheme+'://' + window.location.host + '/cmd1');
    this.cmd = new WebSocket(this.ws_scheme+'://' + window.location.host + '/cmd2');
    }
    catch(e){
    this.info = new WebSocket('ws://localhost:8000/cmd1');
    this.cmd = new WebSocket('ws://localhost:8000/cmd2');
    }
    this.CommandQueue = [];
    this.SendingQueue = [];
    this.superQ = {};
    this.count=0;
    var self = this;

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

}

Command.prototype = {

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

            socket.send(cmdName);
            return false;
        }
        else{
            try{

                var btn = cmdObj[cmdName][0];
                var jsn = cmdObj[cmdName][1];
                cb(self.superQ[cmdName],jsn,btn);
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
                break;
            }

            Que_obj = cq.next().value;
        } while(this.RequestCmdDef(Que_obj, cb) == true);

        socket.onmessage = function (event){
            /* Retrieve the object and call the callback. */
            var cmdName = Object.keys(Que_obj)[0];
            var btn = Que_obj[cmdName][0];
            var jsn = Que_obj[cmdName][1];
            self.superQ[cmdName]= event;

            cb(event,jsn,btn);

            do{
                if(cq.done()){
		            log('INFO','Commanding Queue processing complete.!','sendCommand');
                    break;
                }

                Que_obj = cq.next().value;
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
          socket.send(message);
        };

    },


}
//---------------------------------------------------------------------------------------------------------------
/* EVENT:
   A web socket function to establish event specific communication between server and client.
   Initializes web socket to receive events.*/
//---------------------------------------------------------------------------------------------------------------

var Event = function(){
    try{
    this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    this.event = new WebSocket(this.ws_scheme+'://' + window.location.host + '/event');
    }
    catch(e){

    this.event=new WebSocket('ws://localhost:8000/event');
    }
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
        this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        this.vid_subc = new WebSocket(this.ws_scheme+'://' + window.location.host + '/adsb');
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
        this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        this.vid_subc = new WebSocket(this.ws_scheme+'://' + window.location.host + '/video');
        this.video_subscribers = {};
        var self = this;


        this.vid_subc.onopen = function (){
            log('DEBUG','Connection open.','getAdsbStream');
            //self.vid_subc.send('INVOKE');//TODO
            //log('INFO','Message Sent.','getAdsbStream');
        }

        this.vid_subc.onclose = function(){
            log('DEBUG','Connection closed.','getAdsbStream');
        }
        this.vid_subc.onerror = function(){
            log('ERR','Connection closed.','getAdsbStream');
        }

}
Video.prototype = {

    getVideoStream:function(cb){
        var socket = this.vid_subc;
        //this.ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        //ar socket = new WebSocket(this.ws_scheme+'://' + window.location.host + '/video');
        //console.log('hello888888888888888888888888888');
        sleep(200);
        socket.send('INVOKE');
        socket.onmessage = function (event){
            log('INFO','Message received.','getVideoStream');
            cb(event);
        }

        //if (socket.readyState == WebSocket.OPEN) {
        //  socket.send('INVOKE');
        //  log('INFO','Message Sent.','getVideoStream');
        //};

        /*socket.onopen = function (){
            log('DEBUG','Connection open.','getVideoStream');
            socket.send('INVOKE');//TODO
            log('INFO','Message Sent.','getVideoStream');
        }

        socket.onclose = function(){
            log('DEBUG','Connection closed.','getVideoStream');
        }

        socket.onerror = function(){
            log('ERR','Connection closed.','getVideoStream');
        }*/


    },
    killVideo:function(){
        var socket = this.vid_subc;
        for(var i=0;i<20;i++){
            socket.send('KILL');
            console.log('sent kill video');
            //socket.close();
        }

    },

}

//---------------------------------------------------------------------------------------------------------------
/* SESSION:
   A data management function to supervise all above communications.
   It is a collection of utilities to perform advanced operations on communication channels and data.*/
//---------------------------------------------------------------------------------------------------------------

var Session = function(){
    this.DefaultInstance = 'softsim';
    this.CurrentInstance = null;
    this.Master = false;
    this.sockets = [];

}
Session.prototype ={
    //TODO

    setCurrentInstance : function(instance){
        this.CurrentInstance = instance;
    },

    getCurrentInstance : function(){
        return this.CurrentInstance;
    },

    saveSockets : function(list){
        for(var i in list){
            this.sockets = this.sockets.concat(getSockets(list[i]));
        }
    },

    sendMessage : function(message,ws_obj,cb){



        ws_obj.onopen = function (){

            ws_obj.send(message);
        }
        ws_obj.onclose = function (){

            ws_obj.close();
        }
        ws_obj.onerror = function (){


        }
        ws_obj.onmessage = function (event){

            //log('INFO','got resp',event);
            cb(event);
            //socket.close();
        }
        if (ws_obj.readyState == WebSocket.OPEN) {

          ws_obj.onopen();
        };


    }
}


/*
console.log('___________________________');

protobuf.load("/static/proto/web.proto",function(err,root){
var wsr = root.lookupType("web.WebSocketReplyData");
var p = '\x08\x04"\x9a\x01\x08\x02\x10\x08\x1a\x93\x01\n\x90\x01\n\x1c\n\x1a/CFS/DS/CmdRejectedCounter\x12\x04\x08\x02(\x00\x1a\x04\x08\x02(\x00 \x96\xb0\x9f\xda\x8e,(\xbb\xa4\x8f\xe5\x9c\t0\x008\x01Z\x172018-01-12T16:50:05.326b\x171980-01-17T14:04:41.859\xb8\x01\xf2\xbb\x9f\xda\x8e,\xc2\x01\x172018-01-12T16:50:06.826'



var obj = wsr.toObject(p, {
  enums: String,  // enums as string names
  longs: String,  // longs as strings (requires long.js)
  bytes: String,  // bytes as base64 encoded strings
  defaults: true, // includes default values
  arrays: true,   // populates empty arrays (repeated fields) even if defaults=false
  objects: true,  // populates empty objects (map fields) even if defaults=false

});




console.log('success');
console.log(obj);
});





console.log('___________________________');

*/

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
