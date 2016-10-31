# -*coding:GBK -*-
#ping ip,如果10个里面超过3个丢包，就发送邮件
import os
import time
import datetime
import subprocess
import smtplib
import string

def testhaha():
    pass
def go_mail(result):
    HOST="smtp.idmt.com.cn"
    SUBJECT="ping mail.gdc-world.com"
    To='491657963@qq.com'
    FROM="gongwenbin@idmt.com.cn"
    text=str(datetime.datetime.now())
    for a in result:
        text=text+a
    BODY=string.join((
        "From: %s" %FROM,
        "To: %s" %To,
        "Subject: %s" % SUBJECT,
        "",
        text
    ),"\r\n")
    server=smtplib.SMTP()
    server.connect(HOST,"25")
    server.login("gongwenbin","123idmt456")
    server.sendmail(FROM,[To],BODY)
    server.quit()

def go_ping():
    iplist=['mail.google.com',]
    while 1:
        for i in iplist:
            result_ping=[]
            pingnuke='ping -n 1 -w 1  %s' % i
            n=0
            j=0
            for n in range(0,10):
                return3=subprocess.Popen(pingnuke,stdout=subprocess.PIPE,shell=True)
                result_ping.append(return3.stdout.read())
                print result_ping[n]
                if 'time=' not in result_ping[n]:
                    j=j+1
                    if j >3:
                        print "network faild"
                        go_mail(result_ping)
                        break
        time.sleep(60)

if __name__=="__main__":
    go_ping()
