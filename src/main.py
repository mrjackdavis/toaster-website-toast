#!/usr/bin/env python
from __future__ import print_function
 
import argparse
import logging
from toaster import toast

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--uri", help="URI to fetch", required=True)
    args = parser.parse_args()

    toast(args.uri)


