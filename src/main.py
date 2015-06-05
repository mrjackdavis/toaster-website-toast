#!/usr/bin/env python
from __future__ import print_function
 
import os
import time
import logging
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.connection import Location

from ToastItApi import ToastItApi
from toaster import toast

logging.basicConfig(level=logging.INFO)
generatorName = "Real Toast"
apiLocation = os.environ['API_PORT'].replace('tcp://','http://') + '/v0-2/'

s3Connection = S3Connection(os.environ['S3_ACCESS_KEY'],os.environ['S3_SECRET_KEY'], host="s3-ap-southeast-2.amazonaws.com",
)

def uploadItemToS3(pathToImg,itemID):
    logging.info("Uploading %s (%s) to S3",itemID,pathToImg)

    bucketName = 'toast-artefacts'

    logging.info(s3Connection)

    bucket = s3Connection.get_bucket(bucketName)
    k = Key(bucket)
    k.key = 'generators/%s/%s.png' % (generatorName,itemID)
    k.set_contents_from_filename(pathToImg)
    k.set_canned_acl('public-read')

    return "https://s3-ap-southeast-2.amazonaws.com/%s/%s" % (bucketName,k.key)

if __name__ == "__main__":
    toastItApi = ToastItApi(apiLocation);

    while True:
        logging.info('Checking for new requests')
        items = toastItApi.GetAllNewForGenerator(generatorName)

        logging.info('Found %s new requests',len(items))

        for item in items:
            try:
                toastItApi.StartProcessing(item)
                fullImage, thumbnail = toast(item.resourceURL)
                logging.info("Finished generating %s",item.id)

                item.resultURL=uploadItemToS3(fullImage,item.id)
                item.thumbnailURL=uploadItemToS3(thumbnail,"%s-thumbnail"%item.id)

                toastItApi.CompleteProcessing(item)

                logging.info('Generated result for %s. Found at %s',item.id,item.resultURL)

            except Exception as e:
                logging.exception(e)
                toastItApi.FailProcessing(item)

        logging.info("Sleeping for 10...")
        time.sleep(10)