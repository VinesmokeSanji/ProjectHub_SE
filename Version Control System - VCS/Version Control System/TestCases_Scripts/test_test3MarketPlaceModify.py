# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest3MarketPlaceModify():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test3MarketPlaceModify(self):
    self.driver.get("http://127.0.0.1:5501/login.html")
    self.driver.set_window_size(1722, 1082)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("foreversurya007@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("2651265161gfh")
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.LINK_TEXT, "Explore Now").click()
    self.driver.find_element(By.LINK_TEXT, "Market Place").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) .btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) .btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".d-flex > .btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".d-flex > .btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(3) .btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(3) .btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(6) .btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(6) .btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(7) .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(1) .cart-quantity-input").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(1) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(1) .cart-quantity-input").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(1) .cart-quantity-input").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(1) .cart-quantity-input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(2) .cart-quantity-input").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(2) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(2) .cart-quantity-input").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(2) .cart-quantity-input").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(2) .cart-quantity-input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("4")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("5")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("6")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").send_keys("7")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(3) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(4) .cart-quantity-input").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(4) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(5) .cart-quantity-input").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(5) .cart-quantity-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-row:nth-child(4) .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-dark").click()
    assert self.driver.switch_to.alert.text == "Thank you for your purchase!!!"
    self.driver.close()
  