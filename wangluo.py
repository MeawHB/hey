#coding:utf8

import re
import os
import time

netcmd = '/sbin/ifconfig eth0 | grep bytes'

def getnetio(line):
    rx = re.match(r'RX(.*)(bytes.)(\d+)(.*)TX', line)
    tx = re.match(r'(.*)TX(.*)(bytes.)(\d+)', line)
    return (int(rx.group(3)), int(tx.group(4)))


line = os.popen(netcmd).read().strip()
netio = getnetio(line)
print(netio)
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


