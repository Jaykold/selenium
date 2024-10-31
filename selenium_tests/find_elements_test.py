from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[id='ctl00_mainContent_rbtnl_Trip_2']").click()
driver.find_element(By.ID, "MultiCityModelAlert").click()

driver.find_element(By.ID, "autosuggest").send_keys("nig")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item a")
#print(len(countries))

for country in countries:
    if country.text == "Nigeria":
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Nigeria"