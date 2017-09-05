'''
Custom login user name and password of zabbix, and defines the URL of zabbix API, as well as the header information
'''
user = "Admin"
passwd = "Headway!@#0223."
url = "http://10.36.1.101/zabbix/api_jsonrpc.php"
#url = "http://119.4.208.78/zabbix/api_jsonrpc.php"
Header = {"Content-Type": "application/json-rpc"}