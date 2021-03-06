from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from pyga.requests import Q

def shutdown():
    '''
    Fire all stored GIF requests One by One.
    You should call this if you set Config.queue_requests = True
    '''
    map(lambda func: func(), Q.REQ_ARRAY)
