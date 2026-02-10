from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Launch website
driver.get("https://morent-car.archisacademy.com/")

# Click Search
search_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
)
search_button.click()

# Click Rent Now
rent_now = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Rent Now')]"))
)
rent_now.click()

# Capture car name
car_name = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1"))
).text
print("Selected Car:", car_name)

# Capture car price
car_price_text = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'$')]"))
).text

car_price = float(car_price_text.replace("$", "").strip())
print("Car Price:", car_price)

# Proceed to Billing step
next_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))
)
next_button.click()

time.sleep(2)

# Rental Summary - Car name
summary_car_name = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Rental Summary')]"))
)
print("Rental Summary loaded")

# Capture Subtotal
subtotal_text = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Subtotal')]/following-sibling::*"))
).text

subtotal = float(subtotal_text.replace("$", "").strip())
print("Subtotal:", subtotal)

# Capture Total Price
total_text = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Total')]/following-sibling::*"))
).text

total = float(total_text.replace("$", "").strip())
print("Total Price:", total)

# Assertions
assert subtotal == car_price, "Subtotal does not match car price"
assert total >= subtotal, "Total price calculation incorrect"

print("Rental Summary price consistency verified successfully")

time.sleep(2)
driver.quit()
