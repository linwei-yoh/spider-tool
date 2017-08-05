#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'AL'

import csv


if __name__ == '__main__':
    with open('../output/suburb_postcode.csv') as f:  # 采用b的方式处理可以省去很多问题
        reader = csv.reader(f)
        result = list(reader)
    pass