import pytest
from selene import browser


@pytest.fixture
def browser_configuration():
    browser.config.browser_name = "chrome"
    browser.config.window_height = 1080
    browser.config.window_width = 720

