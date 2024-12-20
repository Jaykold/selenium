from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://quizzard-ten.vercel.app/signup")
time.sleep(2)
driver.find_element(By.ID, "firstName").send_keys("Foo")
driver.find_element(By.ID, "lastName").send_keys("Bear")
driver.find_element(By.ID, "email").send_keys("test123@gmail.com")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "confirmPassword").send_keys("password")
time.sleep(2)

# //tagname[@attribute='value']
submit_button = driver.find_element(By.XPATH, "//button[contains(@class, 'rounded-full')]")

while submit_button.is_enabled() == False:
    time.sleep(1)

submit_button.click()


time.sleep(2)
# Assert the current URL
expected_url = "https://quizzard-ten.vercel.app/"
current_url = driver.current_url

assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

print("Navigation to login page successful")