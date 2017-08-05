#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : AL


from multiprocessing.dummy import Pool as ThreadPool
import util_request
from bs4 import BeautifulSoup
import pandas as pd
from util_fetch import make_random_useragent

URL_IP = "http://icanhazip.com"
Url_Target = "https://www.baidu.com/"


# 在使用requests的代理的时候
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": None,
# }
# 如果两个 http/https 有设定，则在访问对应类型网址的时候就会使用代理
# 否则直接访问 不经过代理  上述的情况下 对于http开头的网站需要代理 https的则不用


def get_proxy_ip_xicidaili():
    """
    从xicidaili  解析获得代理IP列表 
    :return: 
    """
    Tmp_Header = {"User-Agent": make_random_useragent()}
    content = util_request.requests_get("http://www.xicidaili.com/wt/", header=Tmp_Header)

    if content is None:
        print("代理IP页面读取出错")
        return None
    else:
        bsobj = BeautifulSoup(content, 'lxml')
        table_node = bsobj.find("table", {"id": "ip_list"})
        iplist = pd.read_html(str(table_node), header=0)[0]
        iplist = iplist.reindex(columns=["IP地址", "端口", "类型"])
        iplist = iplist.values.tolist()
        return iplist


def request_with_proxy(item):
    Tmp_Header = {"User-Agent": make_random_useragent()}

    ip_type = item[2].lower()
    ip_add = "http://" + item[0] + ":" + str(item[1])
    proxies = {ip_type: ip_add}

    content = util_request.requests_get(Url_Target, header=Tmp_Header, proxies=proxies)

    if content is None:
        return None
    else:
        return proxies


def proxy_show_ip(item):
    Tmp_Header = {"User-Agent": make_random_useragent()}

    ip_type = item[2].lower()
    ip_add = "http://" + item[0] + ":" + str(item[1])
    proxies = {ip_type: ip_add}

    content = util_request.requests_get(Url_Target, header=Tmp_Header, proxies=proxies)

    if content is not None:
        print(content)


def check_proxy_ip(ip_list):
    """
    多线程测试代理后能否访问目标网址
    :param ip_list: 待测试代理ip列表
    :return: 有效代理IP集合([ip类型，"IP:端口"])
    """
    pool = ThreadPool(10)
    results = pool.map(proxy_show_ip, ip_list)
    pool.close()
    pool.join()
    vaild_list = [proxy for proxy in results if proxy is not None]
    return vaild_list


def proxy_src_switch(url_ip):
    """
    选择代理IP来源网站的解析函数
    :param url_ip: 代理网站
    :return: 
    """
    if url_ip == "xicidaili":
        return get_proxy_ip_xicidaili()
    else:
        return [None]


def get_valid_proxy(url_tar, ip_src="xicidaili"):
    """
    通过代理网站获取代理IP，并对目标网址url_tar测试 获得有效代理IP集合
    :param url_tar: 目标测试地址
    :param ip_src: 代理IP来源地址
    :return: 
    """
    global Url_Target
    Url_Target = url_tar
    ip_list = proxy_src_switch(ip_src)
    valid_ip = check_proxy_ip(ip_list[:10])
    print("有效代理IP共 %s 个" % len(valid_ip))
    return valid_ip


if __name__ == '__main__':

    # proxy_list = get_valid_proxy("http://icanhazip.com")
    #
    # for i in proxy_list:
    #     URL_IP = "http://icanhazip.com"
    #     # url = "http://house.ksou.cn/p.php?q=Mount+Waverley&sta=vic&p=%s" % i
    #     Tmp_Header["User-Agent"] = make_random_useragent()
    #     bol = requests_get(URL_IP, header=Tmp_Header, proxies=proxy_list[0])
    #
    #     if bol is None:
    #         print("Faile")
    #     else:
    #         print(bol)

    pass
