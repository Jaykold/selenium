import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service(config.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
discount_code= "rahulshettyacademy"
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
assert count > 0

actual_list = []
for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert actual_list == expected_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(discount_code)
driver.find_element(By.CLASS_NAME, "promoBtn").click()


wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

total_amount = driver.find_element(By.CLASS_NAME, "totAmt").text
discount_amount = driver.find_element(By.CLASS_NAME, "discountAmt").text

assert float(total_amount) > float(discount_amount)