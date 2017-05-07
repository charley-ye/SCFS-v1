#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
use Client for test
"""
import argparse
import ConfigParser as configparser
import time
import sys
import os
from simplecfs.client.api import Client
from simplecfs.common.parameters import CODE_Z
from simplecfs.common.parameters import DS_BROKEN, DS_CONNECTED

#des_path = './testM.txt'
base_path = '/home/cpy/'
src_path = ''

code_info = {  # default code info
    'type': CODE_Z,
    'k': 3,
    'm': 2,
    'w': 8,
    'packet_size': 20480,
    'block_size': 33554432,  # 32M
}


def init():
    """init client"""
    # handle command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        metavar='CONFIG_FILE',
                        help='clientconfig file',
                        default='./conf/client.cfg')
    args = parser.parse_args()
    config_file = args.config

    # get config options
    config = configparser.ConfigParser()
    config.read(config_file)

    # get the client
    client = Client(config)
    return client


def test_putfile(client,des_path):
    client.putfile(src_path,des_path,code_info)

if __name__ == '__main__':
    size_num = int(sys.argv[1])
    del sys.argv[1]
    client = init()
    times=size_num/1024
    print times
    os.system('python split.py'+' '+str(times)+' '+str(size_num))
    for i in range (0,times-1):
        file_name1=str(size_num)+'M'+str(i)+'.txt'
        src_path=base_path+file_name1
        file_size=1024*1024*1024
        des_path='./test'+str(size_num)+'M'+str(i)+'.txt'
       # print src_path,des_path
        code_info['block_size']=(file_size/(3*4*1024)+1)*1024
        test_putfile(client,des_path)
    file_name2 = str(size_num)+'M'+str(times-1)+'.txt'
    src_path = base_path+file_name2
    file_size = (size_num-(times-1)*1024)*(1024*1024)
    des_path='./test'+str(size_num)+'M'+str(times-1)+'.txt'
    code_info['block_size'] = (file_size/(3*4*1024)+1)*1024
    #print src_path,des_path
    test_putfile(client,des_path)
    os.system('remove /home/cpy/*')
