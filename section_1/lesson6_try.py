"""C помощью конструкции try - finally браузер закроется даже если будет ошибка"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.ID, "submit_button44")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
