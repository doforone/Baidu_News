import random
import hashlib
import time
from math import *
from urllib import request as requestt, parse
from urllib.parse import quote, unquote

from flask import request,session

#----------------------
def abc123(sss):
    rrr=set()
    aaa="abcdefghijklmnopqrstuvwxyz"
    bbb="1234567890"
    p=0
    t=""
    sss=sss.replace(","," ").replace("."," ").replace("，"," ").replace("。"," ")\
         .replace("("," ").replace(")"," ").replace("（"," ").replace("）"," ")\
         .replace("_"," ").replace("-"," ").replace(":"," ").replace("："," ")
    sss=(sss+".").lower()  #转换为小写
    for i in range(1,len(sss)):
        if ord(sss[i])<=255:
            if sss[i] not in aaa and sss[i] not in bbb:
                if sss[p:i].isalpha():
                    rrr.add(sss[p:i][:3])  #取英文单词的前3个，一般为字根
                elif sss[p:i].isdigit():
                    rrr.add(sss[p:i])
                elif sss[p:i].isalnum():
                    rrr.add(sss[p:i])
                p=i+1
        else:
            if sss[p:i].isalpha() or sss[p:i].isdigit():
                rrr.add(sss[p:i])
            rrr.add(sss[i])
            p=i+1
    return rrr


def at_acc(atacc):
     aaa="0123456789abcdefghijklmnopqrstuvwxyz"
     if (pos:=atacc.find("@"))>-1:
          pos+=1
          pos_l=pos
          lenn=len(atacc)
          while pos<lenn:
               if aaa.find(atacc[pos])>-1:
                    pos+=1
               else:
                    break
          return atacc[pos_l:pos]
     else:
          return ""


def cre_acc():
    aaa=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f",
         "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    acc=f"{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}"
    return acc


def cre_pw():
    aaa=["0","1","2","3","4","5","6","7","8","9"]
    pw=f"{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}{random.choice(aaa)}"
    return pw


def del_tag2(html):
    pos_l=0
    pos_r=0
    while True:
        pos_l=html.find("<",pos_l)
        if pos_l==-1:
            break
        else:
            pos_r=html.find(">",pos_l)
            if pos_r==-1:
                break
            else:
                html=html[0:pos_l]+html[pos_r+1:]
    return html


def find_mob(xx):
##    xx=str(xx)
##    if (pos:=xx.find("1"))<=len(xx)-11:
##        if (mob:=xx[pos:pos+11]).isdigit():
##            xx=xx.replace(mob,f"<a href='tel:{mob}' class=a2>{mob}</a>")

    return xx


def split_str(sss):
     sss=sss.replace("（","(")
     sss=sss.replace("）",")")

     while True:
          if sss.find("((")>-1:
               sss=sss.replace("((","(")
          else:
               break
          
     while True:
          if sss.find("))")>-1:
               sss=sss.replace("))",")")
          else:
               break

     sss=sss.replace("()","")
     
     a_b=sss
     ab=[]
     AB=""
     pos_l=0
     pos_r=0

     while True:
          if (pos_l:=sss.find("(",pos_l))>-1:
               if (pos_r:=sss.find(")",pos_l))>-1:
                    AB=sss[pos_l+1:pos_r]
                    a_b=a_b.replace(AB,"")
                    AB=AB.replace("(","")
                    ab.append(AB)
                    pos_l=pos_r
               else:
                    break
          else:
               break

     a_b=a_b.replace("(","")
     a_b=a_b.replace(")","")

     ab_join="".join(ab)
     a_b_2=a_b
     for w in a_b_2:
         if ab_join.find(w)>-1:
             a_b=a_b.replace(w,"")
             
     return a_b,ab
    

def abc(s):
    s=set(s)
    s=list(s)
    s.sort(reverse=False)
    s = "".join(s)
    return s


def sear_abc(aaa,bbb):  #在b中查找a
    rrr=True
    pos_l=-1
    for aa in aaa:
        if (pos_l:=bbb.find(aa,pos_l+1))==-1:
            rrr=False
            break
##        else:
##            pass
    return rrr

#--------------------------

def req(xx):
    xx=str(xx)
    aa=""
    if request.method == 'GET':
        if xx in request.args.keys():
            aa=request.args[xx]
    if request.method == 'POST':
        if xx in request.form.keys():
            aa=request.form[xx]
    return aa


def sessionn(xx):
    if xx in session.keys():
        rrr=session[xx]
    else:
        rrr=""
    return rrr


def time_str(xx):
    timeArray = time.localtime(xx)
    rrr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return rrr


def dictt(dict,key):
    if key in dict:
        return dict[key]
    else:
        return ""


def ip():  #IPv4转int
    if "X-Real-IP" in request.headers:
        ip=request.headers["X-Real-IP"]
    else:
        ip=request.remote_addr
    return ip


def ip_int(ip):  #IPv4转int
    lll=ip.split(".")
    ip_int=int(lll[0])*16777216+int(lll[1])*65536+int(lll[2])\
            *256+int(lll[3])-2147483648
    return ip_int


def int_ip(intt):  #int转IPv4
    intt+=2147483648
    a=divmod(intt, 16777216)
    int_ip=str(a[0])
    a=divmod(a[1], 65536)
    int_ip+="."+str(a[0])
    a=divmod(a[1], 256)
    int_ip+="."+str(a[0])+"."+str(a[1])
    return int_ip


def ran_str(intt):  #随机字符串
    #ran_str=''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', intt))
    return ''.join(random.sample(\
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', intt))


def md5(strr):  #输出字符串的md5值
    #md5=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()
    return hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()


def timee():  #时间戳（秒）整型
    return int(time.time())-2147483648


def yxyx16(x, y, id):  # x为实际经度*1000000
    x = 180*1000000 + x  # 以东经180度为边界，因为在太平洋，人口稀少。xx始终为+
    a = bin(int(x))[2:]
    y = 90*1000000 - y  # 以北极为0。yy始终为+
    b = bin(int(y))[2:]

    if (len_a := len(a)) > (len_b := len(b)):
        b = b.zfill(len_a)
    else:
        a = a.zfill(len_b)

    yxyx16=""
    for i in range(len(a)):
        yxyx16 += b[i] + a[i]

    yxyx16 = hex(int(yxyx16, 2))[2:]
    yxyx16 = yxyx16.zfill(15)

    id += 2147483648
    yxyx16 += hex(id)[2:].zfill(8)

    return yxyx16


def yxyx10(x, y):  # x为实际经度*1000000
    x = int(x/100)
    x = 180*10000 + x  # 以东经180度为边界，因为在太平洋，人口稀少。xx始终为+
    a = bin(int(x))[2:]

    y = int(y/100)
    y = 90*10000 - y  # 以北极为0。yy始终为+
    b = bin(int(y))[2:]

    if (len_a := len(a)) > (len_b := len(b)):
        b = b.zfill(len_a)
    else:
        a = a.zfill(len_b)

    yxyx10=""
    for i in range(len(a)):
        yxyx10 += b[i] + a[i]

    yxyx10 = int(yxyx10, 2)
    return yxyx10


def ab_sort16(x, y, lll):  # x为实际经度*1000000
    o = yxyx16(x, y, 2147483647)
    
    for ll in lll:
        ll[1] = abs(int(o,16)-int(ll[1],16))

    lll=sorted(lll, key = lambda k: k[1])

    return lll


def ab_sort10(lll, x, y, a, b):  # x为实际经度*1000000
    o = yxyx10(x, y)*1000000+999999
    for ll in lll:
        ll[1] = abs(o-ll[0])

    lll=sorted(lll, key = lambda k: k[1])

    if (lenn:=len(lll))>=20:
        lenn=19
        for i in range(lenn,0,-1):
            if lll[i][1]!=lll[i-1][1]:
                lll=lll[:i]
                break
    else:
        lenn-=1

    if lenn>=0:
        if (min_lll:=min(lll)[0])<a:
            a=min_lll

        if (max_lll:=max(lll)[0])>b:
            b=max_lll

    return lll,a,b


def geoDistance(lng1,lat1,lng2,lat2):
    '''
    公式计算两点间距离（m）
    '''
    #经纬度转换成弧度
    lng1,lat1,lng2,lat2=map(radians,[float(lng1),float(lat1),float(lng2),float(lat2)]) 
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
    distance=2*asin(sqrt(a))*6371*1000   # 地球平均半径，6371km
    distance=round(distance,3)
    return distance
 
 
def geoDegree(lng1,lat1,lng2,lat2):
    '''
    公式计算两点间方位角
    方位角：是与正北方向、顺时针之间的夹角
    '''
    lng1,lat1,lng2,lat2=map(radians,[float(lng1),float(lat1),float(lng2),float(lat2)]) 
    dlon=lng2-lng1
    y=sin(dlon)*cos(lat2)
    x=cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(dlon)
    brng=degrees(atan2(y,x))
    brng=(brng+360)%360

    if brng>=337.5 or brng<22.5:
        brng="↑"
    elif brng>=22.5 and brng<67.5:
        brng="↗"
    elif brng>=67.5 and brng<112.5:
        brng="→"
    elif brng>=112.5 and brng<157.5:
        brng="↘"
    elif brng>=157.5 and brng<202.5:
        brng="↓"
    elif brng>=202.5 and brng<247.5:
        brng="↙"
    elif brng>=247.5 and brng<292.5:
        brng="←"
    elif brng>=292.5 and brng<337.5:
        brng="↖"
    
    return brng


#!/usr/bin/env python
# coding:utf-8
# @author: KaiVen
"""
GPS坐标转换：
WGS-84：是国际标准，GPS坐标（Google Earth使用、或者GPS模块）
GCJ-02：中国坐标偏移标准，Google Map、高德、腾讯使用
BD-09：百度坐标偏移标准，Baidu Map使用
"""

import math


def transformLat(x, y):
    # 转换经度
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return ret


def transformLon(x, y):
    # 转换纬度
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
    return ret


def delta(lat, lng):
    a = 6378245.0
    # a: 卫星椭球坐标投影到平面地图坐标系的投影因子
    ee = 0.00669342162296594323
    # ee: 椭球的偏心率
    dLat = transformLat(lng - 105.0, lat - 35.0)
    dLon = transformLon(lng - 105.0, lat - 35.0)
    radLat = lat / 180.0 * math.pi
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    return dLat, dLon


def wgs2gcj(wgsLat, wgsLng):
    """
    WGS-84转成GCJ-02
    """
    if outOfChina(wgsLat, wgsLng):
        #print("The latitude or longitude is out of China!")
        return wgsLat, wgsLng
    lat, lng = delta(wgsLat, wgsLng)
    return wgsLat + lat, wgsLng + lng


def gcj2wgs_rough(gcjLat, gcjLon):
    """
    GCJ-02 转 WGS-84 粗略版
    """
    if outOfChina(gcjLat, gcjLon):
        #print("The latitude or longitude is out of China!")
        return gcjLat, gcjLon
    lat, lng = delta(gcjLat, gcjLon)
    return gcjLat - lat, gcjLon - lng


def gcj2wgs_accurate(gcjLat, gcjLon):
    """
    GCJ-02 转 WGS-84 精确版
    """
    initDelta = 0.01
    threshold = 0.000000001
    dLat = initDelta
    dLon = initDelta
    mLat = gcjLat - dLat
    mLon = gcjLon - dLon
    pLat = gcjLat + dLat
    pLon = gcjLon + dLon
    wgsLat = 0
    wgsLon = 0
    i = 0
    while 1:
        wgsLat = (mLat + pLat) / 2
        wgsLon = (mLon + pLon) / 2
        lat, lon = gcj2wgs_rough(wgsLat, wgsLon)
        dLat = lat - gcjLat
        dLon = lon - gcjLon
        if (abs(dLat) < threshold) and (abs(dLon) < threshold):
            break
        if dLat > 0:
            pLat = wgsLat
        else:
            mLat = wgsLat
        if dLon > 0:
            pLon = wgsLon
        else:
            mLon = wgsLon
        if ++i > 10000:
            break
    return wgsLat, wgsLon


def gcj2bd(gcjLat, gcjLon):
    """
    GCJ-02 转 BD-09
    """
    x_pi = math.pi * 3000.0 / 180.0
    x = gcjLon
    y = gcjLat
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    bdLon = z * math.cos(theta) + 0.0065
    bdLat = z * math.sin(theta) + 0.006
    return bdLat, bdLon


def bd2gcj(bdLat, bdLon):
    """
    BD-09 转 GCJ-02
    """
    x_pi = math.pi * 3000.0 / 180.0
    x = bdLon - 0.0065
    y = bdLat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gcjLon = z * math.cos(theta)
    gcjLat = z * math.sin(theta)
    return gcjLat, gcjLon


def wgs2mercator(wgsLat, wgsLon):
    """
    WGS-84 to Web mercator
    mercatorLat -> y mercatorLon -> x
    """
    x = wgsLon * 20037508.34 / 180.
    y = math.log(math.tan((90. + wgsLat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180.
    return y, x


def mercator2wgs(mercatorLat, mercatorLon):
    """
    Web mercator to WGS-84
    mercatorLat -> y mercatorLon -> x
    """
    x = mercatorLon / 20037508.34 * 180
    y = mercatorLat / 20037508.34 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180.)) - math.pi / 2)
    return y, x


def outOfChina(lat, lng):
    """
    判断是否在中国范围外
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


def haversine(lat1, lon1, lat2, lon2):
    """
    :param: 纬度1，经度1，纬度2，经度2（十进制度数）
    :return: 二个坐标之间的距离（单位米）
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def company(con):
    con=con.replace("（传真：", "≌")
    con=con.replace("  ", " ")
    con_str="1234567890- １２３４５６７８９０/"
    con_str2="1234567890-１２３４５６７８９０"

    con_pos0=0
    con_pos=0
    loop_pos=0

    aaa={"phone":"","person":"","mob":"","comp":"","fax":"","add":"","qq":"","email":"","prod":"","http":""}
    
    while con_pos<(con_len:=len(con)):
        if loop_pos==0:  #电话
            if con[con_pos]==" ":
                phone=con[con_pos0:con_pos].strip()
                if (pos_l:=phone.find("-"))>-1:
                    phone_l=phone[:pos_l]
                    if phone_l=="0086" or phone_l=="086" or phone_l=="86":
                        phone=phone[pos_l+1:]
                    if phone[0]!="0" and phone[:3]!="400" and phone[:3]!="800":
                        phone="0"+phone
                con_pos0=con_pos
                loop_pos+=1
                if len(phone)<7:
                    phone=""
                aaa["phone"]=phone

        elif loop_pos==1:  #姓名
            if con[con_pos]==" ":
                person=con[con_pos0:con_pos].strip()
                con_pos0=con_pos
                loop_pos+=1
                aaa["person"]=person

        elif loop_pos==2:  #手机
            if con_str2.find(con[con_pos])==-1:
                mob=con[con_pos0:con_pos].strip()
                con_pos0=con_pos
                loop_pos+=1
                if len(mob)<11:
                    mob=""
                aaa["mob"]=mob

        elif loop_pos==3:  #企业名称
            if con[con_pos]=="≌":
                comp=con[con_pos0:con_pos].strip()
                con_pos0=con_pos
                loop_pos+=1
                aaa["comp"]=comp

        elif loop_pos==4:  #传真
            if con[con_pos]=="）":
                fax=con[con_pos0+1:con_pos].strip()
                if (pos_l:=fax.find("-"))>-1:
                    fax_l=fax[:pos_l]
                    if fax_l=="0086" or fax_l=="086" or fax_l=="86":
                        fax=fax[pos_l+1:]
                    if fax[0]!="0" and fax[:3]!="400" and fax[:3]!="800":
                        fax="0"+fax
                con_pos0=con_pos
                loop_pos+=1
                if len(fax)<7:
                    fax=""
                aaa["fax"]=fax

        elif loop_pos==5:  #地址
            add=con[con_pos0+2:]
            add=add.replace("中国 ", "")

            ttt=add.split("〓")
            
            tt0=ttt[0].split("|")
            if len(tt0)==3:
                aaa["add"]=tt0[0]
                aaa["qq"]=tt0[1].replace(":","：")
                aaa["email"]=tt0[2]
            else:
                aaa["add"]=tt0[0]

            tt1=ttt[1].split("‖")
            if len(tt1)==2:
                aaa["prod"]=tt1[0]
                aaa["http"]=tt1[1]
            else:
                aaa["prod"]=tt1[0]

        con_pos+=1
    return aaa
        

def remark(con):
    aaa={"remark":"","url":""}
    ttt=con.split("‖")
    if len(ttt)==2:
        aaa["remark"]=ttt[0]
        aaa["url"]=ttt[1]
    else:
        aaa["remark"]=ttt[0]

    return aaa


def img(con):
    aaa={"img":"","w":0,"h":0}
    ttt=con.split("*")
    if len(ttt)==3:
        aaa["img"]=ttt[0]
        aaa["w"]=int(ttt[1])
        aaa["h"]=int(ttt[2])
    else:
        aaa["img"]=ttt[0]

    return aaa


def model(con):
    if con==1:
        aaa="生产厂家"
    elif con==2:
        aaa="经销批发"
    elif con==3:
        aaa="招商代理"
    elif con==4:
        aaa="商业服务"
    else:
        aaa="其他组织"

    return aaa


def baidu(address, data=None):
    """
    请求页面，这个函数要用线程，长时间不响应就杀死线程，
    参数5秒有时不起作用。
    """
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url="http://api.map.baidu.com/geocoding/v3/?address="+quote(address.encode("utf-8"))+"&output=json&ak=9QTTGVUaCdxhVu8eA2XzwyMseHOwn8s6"
    
    try:
        if data:
            data=data.encode('utf-8')
        req = requestt.Request(url, data, headers=headers)
        with requestt.urlopen(req, timeout=4) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        #print(e)
        return "{'status': -1}"


def same_url(domain):
    if "referer" in request.headers:
        ref_url=request.headers["referer"]
    else:
        ref_url=""

    if ref_url.find(domain)>-1:
        rrr=1
    else:
        rrr=0

    return rrr
