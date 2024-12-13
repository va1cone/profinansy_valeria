from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by: By, value: str):
        element = self.wait_until_clickable(by, value)
        element.click()

    def send_keys(self, by: By, value: str, keys: str):
        element = self.wait_until_visible(by, value)
        element.send_keys(keys)

    def wait_for_url(self, url: str):
        self.wait.until(expected_conditions.url_to_be(url))

    def open_page(self, url: str):
        self.driver.get(url)

    def assert_current_url(self, expected_url: str):
        assert self.driver.current_url == expected_url

    def wait_until_clickable(self, by: By, value: str):
        return self.wait.until(expected_conditions.element_to_be_clickable((by, value)))

    def wait_until_visible(self, by: By, value: str):
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)))

    def wait_until_invisible(self, by: By, value: str):
        return self.wait.until(expected_conditions.invisibility_of_element_located((by, value)))

    def long_press(self, by: By, value: str, duration: int):
        element = self.wait_until_visible(by, value)
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).pause(duration).release().perform()

    def drag_and_drop_bun(self, source_selector: str, target_selector: str):
        bun_source = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, source_selector)))
        bun_target = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, target_selector)))

        actions = ActionChains(self.driver)
        actions.click_and_hold(bun_source).move_to_element(bun_target).release().perform()

    def wait_sleep(self, seconds: int):
        time.sleep(seconds)

    def get_number(self, by: By, value: str) -> int:
        element = self.wait.until(expected_conditions.visibility_of_element_located((by, value)))
        number = element.text
        return int(number.replace('#', ''))