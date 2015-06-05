#!/usr/bin/env python
from __future__ import print_function
 
import os
import logging

from ToastItApi import ToastItApi
from toaster import toast

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info('Test toasting')

    fullImage, thumbnail = toast("http://www.trioxis.com")

    logging.info('Done')