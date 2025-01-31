from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")  

service = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")  
driver = webdriver.Chrome(service=service, options=options)

def scen_3():
    try:
        start_time = time.time()
        
        driver.get("https://en.wikipedia.org/wiki/Space")
        driver.maximize_window()
        time.sleep(2)
        
        language_button = driver.find_element(By.ID, "p-lang-btn")
        language_button.click()
        time.sleep(2)
        
        russian_link = driver.find_element(By.XPATH, "//a[@lang='ru']")
        russian_link.click()
        
        time.sleep(2)
        
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        driver.quit()
        return execution_time

print(f"Время выполнения теста (переключение языка): {scen_3():.2f} секунд")
