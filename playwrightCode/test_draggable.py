import time
from turtledemo.penrose import start

from playwright.sync_api import Page


def test_AlertboxWithOkButton(page : Page):
    page.goto("https://jqueryui.com/draggable/")

    frame = page.frame_locator(".demo-frame")

    draggable = frame.locator("#draggable")

    box = draggable.bounding_box()
    if not box:
        raise Exception("could not find the element")

    start_x = box["x"] + box["width"]/2
    start_y = box["y"] + box["height"]/2

    page.mouse.move(start_x, start_y)
    page.mouse.down()

    time.sleep(5)

    page.mouse.move(start_x + 200, start_y + 50, steps=15)
    page.mouse.up()

    time.sleep(5)