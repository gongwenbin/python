import os
import sys
def search(path,word,nuke6_store,i):
    for filename in os.listdir(path):
        fp=os.path.join(path,filename)
        if os.path.isfile(fp) and word in filename:
            #nuke6_store.append(i.strip()+os.linesep)
            if os.path.isdir("\\\\"+i.strip()+"\\l$"):
                nuke6_store.append(i.strip()+",L is OK"+os.linesep+os.path.getsize(fp))
            else:
                nuke6_store.append(i.strip()+",L no found"+os.linesep+os.path.getsize(fp))
        elif os.path.isdir(fp):
            search(fp,word,nuke6_store,i)
if __name__=='__main__':
    files=open('C:\\all_user_12.txt','r')
    nuke_user=files.readlines()
    files.close()
    nuke6_store=[]
    for i in nuke_user:
        pingnuke='ping -n 1 -w 1  %s' % i.strip()
        return1=os.system(pingnuke)
        if not  return1:
            str1="\\\\"+i.strip()+"\\c$\\Program Files (x86)"
            print str1
            if os.path.exists(str1):
                search("\\\\"+i.strip('\n')+"\\c$\\Program Files (x86)","LeoService.exe",nuke6_store,i)
    a=open('C:\\leo_user_12.txt','a')
    nuke_store=list(set(nuke6_store))
    a.writelines(nuke_store)
    a.close()
