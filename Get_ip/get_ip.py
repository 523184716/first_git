import json
import urllib2
from Config import config
from login_auth.auth import ReqToken
import  re

class Publicdata(object):
    def __init__(self):
        self.token = ReqToken().authToken()
        self.URL = config.url
        self.Header = config.Header

    def GetHostID(self):
        jsondata = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["name","hostid"],
                "selectInterfaces": ["ip"],
                "selectGroups": []
        },
            "auth": self.token,
            "id": 0
        })
        req = urllib2.Request(url=self.URL, headers=self.Header, data=jsondata)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
        ip_list = {}
        regex = re.compile("10.36.8.")
        for i in data.get("result"):
            ip = i["interfaces"][0]["ip"]
            match = regex.search(ip)
            if match:
                hostid = i["hostid"]
                ip_list[hostid] = ip
            else:
                pass
        #print  ip_list
        return  ip_list
        #return data.get("result")



#A=Publicdata()
#A.GetHostID()