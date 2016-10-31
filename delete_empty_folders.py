# -*coding:UTF-8 -*-

#查找空文件夹，并删除它
import os
import sys
emptyfolder=[]
def delete_null_dir(dirr):
    if os.path.isdir(dirr):
        for p in os.listdir(dirr):
            d=os.path.join(dirr,p)
            if (os.path.isdir(d)==True):
                delete_null_dir(d)
    if not os.listdir(dirr):
        os.rmdir(dirr)
        print "delete empty folder",dirr
        emptyfolder.append(dirr+'is empty folder')

if __name__=="__main__":
    print "---start delete empty folder"
    delete_null_dir(r'F:\New folder')

