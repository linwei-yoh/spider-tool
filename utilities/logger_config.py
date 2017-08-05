#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : AL

import logging


def allot_logger_Show(name, level=None, fmt=None):
    '''
    初始化一个logger
    :param name: logger名称
    :param filename: 日志文件路径
    :param fmt: 日志格式
    :param level: 日志的严重程度
    :return:
    '''
    if level == None:
        level = logging.DEBUG
    if fmt == None:
        fmt = '%(asctime)s - %(levelname)s : %(message)s'
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)

        con_handler = logging.StreamHandler()
        con_handler.setLevel(logging.DEBUG)
        con_handler.setFormatter(logging.Formatter(fmt))

        logger.handlers = [con_handler]


def allot_logger_show_save(name, filename, level=None, fmt=None):
    '''
    初始化一个logger
    :param name: logger名称
    :param filename: 日志文件路径
    :param fmt: 日志格式
    :param level: 日志的严重程度
    :return:
    '''
    if level == None:
        level = logging.DEBUG
    if fmt == None:
        fmt = '%(asctime)s - %(module)s.%(funcName)s - %(levelname)s [line:%(lineno)d]: %(message)s'
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(fmt))

        logger.handlers = [file_handler]


allot_logger_show_save('request', '../report/reqest_report.log', level=logging.WARNING)


def get_logger():
    return logging.getLogger('request')



if __name__ == '__main__':
    log = get_logger()
    log.warning("mark")
