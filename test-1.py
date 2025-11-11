from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "http://localhost:5000"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # ---------- TEST 1: Valid Data ----------
    print("Running Test 1: Valid Input (Expect Success Message)")
    driver.get(URL)
    driver.maximize_window()

    # Fill valid inputs
    driver.find_element(By.ID, "name").send_keys("Ayush Astiker")
    driver.find_element(By.ID, "roll-number").send_keys("21CS123")
    driver.find_element(By.ID, "college").send_keys("JNTU Hyderabad")
    driver.find_element(By.ID, "branch").send_keys("CSE")
    driver.find_element(By.ID, "email").send_keys("ayush@example.com")
    driver.find_element(By.ID, "mobile").send_keys("9876543210")
    driver.find_element(By.ID, "gender").send_keys("Male")
    driver.find_element(By.ID, "year").send_keys("2nd Year")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for success message to appear
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "success-message"))
    )
    print("✅ Test 1 Passed: Success message displayed.")

    # ---------- TEST 2: Invalid Data ----------
    print("Running Test 2: Missing Fields (Expect Error Message)")
    driver.get(URL)
    time.sleep(1)

    # Explicitly clear inputs before leaving them blank
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "roll-number").clear()
    driver.find_element(By.ID, "college").send_keys("JNTU Hyderabad")
    driver.find_element(By.ID, "branch").clear()
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "mobile").clear()
    driver.find_element(By.ID, "gender").send_keys("")  # leave default "Select Gender"
    driver.find_element(By.ID, "year").send_keys("")    # leave default "Select Year"

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for error message to appear
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "error-message"))
    )
    print("✅ Test 2 Passed: Error message displayed.")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    time.sleep(2)
    driver.quit()
