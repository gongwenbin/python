#-*- coding: GBK -*-
import os
import string
import datetime
import re

clock=re.sub(':| ','-',str(datetime.datetime.now())[0:-7])
date=str(datetime.datetime.now())[0:10]

print clock

#loglocations=[]
alll_use_logs=[]
user_times=[]
use_logs=[]
user_times_logs=[]

logfiles=os.listdir(os.getcwd()+'\\logs')

for logfile in logfiles:
	file=open(os.getcwd()+'\\logs\\'+logfile,'r')
	logs=file.readlines()
	file.close()
	for i in logs:
		if 'start' in i:
			alll_use_logs.append(i)
			use_logs.append(i.split('    ')[1].split(' ')[0]+'\n')
			
#for i in use_logs:
#	user_time=i.split('\n')[0]+'： 使用次数为 '+str(use_logs.count(i))+'次； 折合时间为 '+str(use_logs.count(i)*30)+' 分钟；'+'\n'
#	if user_time not in user_times:
#		user_times.append(user_time)
	
for i in use_logs:
	user_time=i.split('\n')[0]+' '+str(use_logs.count(i))+' \n'
	if user_time not in user_times:
		user_times.append(user_time)
	
user_times.sort(key=lambda x:int(x.split(r' ')[1]))
user_times.reverse()

for i in user_times:
	user_times_log=i.split(' ')[0]+'： 使用次数为 '+str(i.split(' ')[1])+'； 折合时间为 '+str(int(i.split(' ')[1])*30)+' 分钟；'+'\n'
	if user_times_log not in user_times_logs:
		user_times_logs.append(user_times_log)
	
file=open(os.getcwd()+'\\'+'Nuke_users.txt','w')
file.writelines(alll_use_logs)
file.close()

file=open(os.getcwd()+'\\'+'Nuke_use_time.txt','w')
file.writelines(user_times_logs)
file.close()

