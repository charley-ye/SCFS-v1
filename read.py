#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
use Client for test
"""
import argparse
import ConfigParser as configparser
import sys
from simplecfs.client.api import Client



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


def test_normal_get_chunk(client,size_num,id):
    chunk_id = '/test'+str(size_num)+'M.txt_obj0_chk'+id
    local_path = '/home/de_test'+chunk_id
    client.getchunk(chunk_id, local_path)




if __name__ == '__main__':
    #t1=time.time()
    size_num = int(sys.argv[1])
    #des_path='./test'+sys.argv[1]+'M.txt'
    id = sys.argv[2]
    del sys.argv[1],sys.argv[1]
#    t1=time.time()
    client = init()
    test_normal_get_chunk(client,size_num,id)

