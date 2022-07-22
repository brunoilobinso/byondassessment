import os

class BaseConfig(object):
    
    REDIS_HOST = Redis(os.environ['REDIS_HOST'])
    REDIS_PORT = os.environ['REDIS_PORT']
    BIND_PORT = int(os.environ['BIND_PORT'])

