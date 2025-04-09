# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import time
import json
#import pyodbc
import random
import sys
import hashlib

from inc import fun
import os

#============================时间到强制结束线程
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

#=============================

def get_htmll(urll, p=0, dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    try:
        req = request.Request(urll, headers=headers)
        with request.urlopen(req, timeout=120) as resp:
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            #with open('aaa.txt', 'a', encoding='utf-8', newline='\r\n') as f:
                #f.write(htmll)
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(str(p)+"\r\n")
        return htmll


def get_htmll2(urll, p, dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    #headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36'}
    
    #data={"areaSn":"","entType":"02","entName":"","pageIndex":p}
    data={"jjrSel":"","p":p}
    data=urllib.parse.urlencode(data)
    data=bytes(data,'utf-8')
    
    try:
        #req = request.Request(urll, headers=headers)
        req = request.Request(urll, headers=headers, data=data, method="POST")
        with request.urlopen(req, timeout=120) as resp:
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            #with open('aaa.txt', 'a', encoding='utf-8', newline='\r\n') as f:
                #f.write(htmll)
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(str(p)+"\r\n")
        return htmll


if __name__ == "__main__":

    www=["%","环比","同比","上涨","下跌","占比","上升","下降","环比%","同比%","上涨%","下跌%","占比%","上升%","下降%","率%"]
    ddd2={}

    with open('Data\\000_all_data.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        ddd=json.loads(f.read())

    #a="2022-10-22"
    a=ddd[list(ddd.keys())[-1]]
    n=0

    for dd in ddd.keys():
        if ddd[dd]==a and dd[-3:]!="..." and (pos_r:=dd.find("%"))>-1:
            pos_l=pos_r-1
            while pos_l>=0:
                if "1234567890.".find(dd[pos_l])>-1:
                    pos_l-=1
                else:
                    pos_l=pos_l+1
                    break

            if pos_l==-1:
                pos_l=0
            k=dd[pos_l:pos_r]
            
            for ww in www:
                if dd.find(ww)>-1:
                    k+=ww

            if dd.find("%")>-1 and (dd.find("年")>-1 or dd.find("月")>-1 or dd.find("日")>-1 or dd.find("季度")>-1 or dd.find("周")>-1):
            #if 1==1:
                if k not in ddd2.keys():
                    ddd2[k]=[dd,1]
                    n+=1
                else:
                    ddd2[k][1]+=1
                    
            #print(dd)

    ddd3=sorted(ddd2.values(),key=lambda x: x[1],reverse=True)
    for dd3 in ddd3:
        if dd3[0].find("下跌")>-1 or dd3[0].find("下降")>-1:
            print(f"▼{dd3[0]}")
        else:
            print(dd3[0])

##    for dd2 in ddd2.keys():
##        print(dd2)
##        print(ddd2[dd2])

    print(f"总计：{n}")
    print("--end--")


while (x:=input("输入X退出：")):
    if x=="x" or x=="X":
        print("--end--")
        break
    
                
                

