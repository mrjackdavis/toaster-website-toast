#!/usr/bin/env python
from __future__ import print_function
 
import argparse
import os
import time
import logging
from ToastItApi import ToastItApi
from toaster import toast

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--uri", help="URI to fetch", required=True)
    args = parser.parse_args()
    apiLocation = os.environ['API_PORT'].replace('tcp://','http://') + '/v0-2/'
    toastItApi = ToastItApi(apiLocation);

    while True:
        logging.info('Checking for new requests')
        items = toastItApi.GetAllNew()

        logging.info('Found %s new requests',len(items))

        for item in items:
            try:
                # toastItApi.StartProcessing(item)
                # fileLocation = generator.new(item)
                # logging.info("Finished generating %s",item.id)

                # if not fileLocation:
                #     raise Exception("File location was null")

                # resultFullSizeFilePath = compress(fileLocation,80)
                # resultThumbnailFilePath = compressAndScale(fileLocation,50,500)

                # item.resultURL=uploadItemToS3(resultFullSizeFilePath,item.id)
                # item.thumbnailURL=uploadItemToS3(resultThumbnailFilePath,"%s-thumbnail"%item.id)

                # toastItApi.CompleteProcessing(item)

                # logging.info('Generated result for %s. Found at %s',item.id,item.resultURL)

                toast(item.resourceURL)
                # toast(args.uri)
            except Exception as e:
                logging.error(e)
                toastItApi.FailProcessing(item)

        logging.info("Sleeping for 10...")
        time.sleep(10)