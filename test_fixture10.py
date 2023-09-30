import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    #browser.quit()


class TestMainPage1():

    @pytest.mark.parametrize("lesson", ["236898", "236899", "236903", "236904", "236905"])
    #@pytest.mark.parametrize("lesson", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    #@pytest.mark.parametrize("lesson",["236895", "236896",])
    def test_guest_should_see_login_link(self, browser, lesson):
        global a
        lesson
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)

        WebDriverWait(browser, 15).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ember33")))
        browser.find_element(By.CSS_SELECTOR, "#ember33").click()

        '''email = input("input email")
        pas = input("input password")'''

        email = "ччч"
        pas = "ччч"

        '''window_after = browser.window_handles[1]
        browser.switch_to.'''

        browser.find_element(By.CSS_SELECTOR, "#id_login_email").click()
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(email)

        browser.find_element(By.CSS_SELECTOR, "#id_login_password").click()
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(pas)



        browser.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(1)

        answer = math.log(int(time.time()))

        WebDriverWait(browser, 15).until(
            expected_conditions.visibility_of_element_located((By.TAG_NAME, "textarea")))

        text_input = browser.find_element(By.TAG_NAME, "textarea")

        time.sleep(2)
        #WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(text_input))

        text_input.click()
        time.sleep(2)

        try:
            text_input.send_keys(answer)
        except selenium.common.exceptions.ElementNotInteractableException:
            browser.find_element(By.XPATH, "//button[@class='again-btn white']").click()
            time.sleep(2)
            text_input = browser.find_element(By.TAG_NAME, "textarea")
            text_input.send_keys(answer)
        time.sleep(3)

        #browser.find_element(By.CSS_SELECTOR, "#ember99").send_keys(answer)



        #mybutton =  "//button[@type='button']"
        mybutton = "//button[@class = 'submit-submission']"
        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, mybutton)))
        browser.find_element(By.XPATH, mybutton).click()

        WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class,'hints')]")))

        got_text = browser.find_element(By.XPATH, "//div[contains(@class,'hints')]").text

        '''if got_text != "Correct!":
            feedback = a.append(got_text)
            print(feedback)'''

        assert got_text == "Correct!", "Got text not equal"

        time.sleep(1)

