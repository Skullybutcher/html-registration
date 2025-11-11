from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome with higher timeout and stable options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(20)  # wait up to 20 seconds for page load

try:
    print("Opening Wikipedia...")
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()
    print("Opened Wikipedia successfully.")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Python (programming language)")
    search_box.send_keys(Keys.RETURN)
    print("Searched for Python (programming language)")

    time.sleep(2)

    heading = driver.find_element(By.ID, "firstHeading").text
    if "Python" in heading:
        print("✅ Test Passed: Heading contains 'Python'")
    else:
        print("❌ Test Failed: Heading does not contain 'Python'")

except Exception as e:
    print(f"❌ Error during test: {e}")

finally:
    time.sleep(2)
    driver.quit()
