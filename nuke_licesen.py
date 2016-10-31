import os
import sys
f=open('nuke_license.txt','r')
afile=[]
for line in f:
    afile.append(line.strip().split()[2]+'\t'+line.strip().split()[5]+' '+line.strip().split()[6])

bfile=set(afile)
'''for a in bfile:
    print  a
if len(bfile)>14:
    for b in bfile:
        for c in bfile:
            if b.split()[0]==c.split()[0] and b.split()[1]==c.split()[1]:
                bfile.remove(b)
                print b'''
cfile=[]
for i in bfile:
    for c in cfile:
        if i.split()[0]==c.split()[0] and i.split()[1]==c.split()[1]:
            continue
        else:
            cfile.append(i)

print cfile