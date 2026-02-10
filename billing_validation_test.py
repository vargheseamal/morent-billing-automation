from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Open MoRent website
driver.get("https://morent-car.archisacademy.com/")

# Click Search
search_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
)
search_button.click()

# Click Rent Now
rent_now_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Rent Now')]"))
)
rent_now_button.click()

# Verify Billing Information page
billing_title = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Billing Info')]"))
)
print("Billing Information step loaded")

# Click Next without filling any field
next_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))
)
next_button.click()

time.sleep(2)

# Verify still on Billing step
assert billing_title.is_displayed()
print("User is still on Billing Information step")

# Check validation errors
required_fields = ["Name", "Phone", "Address", "Town"]

errors = 0
for field in required_fields:
    try:
        driver.find_element(By.XPATH, f"//*[contains(text(),'{field}')]")
        errors += 1
    except:
        pass

assert errors > 0
print("Validation messages displayed")

time.sleep(2)
driver.quit()
