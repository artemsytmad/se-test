from etc.helper import properties
from selenium import webdriver


def get():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    return webdriver.Remote(
        command_executor=properties.get_settings()['server_url'],
        options=options
    )
