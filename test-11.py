from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    print("Opening the login demo site...")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # Enter credentials
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)

    # Verify login success
    message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in message:
        print("✅ Test Passed: Login successful message displayed.")
    else:
        print("❌ Test Failed: Unexpected message.")

except Exception as e:
    print(f"❌ Error during test: {e}")

finally:
    time.sleep(2)
    driver.quit()
