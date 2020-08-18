# -*- coding:utf-8 -*-
__author__ = 'DDS'


import requests   #先导入包,这是必须的
import json
import urllib.parse
import urllib.request

url = 'http://cms.dev.livenaked.com/blog/getBlogDetail'       #url:接口地址
data = {'siteId':'1','postName':'TestZX-001'}                        #data:接口传递的参数
headers = {'Connection':'close'}                        #header:传递header信息


# Post方法
def Post_requests(url,data,headers):
    response = requests.post(url, data=data,headers = headers)
    P = json.dumps(json.loads(response.text),indent=2,ensure_ascii=False);
    print('Post_JSON格式化数据 返回',P)
    Object_P = json.loads(response)  # = response.json() 方法
    return Object_P

# Get方法
def Get_requests(url,data,headers):
    response = requests.get(url, data,headers = headers)
    G = json.dumps(json.loads(response.text),indent=2,ensure_ascii=False);
    # print('Get_JSON格式化数据 返回',G)
    Object_G = json.loads(G)
    return Object_G

# 获取headers信息
def urllib_test(url,data):
    data1 = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.Request(url=url,data = data1)
    html = urllib.request.urlopen(response)
    # print(html.read())                    #获得 源数据
    print('状态 返回',html.getcode(),html.msg)          #获得 html返回的状态
    # print(html.headers)                   #返回 头部信息


if __name__ == '__main__':

    urllib_test(url,data) #获取头信息
    Post_requests(url,data,headers)