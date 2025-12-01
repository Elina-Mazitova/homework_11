import pytest
from selenium import webdriver

@pytest.fixture
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",   # смотри актуальные версии на https://selenoid.autotests.cloud/status
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user:password@selenoid.autotests.cloud/wd/hub",
        options=options,
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()
