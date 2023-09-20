from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

import math

from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

   
    input1 = browser.find_element(By.XPATH, "//*[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//*[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//*[@name='email']")
    input3.send_keys("123")




    file_elem = browser.find_element(By.CSS_SELECTOR, "#file")

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_elem.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    #browser.find_element(By.XPATH, "//button").click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

