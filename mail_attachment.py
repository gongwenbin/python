# -*coding:GBK -*-
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


HOST="192.168.0.8"
SUBJECT=u"官网业务服务质量周报"
To="491657963@qq.com"
FROM="gongwenbin@idmt.com.cn"

def addimg(src,imgid):
    fp=open(src,'rb')
    msgImage=MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID',imgid)
    return msgImage

#构建html类型的文档正文
msg=MIMEMultipart('related')
msgtext=MIMEText("<font color=red>官网业务周平均:<br><img src=\"cid:weekly\"border=\"1\"><br>详细内容见附件。</font>","html","GB18030")
msg.attach(msgtext)

#将图片内置到html，需要先添加
msg.attach(addimg("iptables.jpg","weekly"))

#发送xlsx附件
attach=MIMEText(open("train_network.xlsx","rb").read(),"base64","utf-8")
attach["Content-Type"]="application/octet-stream"
attach["Content-Disposition"]="attachment;filename=\"train_network1网络.xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

#发送图片附件
attach=MIMEText(open("iptables.jpg","rb").read(),"base64","utf-8")
attach["Content-Type"]="application/octet-stream"

attach["Content-Disposition"]="attachment;filename=\"favicon1.jpg\""
msg.attach(attach)

#发送邮件
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