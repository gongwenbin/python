import os
import sys
def search(path,word,nuke9_store,i):
    for filename in os.listdir(path):
        fp=os.path.join(path,filename)
        if os.path.isfile(fp) and word == filename:
            if i not in nuke9:
                nuke9_store.append(i.strip()+os.linesep)
        elif os.path.isdir(fp) and "uke" in fp:
            search(fp,word,nuke9_store,i)
if __name__=='__main__':
    files=open('C:\\tools\\all_user.txt','r')
    nuke_user=files.readlines()
    files.close()
    file9list=open('C:\\nuke9_user.txt','r')
    nuke9=file9list.readlines()
    file9list.close()
    nuke9_store=[]
    for i in nuke_user:
        pingnuke='ping -n 1 -w 1  %s' % i.strip()
        return1=os.system(pingnuke)
        if not  return1:
            str1="\\\\"+i.strip('\n')+"\\c$\\tools64"
            print str1
            if os.path.exists(str1):
                search("\\\\"+i.strip('\n')+"\\c$\\tools64","Nuke9.0.exe",nuke9_store,i)
    a=open('C:\\nuke9_user.txt','a')
    b=list(set(nuke9_store))
    a.writelines(b)
    a.close()
