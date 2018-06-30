# -*- coding:utf-8 -*-
#test
import sys
import os
import time

netcmd = '/sbin/ifconfig eth0 | grep bytes'

def getnetio(line):
    s1 = line.find('RX*bytes ')
    e1 = line.find(' ', s1)
    neti = line[s1:e1]
    s2 = line.find('TX*bytes ')
    e2 = line.find(' ', s2)
    neto = line[s2:e2]
    result = (int(neti), int(neto))
    return result

line = os.popen(netcmd).readline().strip()
netio = getnetio(line)
neti_start = netio[0]
neto_start = netio[1]
time_start = time.time()

while (True):
    time.sleep(1);
    info = []
    line = os.popen(netcmd).readline().strip()
    netio = getnetio(line)
    info.append("流入总量:%.4fm, 流出总量:%.4fm" % (netio[0]/1024/1024, netio[1]/1024/1024))
    time_curr = time.time()
    neti_total = netio[0]-neti_start
    neto_total = netio[1]-neto_start
    sec_total = time_curr-time_start
    neti_start = netio[0]
    neto_start = netio[1]
    time_start = time_curr
    info.append("流入速度:%.4fk/s" % (neti_total/sec_total/1024))
    info.append("流出速度:%.4fk/s" % (neto_total/sec_total/1024))
    show = ", ".join(info)
    print(show+"\r")


