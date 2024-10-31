from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
name="Foo"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(1)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(1)
alert = driver.switch_to.alert
alertText = alert.text
time.sleep(1)
assert name in alertText
alert.accept()
#alert.dismiss() - for cancel
time.sleep(1)