#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
start the client for test mds
"""
import argparse
import ConfigParser as configparser
import logging
import logging.handlers
import eventlet
import sys
sys.path.append('../')
from simplecfs.common.parameters import CODE_RS, DS_CONNECTED, DS_BROKEN # NOQA
from simplecfs.message.packet import MakeDirPacket, RemoveDirPacket,\
    ListDirPacket, StatusDirPacket, ValidDirPacket, AddDSPacket,\
    ReportDSPacket, AddFilePacket, AddFileCommitPacket, StatFilePacket,\
    DeleteFilePacket, GetFilePacket, GetObjPacket, GetChkPacket,\
    RepairChkPacket, RepairChkCommitPacket
from simplecfs.message.network_handler import send_command, recv_command


def get_new_connection(ip_='127.0.0.1', port=8000):
    return eventlet.connect((ip_, port))


def init():
    """init client"""
    # handle command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        metavar='CONFIG_FILE',
                        help='clientconfig file',
                        default='../conf/client.cfg')
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


def test_make_dir(dirname='/testdir/'):
    """test function: make_dir(dirname)
    dirname should be absolute path and end with '/'
    """

    dirname = dirname.strip()
    if not dirname.endswith('/'):
        dirname += '/'
    print 'make dirname %s' % dirname
    packet = MakeDirPacket(dirname)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_remove_dir(dirname='/testdir/'):
    """test function: remove_dir(dirname)
    dirname should be absolute path and end with '/'
    """

    dirname = dirname.strip()
    if not dirname.endswith('/'):
        dirname += '/'
    print 'remove dirname %s' % dirname
    packet = RemoveDirPacket(dirname)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_list_dir(dirname='/'):
    """test function: list_dir(dirname)
    dirname should be absolute path and end with '/'
    """

    dirname = dirname.strip()
    if not dirname.endswith('/'):
        dirname += '/'
    print 'list dirname %s' % dirname
    packet = ListDirPacket(dirname)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_status_dir(dirname='/testdir/'):
    """test function: status_dir(dirname)
    dirname should be absolute path and end with '/'
    """

    dirname = dirname.strip()
    if not dirname.endswith('/'):
        dirname += '/'
    print 'status dirname %s' % dirname
    packet = StatusDirPacket(dirname)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_valid_dir(dirname='/testdir/'):
    """test function: valid_dir(dirname)
    dirname should be absolute path and end with '/'
    """

    dirname = dirname.strip()
    if not dirname.endswith('/'):
        dirname += '/'
    print 'valid dirname %s' % dirname
    packet = ValidDirPacket(dirname)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7000):
    """test function: add_ds(rack_id, ds_ip, ds_port)
    """
    print 'add ds, rack_id:%d ip:%s port:%d' % (rack_id, ds_ip, ds_port)
    packet = AddDSPacket(rack_id, ds_ip, ds_port)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_report_ds(ds_ip='127.0.0.1', ds_port=7000, status=DS_CONNECTED):
    """test function: report_ds(info)
    report ds state info to mds
    """
    info = {
        'space': 102400,
        'chunk_num': 898,
        'status': status,
    }
    packet = ReportDSPacket(ds_ip, ds_port, info)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_add_file(filename='/testfile', fileinfo={}):
    """
    test function: add_file(filename, fileinfo)
    filename should be absolute path,
    finleinfo contain all the info in dict format:
    fileinfo = {
        "filename": filename,
        "filesize": 1048576,
        "block_size": 512,
        "code": {
            "type": "rs",  # "rs/crs/zcode/etc.",
            "k": 2,
            "m": 2,
            "w": 8,
        },
    }
    """
    fileinfo = {
        "filesize": 2048,
        "block_size": 1024,
        "code": {
            "type": CODE_RS,  # "rs/crs/zcode/etc.",
            "k": 2,
            "m": 2,
            "w": 8,
            "packet_size": 512,
        },
    }

    print 'add file %s' % filename
    print 'file info:'
    print fileinfo
    packet = AddFilePacket(filename, fileinfo)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_add_file_commit(filename='/testfile'):
    """
    test function: add_file_commit(filename)
    filename should be absolute path,
    """
    print 'add file commit %s' % filename
    packet = AddFileCommitPacket(filename)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_stat_file(filename='/testfile'):
    """
    test function: stat_file(filename)
    filename should be absolute path,
    """
    print 'stat file %s' % filename
    packet = StatFilePacket(filename)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_delete_file(filename='/testfile'):
    """
    test function: delete_file(filename)
    filename should be absolute path,
    """
    print 'delete file %s' % filename
    packet = DeleteFilePacket(filename)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_get_file(filepath='/testfile'):
    """
    test function: get_file(filepath)
    filepath should be absolute path,
    """
    print 'get file %s' % filepath
    packet = GetFilePacket(filepath)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_get_obj(obj_id='/testfile_obj0'):
    """
    test function: get_obj(obj_id)
    """
    print 'get obj %s' % obj_id
    packet = GetObjPacket(obj_id)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_get_chk(chk_id='/testfile_obj0_chk0'):
    """
    test function: get_chk(chk_id)
    """
    print 'get chk %s' % chk_id
    packet = GetChkPacket(chk_id)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_repair_chk(chk_id='/testfile_obj0_chk0'):
    """
    test function: repair_chk(chk_id)
    """
    print 'repair chk %s' % chk_id
    packet = RepairChkPacket(chk_id)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


def test_repair_chk_commit(chk_id='/testfile_obj0_chk0',
                           ds_id='127.0.0.1:7000'):
    """
    test function: repair_chk_commit(chk_id, ds_id)
    """
    print 'repair chk commit %s %s' % (chk_id, ds_id)
    packet = RepairChkCommitPacket(chk_id, ds_id)
    msg = packet.get_message()

    sock = get_new_connection()
    sock_fd = sock.makefile('rw')

    logging.info('%s', msg)
    send_command(sock_fd, msg)

    recv = recv_command(sock_fd)
    print recv
    logging.info('recv: %s', recv)
    sock_fd.close()


if __name__ == '__main__':
    init()

    # start test mds
    dirname = '/testdir/'
    # test_make_dir(dirname)
    # test_list_dir('/')
    # test_list_dir(dirname)
    # test_status_dir(dirname)
    # test_status_dir('/nosuchdir/')
    # test_valid_dir(dirname)
    # test_valid_dir('/nosuchdir/')
    # test_remove_dir('/nosuchdir/')
    # test_remove_dir(dirname)
    # test_list_dir('/')
    # test_status_dir(dirname)
    # test_valid_dir(dirname)

    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7000)
    # test_report_ds()
    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7001)
    # test_report_ds(ds_ip='127.0.0.1', ds_port=7001, status=DS_BROKEN)

    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7002)
    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7003)
    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7004)
    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7005)
    # test_add_ds(rack_id=0, ds_ip='127.0.0.1', ds_port=7006)

    # test_add_file()
    # test_add_file_commit()
    # test_stat_file()
    # test_delete_file()

    # test_add_file()
    # test_add_file_commit()

    # test_get_file()
    # test_get_obj()
    # test_get_chk()
    # test_repair_chk()
    # test_repair_chk_commit()
    # test_delete_file()
