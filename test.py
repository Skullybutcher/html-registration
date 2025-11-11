from selenium import webdriver
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
# Open a webpage
driver.get("http://selenium.dev")
# Print the page title
print("Title:"+ driver.title)

driver.quit()