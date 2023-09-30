from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pytest

from selenium import webdriver


def test_loginst():
    browser = webdriver.Chrome()
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "#ember33").click()

    '''email = input("input email")
    pas = input("input password")'''

    email = "xx"
    pas = "xx"

    browser.switch_to.alert

    browser.find_element(By.CSS_SELECTOR, "#id_login_email").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").sendkeys(email)

    browser.find_element(By.CSS_SELECTOR, "#id_login_password").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").sendkeys(pas)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()


