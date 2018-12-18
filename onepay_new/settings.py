# -*- coding: utf-8 -*-

import os
import sys
import logging

# sqlite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dev_db = prefix + os.path.join(basedir, 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s.%(msecs)03d]: %(message)s',
                    datefmt='%Y-%m-%d %X',
                    stream=sys.stdout)