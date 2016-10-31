import os
import sys
def search(path,word):
    for filename in os.listdir(path):
        fp=os.path.join(path,filename)
        if os.path.isfile(fp) and word in filename:
            nuke9.write(fp+'\n')
        elif os.path.isdir(fp) and "uke" in fp:
            search(fp,word)
nuke_user=open('F:\\nuke_user.txt','r')
nuke9=open('F:\\nuke9.txt','a')
for i in nuke_user:
    pingnuke='ping -n 1 -w 1  %s' % i.strip()
    return1=os.system(pingnuke)
    if not  return1:
        str1="\\\\"+i.strip('\n')+"\\c$\\tools64"
        print str1
        if  os.path.exists(str1):
            search("\\\\"+i.strip('\n')+"\\c$\\tools64","Nuke9.0.exe")