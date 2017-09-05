
from Get_ip import  get_ip
from Get_item_id import get_item_id
from Zabbix_item_update import zabbix_item_update

item_list = ["get.sda.ws","get.sda.rs","get.sda.riops","get.sda.rkb","get.sda.wiops","get.sda.wkb"]

total = {}
host_list = get_ip.Publicdata().GetHostID()
print host_list
for host,ip in get_ip.Publicdata().GetHostID().items():
    for items in item_list:
        itemid = get_item_id.Get_item_id().GetItemsID(host,items)
        print ip, host, items,itemid
        zabbix_item_update.ItemData().Item_Statu_update(itemid)