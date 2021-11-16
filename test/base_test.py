import unittest

from pages.base.base_page import BasePage
from etc.helper.properties import get_settings


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = BasePage().get_driver()
        self.driver.get(get_settings()['default_base_url'])

    def tearDown(self):
        self.driver.quit()
