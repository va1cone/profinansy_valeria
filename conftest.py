import pytest
from helpers import WebdriverFactory

@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    driver = WebdriverFactory.getWebdriver(browser)
    yield driver
    driver.quit()