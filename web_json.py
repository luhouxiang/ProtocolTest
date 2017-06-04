#!/usr/bin/evn python3
#coding=utf-8

# 针对web端json协议的通信库，通信协议为json,传出的data为json格式，接收的数据也是json格式
# 外界调用时可先初始化web_json类，如下所示：
# get调用
# web = WebJson("http://baidu.com/")
# params = "abcd/select/100000?userID=1234&groupID=79"
# web.get(params)
# 
# post调用
# web = WebJson("http://baidu.com/")
# params = "abcd/select/100000"
# data = '{"name": "jack", "id": "1"}'
# web.post(params, data)

from urllib.request import urlopen
import json

class WebJson(object):
    def __init__(self):
        pass

        
    def get_url_data(self, url, data):
        web = urlopen(url, data)
        print (web.url)
        print ("status: " , web.status)
        rawtext = web.read()
        jsonStr = json.loads(rawtext.decode('utf8'))   
        
        jsonStr = json.dumps(jsonStr, sort_keys=False, ensure_ascii= False, indent=2)
        print(jsonStr)
        return jsonStr       
    
    # get方法
    def get(self, url):
        return self.get_url_data(url, None)
    
    # post方法
    def post(self, url, data):
        data=bytes(data, 'utf8')
        return self.get_url_data(url, data)


if __name__ == '__main__':
    rawtext = '{"name":"jack", "value":"1"}'
    json_str = json.loads(rawtext) 
    str_list = []
    str = None
    if (isinstance(json_str, dict)):
        for item in json_str:
            str_list.append(item+"="+json_str[item])
            print ("key:", item,", value:" ,json_str[item])
    if len(str_list) != 0:
        str = "&".join(str_list)
    print(str)
    print(len(str))
    #print(len(None))
        
        