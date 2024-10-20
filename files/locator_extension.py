from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/angularpractice")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Foo Bear")
driver.find_element(By.NAME, "email").send_keys("foobear@123.com")
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("password")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
time.sleep(1)
dropdown.select_by_visible_text('Female')
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='date']").send_keys("18/10/2024")
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()


time.sleep(2)
