import json
import urllib2
from Config import config
from login_auth.auth import ReqToken

class Get_item_id(object):
    def __init__(self):
        self.token = ReqToken().authToken()
        self.URL = config.url
        self.Header = config.Header

    def GetItemsID(self, hostid, items):
        jsondata = json.dumps({
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "itemids",
                "hostids": hostid,
                "search": {"key_": items}
            },
            "auth": self.token,
            "id": 1
        })
        req = urllib2.Request(url=self.URL, headers=self.Header, data=jsondata)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
        try:

            return data["result"][0]["itemid"]
        except IndexError:
            return 0

#A=Get_item_id()
#A.GetItemsID(10699,"get.sda.ws")