import pytest
from selene import browser

@pytest.fixture()
def constants():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080