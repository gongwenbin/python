# -*-coding:GB18030 -*-
import pycurl
import os
import time
import sys

URL="http://think.idmt.com.cn"
c=pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,1)
#c.setopt(pycurl,MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)
try:
    a=c.perform()\
        #.decode('UTF-8').encode('GBK')
except Exception, e:
    print "connection error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME=c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME=c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME=c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME=c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME=c.getinfo(c.TOTAL_TIME)
HTTP_CODE=c.getinfo(c.HTTP_CODE)
SIZ_DOWNLOAD=c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE=c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
print "HTTP״̬�룺 %s" %(HTTP_CODE)
print "DNS����ʱ�䣺%.2f ms" %(NAMELOOKUP_TIME*1000)
print "��������ʱ�䣺 %.2f ms" %(CONNECT_TIME*1000)
print "׼������ʱ�䣺 %.2f ms" %(PRETRANSFER_TIME*1000)
print "���俪ʼʱ�䣺 %.2f ms" %(STARTTRANSFER_TIME*1000)
print "���������ʱ�䣺 %.2f ms" %(TOTAL_TIME*1000)
print "�������ݰ���С�� %d bytes/s" %(SIZ_DOWNLOAD)
print "HTTPͷ����С�� %d byte" %(HEADER_SIZE)
print "ƽ�������ٶȣ� %d bytes/s" %(SPEED_DOWNLOAD)
indexfile.close()
c.close()