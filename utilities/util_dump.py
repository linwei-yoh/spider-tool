#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'AL'
import pickle


def dump_to_file(filename, date):
    with open(filename, 'wb') as f:
        pickle.dump(date, f)


def dump_from_file(filename):
    with open(filename, 'rb') as f:
        d = pickle.load(f)
    return d


if __name__ == '__main__':
    pass
