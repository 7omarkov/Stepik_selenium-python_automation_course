import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Abs(unittest.TestCase):
    def testreg1(self):

        link = "http://suninjuly.github.io/registration1.html"

        #try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'first')]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'second')]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'third')]")
        input3.send_keys("Smolensk")
        '''input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")'''
        button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!","aaaa")

    def testreg2(self):
        link = "http://suninjuly.github.io/registration2.html"

        # try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'first')]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'second')]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//*[@class='first_block']//input[contains(@class, 'third')]")
        input3.send_keys("Smolensk")
        '''input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")'''
        button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "aaaa")





if __name__ == "__main__":
    unittest.main()