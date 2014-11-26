#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
connet to MongoDB
"""
import sys

from pymongo import Connection
from pymongo.errors import ConnectionFailure
from bson.errors import InvalidStringData

reload(sys)
sys.setdefaultencoding('utf-8')

def con2MongoDB(host="192.168.1.220", port=27017):
    try:
        c = Connection(host, port)
        return c
    except ConnectionFailure, e:
        sys.stderr.write("Error")
        return

if __name__ == '__main__':
    con2MongoDB()