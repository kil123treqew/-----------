import unittest
import time
from selenium.webdriver.common.by import By
import driver_config  
import config  

class TestSwitchLanguage(unittest.TestCase):

    def setUp(self):
        """Считывание конфигурации и настройка драйвера"""
        self.driver = driver_config.get_driver()
        self.url = config.URL
        self.language_selector_id = config.LANGUAGE_SELECTOR_ID
        self.russian_link_xpath = config.RUSSIAN_LINK_XPATH

    def test_switch_language(self):
        """Тест переключения языка на веб-странице"""
        start_time = time.time()

        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)

        # Переключение языка
        language_button = self.driver.find_element(By.ID, self.language_selector_id)
        language_button.click()
        time.sleep(2)

        russian_link = self.driver.find_element(By.XPATH, self.russian_link_xpath)
        russian_link.click()

        time.sleep(2)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения теста (переключение языка): {execution_time:.2f} секунд")

    def tearDown(self):
        """Закрытие драйвера после выполнения теста"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
