#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : AL

import os
import requests
import logger_config

logger = logger_config.get_logger()

output_path = "../output"


def requests_get(url, header=None, param=None, proxies=None, timeout=(6.1, 20)):
    try:
        r = requests.get(url, headers=header, params=param, proxies=proxies, timeout=timeout)
        r.raise_for_status()
    except Exception as e:
        logger.warning("request get Error:%s" % url)
        return None

    if r.status_code == 200:
        return r.text
    else:
        logger.warning("request status Error:%s" % url)
        return None


def save_html_file(filename, content):
    file_path = os.path.join(output_path, filename)
    with open(file_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    pass
