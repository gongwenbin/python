# -*coding:GBK -*-
import os
import httplib
import dns.resolver

#解析域名A记录，并通过httplib探测主机是否正常
def get_iplist(domain=""):
    try:
        A=dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True
def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":appdomain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent.strip() in "<!DOCTYPE html":
            print ip+" [OK]"
        else:
            print ip+" [Error]"
if __name__=="__main__":
    iplist=[]
    appdomain="idmt.com.cn"
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error"
