#coding=utf-8

import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

MEDIA_URL = '/media_images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_images')