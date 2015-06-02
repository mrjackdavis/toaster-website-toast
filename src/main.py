#!/usr/bin/env python
from __future__ import print_function
 
import argparse
import io
import logging
import os
 

import PIL.Image
import selenium.webdriver

logging.basicConfig(level=logging.DEBUG)
 
 
def new(sklItem):
	fileLocation = "/app/%s.png" % (sklItem.id)
 
	if os.path.isfile(fileLocation):
		logging.warning("Cannot generate item[%s]. %s already exists",
            sklItem.id,fileLocation)
	else:
		logging.info("Getting URL data for scene %s from %s",
            sklItem.id, sklItem.resourceURL)
        # HERP DERP - code lives here
 
 
def fetch_screen_capture(uri, size):
    browser = selenium.webdriver.PhantomJS()
    browser.set_window_size(*size)
    browser.get(uri)
    return browser.get_screenshot_as_png()
 
 
if __name__ == "__main__":
    logging.debug("Starting thingo")
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--uri", help="URI to fetch", required=True)
    args = parser.parse_args()

    logging.debug("point 1")
 
    toast_image = PIL.Image.open("/app/toast.jpg")
    black_image = PIL.Image.new(mode=toast_image.mode, size=toast_image.size,
        color=0)
    
    logging.debug("point 2")

    capture_cropbox = (0, 0) + toast_image.size
    capture = fetch_screen_capture(args.uri, toast_image.size)
    capture_image = PIL.Image.open(io.BytesIO(capture))
    capture_image.save("/app/capture.png")
    capture_mask = capture_image.crop(capture_cropbox).convert("L")
    
    logging.debug("point 3")

    composite_image = PIL.Image.composite(toast_image, black_image,
        capture_mask)
    composite_image.show()

    logging.debug("point 4")

    composite_image.save("/app/composite.png")

    logging.debug("point 5")
