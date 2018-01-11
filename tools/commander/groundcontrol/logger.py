import logging,coloredlogs
import json,os
coloredlogs.install()
#datefmt='%m/%d/%Y %I:%M:%S %p'
#logging.basicConfig(format="%(asctime)-15s - %(levelname)s - %(message)s",filename=os.path.dirname(__file__)+'/logs/django_server.log', filemode='w')
handlers = [logging.FileHandler(os.path.dirname(__file__)+'/logs/django_server.log'), logging.StreamHandler()]
logging.basicConfig(format="%(asctime)-15s - %(levelname)s - %(message)s",handlers = handlers, level=logging.DEBUG)
#logging.basicConfig(format="%(asctime)-15s - %(levelname)s - %(message)s")



#read configration file
with open(os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/scripts/launch_config.json', 'r') as f:
    json_obj = json.load(f)

log_level = str(json_obj['logging_level'])
log_level = log_level.strip("")

DEBUG = bool(log_level[0] == '1')
INFO = bool(log_level[1] == '1')
WARNING = bool(log_level[2] == '1')
ERROR = bool(log_level[3] == '1')
CRITICAL = bool(log_level[4] == '1')



def logd(s,*args,**kwargs):
    if DEBUG:
        logging.debug(s,*args,**kwargs)

def logi(s,*args,**kwargs):
    if INFO:
        logging.info(s,*args,**kwargs)

def logw(s,*args,**kwargs):
    if WARNING:
        logging.warning(s,*args,**kwargs)

def loge(s,*args,**kwargs):
    if ERROR:
        logging.error(s,*args,**kwargs)

def logc(s,*args,**kwargs):
    if CRITICAL:
        logging.critical(s,*args,**kwargs)

