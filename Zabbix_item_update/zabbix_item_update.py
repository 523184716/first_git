from Config import config
from login_auth.auth import ReqToken
import  json
import urllib2

class ItemData(object):
    get_sda_ws = "get.sda.ws"
    get_sda_rs = "get.sda.rs"
    get_sda_riops = "get.sda.riops"
    get_sda_rkb = "get.sda.rkb"
    get_sda_wiops = "get.sda.wiops"
    get_sda_wkb = "get.sda.wkb"

    def __init__(self):
        self.token = ReqToken().authToken()
        self.URL = config.url
        self.Header = config.Header


    def Item_Statu_update(self,itemid):
        jsondata = json.dumps({
                    "jsonrpc": "2.0",
                     "method": "item.update",
                     "params": {
                         "itemid": itemid,
                         "status": 1
                     },
                    "auth": self.token,
                     "id": 1
        })
        req = urllib2.Request(url=self.URL, headers=self.Header, data=jsondata)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
       # print data
        return data.get("result")

#A=CpuData()
#A.Item_Statu_update(86090)