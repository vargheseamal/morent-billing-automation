from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting MoRent Billing Info test...")

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# 1. Launch website
driver.get("https://morent-car.archisacademy.com/")

# 2. Click Search
search_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
)
search_button.click()

# 3. Click Rent Now
rent_now = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Rent Now')]"))
)
rent_now.click()

# 4. Verify Billing Info Step
billing_title = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Billing Info')]"))
)
print("Billing Information step displayed")

# 5. Verify billing fields
wait.until(EC.visibility_of_element_located((By.NAME, "name")))
wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
wait.until(EC.visibility_of_element_located((By.NAME, "address")))
wait.until(EC.visibility_of_element_located((By.NAME, "town")))

print("All billing input fields are visible")

# 6. Verify Next button is visible and disabled
next_button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]"))
)

assert next_button.get_attribute("disabled") is not None
print("Next button is visible and disabled")

time.sleep(2)
driver.quit()

print("TEST COMPLETED SUCCESSFULLY")
