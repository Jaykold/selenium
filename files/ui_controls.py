from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#checkBoxOption2").click()
radio_buttons = driver.find_elements(By.NAME, "radioButton")
time.sleep(1)

for option in radio_buttons:
    if option.get_attribute("value") == "radio2":
        option.click()
        assert option.is_selected()
        time.sleep(1)
        break