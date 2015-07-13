#!/usr/bin/env python
# coding: utf-8

import os
import sys
import web

# Add current directory to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def is_test():
    return os.getenv('WEBPY_ENV', '') == 'test'


MONGO_HOST = '10.42.0.20'
MONGO_PORT = 27017
MONGO_DB = 'birds'

config = web.storage(
    database=dict(
        host=MONGO_HOST,
        port=MONGO_PORT,
        db=MONGO_DB
    )
)
