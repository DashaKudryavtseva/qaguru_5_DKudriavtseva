import pytest
from selene import browser


@pytest.fixture
def browser_configuration():
    browser.config.hold_browser_open = True
    browser.config.window_height = 1080
    browser.config.window_width = 720