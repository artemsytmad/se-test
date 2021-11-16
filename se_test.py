import unittest

from pages.se_page import SePage
from test.base_test import TestCase


class TestSe(TestCase):

    def test_001(self):
        page = SePage(self.driver)
        page.search("abc")
        page.click_go()

    def test_002(self):
        page = SePage(self.driver)
        page.search("start")
        page.click_go()

    def test_002(self):
        page = SePage(self.driver)
        page.search("driver")
        page.click_go()


if __name__ == "__main__":
    unittest.main()