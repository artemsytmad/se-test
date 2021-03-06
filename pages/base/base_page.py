from etc.helper import properties
from etc.drivers import Chrome, Firefox


class BasePage:
    driver = None

    def get_driver(self):

        default_driver = properties.get_settings()['default_driver']

        if default_driver == "Chrome":
            self.driver = Chrome.get()

        elif default_driver == "Firefox":
            self.driver = Firefox.get()

        self.driver.implicitly_wait(properties.get_settings()['default_timeout'])

        return self.driver

    def navigate_to(self, url):
        print("Navigate to '%s'" % url)
        self.driver.get(url)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to.frame(frame_reference)

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)
