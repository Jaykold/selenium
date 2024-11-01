import config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service(config.CHROME_DRIVER_PATH)
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[@target='_blank']").click()

windows_open = driver.window_handles
driver.switch_to.window(windows_open[1])

words = driver.find_elements(By.XPATH, "//p[@class='im-para red']")
time.sleep(2)

for word in words:
    text = word.text
    for text in text.split(" "):
        if "@" in text:
            email = text
            break

driver.switch_to.window(windows_open[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.XPATH, "//label[1]//span[2]").click()
driver.find_element(By.CSS_SELECTOR, "option[value='teach']").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)