#!/usr/bin/env python
# coding: utf-8

import os
import sys

import mongoengine

# add current directory to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# check for testing env
def is_test():
    return os.getenv('WEBPY_ENV', '') == 'test'


# set mongodb config
MONGO_HOST = os.getenv('MONGODB_HOST', '127.0.0.1')
MONGO_PORT = os.getenv('MONGODB_PORT', 27017)
MONGO_DB = os.getenv('MONGODB_DB', 'birds')

# port may be passed in host with colon sep
if ':' in MONGO_HOST:
    (MONGO_HOST, MONGO_PORT) = MONGO_HOST.split(':')

db = mongoengine.connect(
    MONGO_DB, host=MONGO_HOST, port=int(MONGO_PORT)
)
