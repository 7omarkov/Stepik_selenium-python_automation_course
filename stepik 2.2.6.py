from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

import math

from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()



    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    z = calc(x)
    print(x, z)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(z)

    #browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)



    #browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()


    #browser.find_element(By.XPATH, "//button").click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

