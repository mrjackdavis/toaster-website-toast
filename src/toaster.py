import io
import logging
 
import PIL.Image
import selenium.webdriver

def fetch_screen_capture(uri, size):
    browser = selenium.webdriver.PhantomJS()
    browser.set_window_size(*size)
    browser.get(uri)
    return browser.get_screenshot_as_png()

def toast(uri):
    logging.info("Toasting %s",uri)

    toast_image = PIL.Image.open("/app/toast-01.png")
    black_image = PIL.Image.open("/app/toast-02.png")

    capture_cropbox = (0, 0) + toast_image.size
    capture = fetch_screen_capture(uri, toast_image.size)
    capture_image = PIL.Image.open(io.BytesIO(capture))
    capture_image.save("/app/capture.png")
    capture_mask = capture_image.crop(capture_cropbox).convert("L")

    composite_image = PIL.Image.composite(toast_image, black_image,
        capture_mask)

    renderedImagePath = "/app/render.png"
    thumbnailPath = "/app/thumbnail.png"

    composite_image.save(renderedImagePath)

    size = 500, 500

    #open previously generated file
    compImg = PIL.Image.open(renderedImagePath)

    compImg.thumbnail(size, PIL.Image.ANTIALIAS)

    compImg.save(thumbnailPath, "PNG", quality=60)

    logging.info("Done toasting %s",uri)

    return renderedImagePath, thumbnailPath
