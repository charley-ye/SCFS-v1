#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
start the mds as a service
"""
import argparse
import ConfigParser as configparser
import logging
import logging.handlers

from simplecfs.mds.server import MDSServer


def main():
    """run the mds main function"""
    # handle command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        metavar='CONFIG_FILE',
                        help='mds config file',
                        default='./conf/mds.cfg')
    args = parser.parse_args()
    config_file = args.config

    # get config options
    config = configparser.ConfigParser()
    config.read(config_file)

    # init logging
    logger = logging.getLogger()  # get the 'root' logger
    level = getattr(logging, config.get('log', 'log_level'))
    logger.setLevel(level)
    log_name = config.get('log', 'log_name')
    log_max_bytes = config.getint('log', 'log_max_bytes')
    log_file_num = config.getint('log', 'log_file_num')
    handler = logging.handlers.RotatingFileHandler(log_name,
                                                   maxBytes=log_max_bytes,
                                                   backupCount=log_file_num)
    log_format = logging.Formatter('%(levelname)-8s[%(asctime)s.%(msecs)d]'
                                   '<%(module)s> %(funcName)s:%(lineno)d:'
                                   ' %(message)s',
                                   datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(log_format)
    logger.addHandler(handler)

    # start server
    mds = MDSServer(config)
    mds.start()

if __name__ == '__main__':
    main()
