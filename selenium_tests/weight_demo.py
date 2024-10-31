from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import config
import time

service_obj = Service(config.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service_obj)

discount_code= "rahulshettyacademy"
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(1)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(discount_code)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "promoBtn").click()
time.sleep(2)