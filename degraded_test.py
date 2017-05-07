#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
use Client for test
"""
import argparse
import ConfigParser as configparser
import time
import sys
from simplecfs.client.api import Client
from simplecfs.common.parameters import CODE_Z
from simplecfs.common.parameters import DS_BROKEN, DS_CONNECTED

#des_path = './testM.txt'
base_path = '/home/test/'
src_path = ''
de_base_path='/home/de_test'
code_info = {  # default code info
    'type': CODE_Z,
    'k': 3,
    'm': 2,
    'w': 8,
    'packet_size': 1024,
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


def test_putfile(client):
    t1 = time.time()
    client.putfile(src_path, des_path, code_info)
    interval = time.time()-t1
    return interval * 1000  # ms


def test_normal_get_chunk(client,size_num,id):
    chunk_id = '/test'+str(size_num)+'M.txt_obj0_chk'+id
    local_path = '/home/test/'+'test'+str(size_num)+'M.txt_obj0_chk'+id
    print local_path
    t1 = time.time()
    client.getchunk(chunk_id, local_path)
    interval = time.time()-t1
    return interval * 1000  # ms


def test_degrade_get_chunk(client,size_num,id):
    chunk_id = '/test'+str(size_num)+'M.txt_obj0_chk'+id
    print chunk_id
    (ip, port) = client.get_chunk_ds_id(chunk_id)
    client.report_ds(ip, port, DS_BROKEN)
    degrade_path = de_base_path + chunk_id
   # t1 = time.time()
    client.getchunk(chunk_id, degrade_path)
   # interval = time.time()-t1
    client.report_ds(ip, port, DS_CONNECTED)

    # return interval * 1000  # ms


def test_delete_file(client):
    des_path = './testM.txt'
    client.delfile(des_path)


if __name__ == '__main__':
    size_num = int(sys.argv[1])
    des_path='./test'+sys.argv[1]+'M.txt'
    id = sys.argv[2]
    del sys.argv[1],sys.argv[1]
    client = init()
    # size_num = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    print size_num
    r=4
    file_name = str(size_num)+'Mdeg.txt'
    src_path = base_path+file_name
    file_size = size_num*(1024*1024)
    code_info['block_size'] = file_size/r
 #   test_putfile(client)
 #   total_time =0
#    test_normal_get_chunk(client,size_num,id)
    test_degrade_get_chunk(client,size_num,id)
#    print file_name[:-4], total_time,
