# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from settings import * # путь до драйвера, email, password


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://petfriends1.herokuapp.com/")
        driver.find_element_by_link_text("PetFriends").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='PetFriends'])[2]/following::h1[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='PetFriends'])[3]/following::div[1]").click()
        driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='PetFriends'])[2]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Социальная сеть для любителей животных'])[1]/following::label[1]").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("user")
        driver.find_element_by_id("NameHelp").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Введите уникальное имя пользователя'])[1]/following::label[1]").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("email")
        driver.find_element_by_id("EmailHelp").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Введите адрес электронной почты'])[1]/following::label[1]").click()
        driver.find_element_by_id("pass").click()
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys("pass")
        driver.find_element_by_id("PassHelp").click()
        driver.find_element_by_id("pass").click()
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys("")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("")
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("")
        driver.find_element_by_link_text(u"У меня уже есть аккаунт").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Социальная сеть для любителей животных'])[1]/following::label[1]").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("al66@pf.com")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Электронная почта'])[1]/following::label[1]").click()
        driver.find_element_by_id("pass").click()
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys("1qasw2")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='PetFriends'])[2]/following::div[1]").click()
        #driver.find_element_by_link_text(u"Все питомцы").click()
        driver.find_element_by_link_text(u"Мои питомцы").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Выйти'])[1]/following::h2[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Выйти'])[1]/following::div[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Выйти'])[1]/following::div[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Выйти'])[1]/following::div[3]").click()
        driver.find_element_by_xpath("//div[@id='all_my_pets']/table/thead/tr/th").click()
        driver.find_element_by_xpath("//div[@id='all_my_pets']/table/thead/tr/th[2]").click()
        driver.find_element_by_xpath("//div[@id='all_my_pets']/table/thead/tr/th[3]").click()
        driver.find_element_by_xpath("//div[@id='all_my_pets']/table/thead/tr/th[4]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[3]/following::button[1]").click()
        driver.find_element_by_id("addPetsModalLabel").click()
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div/button/span").click()
        #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[3]/following::button[1]").click()
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div[2]/form/div[2]/label").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("name")
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div[2]/form/div[3]/label").click()
        driver.find_element_by_id("animal_type").click()
        driver.find_element_by_id("animal_type").clear()
        driver.find_element_by_id("animal_type").send_keys("wild animal")
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div[2]/form/div[4]/label").click()
        driver.find_element_by_id("age").click()
        driver.find_element_by_id("age").clear()
        driver.find_element_by_id("age").send_keys("1")
        driver.find_element_by_id("age").click()
        driver.find_element_by_id("age").clear()
        driver.find_element_by_id("age").send_keys("2")
        driver.find_element_by_id("age").click()
        driver.find_element_by_id("age").clear()
        driver.find_element_by_id("age").send_keys("3")
        driver.find_element_by_id("age").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=age | ]]
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div[3]/button[2]").click()
        driver.find_element_by_xpath("//div[@id='addPetsModal']/div/div/div[3]/button").click()
        driver.find_element_by_xpath("//button[@onclick=\"document.location='/logout';\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
