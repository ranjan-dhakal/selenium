import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote import switch_to

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoapp.cellpay.com.np/')

username = driver.find_element(By.XPATH, "//input[@id='username']")
username.send_keys('9860876238')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys('123456')

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


time.sleep(5)
if len(driver.window_handles) > 1:
    popup = driver.window_handles[1]
    driver.switch_to.window(popup)
    driver.close()
    main_window = driver.window_handles[0]
    driver.switch_to.window(main_window)

driver.refresh()

# internet_provider = driver.find_element(By.XPATH, "//a[@href='/dashboard/internet']")
# internet_provider.click()

top_up = driver.find_element(By.XPATH, "//a[@href='/dashboard/topup']")
top_up.click()
mobile_number = driver.find_element(By.XPATH, "//input[@name='mobileNumber']")
mobile_number.send_keys('9860208955')

amount = driver.find_element(By.XPATH, "//input[@name='amount']")
amount.send_keys('2500')

top_up_button = driver.find_element(By.XPATH, "//button[@type='submit']")
top_up_button.click()

# driver.execute_script("window.scrollBy(0, 500);")
# worldlink_function = driver.find_element(By.XPATH, "//img[@src='/img/internet/WorldLink.png']")
# worldlink_function.click()

# profile_section = driver.find_element(By.XPATH, "//button[@class='navbar-account-btn']")
# profile_section.click()
time.sleep(5)
driver.quit()
