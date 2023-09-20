from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import math

from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = browser.find_element(By.CSS_SELECTOR,"#price")
    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"), "$100"))


    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    '''window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)'''



    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    z = calc(x)
    print(x, z)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(z)

    #browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)



    #browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()


    #browser.find_element(By.XPATH, "//button").click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

