# -*- coding: utf-8 -*-
'''
Author:youlinbo
Create:20120319
Last edit:20141127
'''
import wmi
import sys,os
import xlwt
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def getserver():
    if os.path.exists('out.txt'):
        os.remove('out.txt')
        
    server = []
    
    for ln in file('serverconf.txt','r'):
        server.extend(ln.strip().split(' '))

    with open('out.txt', 'a+') as fp:
        fp.writelines('Server Partion Basic_size(GB) Free_size(GB) F_Percentage Share_name Share_path'+'\n')
        fp.writelines('Server Partion Basic_size(GB) Free_size(GB) F_Percentage Share_name Share_path'+'\n')

    for i in range(len(server)):
        try:
            c = wmi.WMI (server[i-1])
            caption = []
            free = []
            size = []
            for disk in c.Win32_LogicalDisk (DriveType=3):
                free = float(disk.FreeSpace) / (1024*1024*1024)
                size = float(disk.Size) / (1024*1024*1024)
                fpoint = (str(free/size*100))[:5]
                for share in c.Win32_Share():
                    if share.Name.find('$') == -1:
                        if size > 200 and disk.Caption == share.Path[:2]:
                            with open('out.txt', 'a+') as fp:
                                fp.writelines('%s' %server[i-1] + ' ' + disk.Caption + ' ' + '%.2f' %size + ' ' +
                                              '%.2f' %free + ' ' + fpoint+'%' + ' ' + '%s' %share.Name + ' ' + share.Path + '\n')

        except:
            with open('out.txt', 'a+') as fp:
                fp.writelines('%s' %server[i-1] + ' ' + 'Error' + ' ' + 'Error' + ' ' + 'Error' + ' '
                              + 'Error' + ' ' + 'Error' + ' ' + 'Error' + '\n')

def wexcel(txt):
    now = datetime.datetime.now()
    xlsfileneme = now.strftime("%Y%m%d") + "_server_disk_stat.xls"
    txtfile = open(txt)
    st = txtfile.read()
    lines = st.split('\n')
    wb = xlwt.Workbook()
    ws = wb.add_sheet("driver",cell_overwrite_ok=True)
    
    fnt = xlwt.Font()
    fnt.name = 'Arial'
    fnt.colour_index = 0
    fnt.bold = True
    
    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style = xlwt.XFStyle()
    style.font = fnt
    style.borders = borders

    fnt1 = xlwt.Font()
    fnt1.name = 'Arial'
    fnt1.colour_index = 10
    fnt1.bold = True
    
    borders1 = xlwt.Borders()
    borders1.left = 6
    borders1.right = 6
    borders1.top = 6
    borders1.bottom = 6

    style1 = xlwt.XFStyle()
    style1.font = fnt1
    style1.borders = borders1

    for i in range(1,len(lines)):
        lin = lines[i].split(' ')
        for j in range(0,len(lin)):
        #前一行和本行的第j个元素相同但是要是同一台服务器才合并
            if (lines[i-1].split(' '))[j] == (lines[i].split(' '))[j] and \
               (lines[i-1].split(' '))[0] == (lines[i].split(' '))[0]:
                ws.write_merge(i-1,i,j,j,lin[j],style)
            else:
                ws.write(i,j,lin[j],style)
            if i >1 and j == 4:
                if (lines[i-1].split(' '))[4] == (lines[i].split(' '))[4]:
                    #percentage = float((lin[4])[0:4])
                    percentage = (lin[4])[0:4]
                    if percentage < str(30):
                        ws.write_merge(i-1,i,4,4,lin[4],style1)

    ws.col(0).width = 0xfa0
    ws.col(1).width = 0x7d0
    ws.col(2).width = 0xfa0
    ws.col(3).width = 0xfa0
    ws.col(4).width = 0xdac
    ws.col(5).width = 0x1770
    ws.col(6).width = 0x2ee0    
    wb.save(xlsfileneme)
    txtfile.close()

def sendMail(to, subject, text, files=[],server="localhost"):
    assert type(to)==list
    assert type(files)==list
    fro = "youlinbo <youlinbo@idmt.com.cn>"

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text,'plain','utf-8'))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()

if __name__ == '__main__':
    getserver()
    wexcel('out.txt')
    #os.remove('out.txt')
    mail = []
    for ln in file('mailconf.txt','r'):
        mail.extend(ln.strip().split(' '))
    fil = datetime.datetime.now().strftime("%Y%m%d") + "_server_disk_stat.xls"
    sendMail(mail, "windows服务器磁盘空间周统计", "windows服务器磁盘空间周统计,见附件.目前的功能：统计磁盘剩余空间以及比例，对剩余空间少于30%的标红。", \
         [fil],"mailsz.idmt.com.cn") 
