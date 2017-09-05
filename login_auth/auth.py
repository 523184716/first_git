#coding=utf-8
from Config import config
import urllib2
import json

class ReqToken(object):
    '''
    Through effective account login and password zabbix, and returns a token.
    Can take this token to get any support access to data
    '''
    def __init__(self):
        self.user = config.user
        self.passwd = config.passwd
        self.URL = config.url
        self.Header = config.Header

    def authToken(self):
        try:
            jsondata = json.dumps({
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {"user": self.user,"password": self.passwd},
                "id": 0
            })
            req = urllib2.Request(url=self.URL, headers=self.Header, data=jsondata)
            response = urllib2.urlopen(req)
            token = json.loads(response.read())
            #print token["result"]
            return token["result"]
        except Exception, e:
            print Exception,":",e

#A=ReqToken()
#A.authToken()