from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Login function
def login():
    driver.find_element(By.NAME, "username").send_keys("9860208955")
    driver.find_element(By.NAME, "password").send_keys("208955")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()


# Create a new instance of the Firefox driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://app.cellpay.com.np/')

# Call the login function
login()

# Wait for 3 seconds
WebDriverWait(driver, 3)
# Wait for the Share Payment link to be clickable and then click on it
share_payment_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dashboard/share']")))
share_payment_link.click()

# Click on the Share Payment link
driver.find_element(By.XPATH, "//a[@href='/dashboard/share']").click()


# Define the renewal system and subscribe system
renew_system = [
    {"title": "Prabbhu Capital", "alt": "PrabhuCapital"}
]
subs_system = [
    {"title": "Laxmi Capital", "alt": "LaxmiCapital"}
]

# Click on the Renewal button
driver.find_element(By.CSS_SELECTOR, "[alt='Renew']").click()

# Loop through each item in the renewal system and click on it
for renew in renew_system:
    driver.find_element(By.CSS_SELECTOR, "[alt='" + renew["alt"] + "']").click()

# Click on the Subscribe button
driver.find_element(By.CSS_SELECTOR, "[alt='Subscribe']").click()

# Loop through each item in the subscribe system and click on it
for subs in subs_system:
    driver.find_element(By.CSS_SELECTOR, "[alt='" + subs["alt"] + "']").click()

# Close the browser
driver.quit()
