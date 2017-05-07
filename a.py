# -*- coding:utf8 -*-
#!/usr/bin/python
import subprocess
import re
import os
class LinkState(object):
    def __init__(self,ip):
        self.ip = ip
        self.getLinkState(self.ip)

    # 获取链路状态
    def getLinkState(self,ip):
        #运行ping程序
        p = subprocess.Popen(["ping.exe", ip],
             stdin = subprocess.PIPE,
             stdout = subprocess.PIPE,
             stderr = subprocess.PIPE,
             shell = True)

        #得到ping的结果
        out = p.stdout.read()
        print p
        print 11, os.system('ping  192.168.1.190 -c 1')

    #输出结果


if __name__ == '__main__':
    ip = 'baidu.com'    #要ping的主机
   # LinkState(ip)
    if('0'== os.system('ping 192.168.1.190 -c 1')):
            print 'ok'
    else:
            print 'failed'
    print os.system('ping 192.168.3.190 -c 1')
