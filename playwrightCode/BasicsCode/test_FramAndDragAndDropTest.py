import time

from playwright.sync_api import Page


def test_AlertboxWithOkButton(page : Page):
    page.goto("https://jqueryui.com/droppable/")

    frame = page.frame_locator(".demo-frame")

    source = frame.locator("#draggable")
    destination = frame.locator("#droppable")

    #source = page.locator("#draggable")
    #destination = page.locator("#droppable")

    source.drag_to(destination)

    time.sleep(5)