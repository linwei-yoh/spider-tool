#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : AL

import utilities as utility
import requests
from pyquery import PyQuery as pq
import re

import time
from functools import wraps
import pandas as pd

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running: %s seconds" %
              (str(t1 - t0))
              )
        return result

    return function_timer


url_Header = {"Host":"www.realestate.com.au"}
url_Params = {}



def single_request_test():
    url_Header['User-Agent'] = utility.make_random_useragent()
    url = "https://www.realestate.com.au/property/1-95-blackburn-rd-mount-waverley-vic-3149"

    r = requests.get(url, headers=url_Header, params=None, cookies=None, timeout=(6.05, 20))

    if r.status_code == 200:
        with open("..\output\html2.txt", 'w', encoding='GB18030') as file:
            file.write(r.text)
        utility.dump_to_file("..\output\html.pkl", r.text)
        print("Success")
    else:
        print("False")

    pass


def pyquery_test():
    try:
        with open("..\output\\tmp.txt", 'r',encoding='GB18030') as file:
            content = file.read()

        doc = pq(content)
        table_node = doc("thead").parent()
        html_src = str(table_node)
        try:
            df = pd.read_html(html_src)[0]
            result = df.to_dict(orient='records')
        except IndexError:
            pass
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    single_request_test()
    pass
