# -*coding:GBK -*-
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


HOST="192.168.0.8"
SUBJECT=u"����ҵ����������ܱ�"
To="491657963@qq.com"
FROM="gongwenbin@idmt.com.cn"

def addimg(src,imgid):
    fp=open(src,'rb')
    msgImage=MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID',imgid)
    return msgImage

#����html���͵��ĵ�����
msg=MIMEMultipart('related')
msgtext=MIMEText("<font color=red>����ҵ����ƽ��:<br><img src=\"cid:weekly\"border=\"1\"><br>��ϸ���ݼ�������</font>","html","GB18030")
msg.attach(msgtext)

#��ͼƬ���õ�html����Ҫ�����
msg.attach(addimg("iptables.jpg","weekly"))

#����xlsx����
attach=MIMEText(open("train_network.xlsx","rb").read(),"base64","utf-8")
attach["Content-Type"]="application/octet-stream"
attach["Content-Disposition"]="attachment;filename=\"train_network1����.xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

#����ͼƬ����
attach=MIMEText(open("iptables.jpg","rb").read(),"base64","utf-8")
attach["Content-Type"]="application/octet-stream"

attach["Content-Disposition"]="attachment;filename=\"favicon1.jpg\""
msg.attach(attach)

#�����ʼ�
msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=To
try:
    server=smtplib.SMTP()
    server.connect(HOST,'25')
    server.set_debuglevel(1)
    server.login("gongwenbin@idmt.com.cn","123idmt456")
    server.sendmail(FROM,To,msg.as_string())
    server.quit()
except Exception,e:
    print "faild:"+str(e)