import io
import logging
import os
 
import PIL.Image
import selenium.webdriver

def fetch_screen_capture(uri, size):
    browser = selenium.webdriver.PhantomJS()
    browser.set_window_size(*size)
    browser.get(uri)
    return browser.get_screenshot_as_png()

def toast(uri):
    logging.info("Toasting %s",uri)

    toast_image = PIL.Image.open("/app/toast.jpg")
    black_image = PIL.Image.new(mode=toast_image.mode, size=toast_image.size,
        color=0)

    capture_cropbox = (0, 0) + toast_image.size
    capture = fetch_screen_capture(uri, toast_image.size)
    capture_image = PIL.Image.open(io.BytesIO(capture))
    capture_image.save("/app/capture.png")
    capture_mask = capture_image.crop(capture_cropbox).convert("L")

    composite_image = PIL.Image.composite(toast_image, black_image,
        capture_mask)

    composite_image.save("/app/composite.png")
    logging.info("Done toasting %s",uri)
