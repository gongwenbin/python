#-*- coding: GBK -*-
'''通过创建多线程来处理windows命令，并把结果写入的文件'''
import datetime,time
import os
import threading
import subprocess
nuke_user=open('C:\\nuke_user.txt','r')
nuke_kill=open('C:\\tools\\2222.txt','a')
def execCmd(cmd):
        return3=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        strtime=cmd+'\t'+time.ctime()
        nuke_kill.write(strtime+return3.stdout.read()+'\n')
if __name__ == '__main__':
    nukebat=[]
    for i in nuke_user:
        pingnuke='ping -n 1 -w 1  %s' % i
        return1=os.system(pingnuke)
        if not  return1:
            print 'YES'
            nukebat.append(str('taskkill /F /S '+i.strip('\n')+' /U Administrator /P TapeLibrary /FI "IMAGENAME eq nuke7*"'))
            nukebat.append(str('taskkill /F /S '+i.strip('\n')+' /U Administrator /P TapeLibrary /FI "IMAGENAME eq nuke6*"'))
    threads = []

    for cmd in nukebat:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

