import json
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import colorama

driver = webdriver.Chrome()
driver.maximize_window()

# Define the length of the code
code_length = 6

# Generate a random hex string of length code_length
code = secrets.token_hex(code_length // 2 + 1)[:code_length]
invoice = secrets.token_hex(code_length // 2 + 1)[:code_length]


# Define the clear_all_fields function
def clear_all_fields():
    fields = driver.find_elements(By.XPATH, "//input[@type='text']")
    for field in fields:
        field.clear()


# Load the JSON data
with open('Test Automation/json/checkout.json', "r") as f:
    data = json.load(f)

# Start the browser and navigate to the page
driver.get("file:///C:/Users/Sanjeet%20Jung%20Gurung/Downloads/demo-client.html")

# Iterate over each data object and submit the form
for value in data:

    colorama.init()
    print(colorama.Fore.YELLOW + f"Test Data No.{value['SN']} is running")
    print(colorama.Style.RESET_ALL)
  # Deinitialize colorama
    colorama.deinit()

    clear_all_fields()

    mode = driver.find_element(By.NAME, "mode")
    mode.send_keys(value["Mode"])

    transaction = driver.find_element(By.NAME, "transaction_type")
    transaction.send_keys(value["TransactionType"])

    merchant = driver.find_element(By.NAME, "merchant_id")
    merchant.send_keys(value["Merchant_id"])

    driver.find_element(By.NAME, "description").send_keys(value["Description"])
    driver.find_element(By.NAME, "amount").send_keys(value["Amount"])
    driver.find_element(By.NAME, "invoice_no").send_keys(invoice)
    driver.find_element(By.NAME, "trace_no").send_keys(code)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    try:
        # Find the element with class "card-header" and text "Details"
        element = driver.find_element(By.XPATH, "//div[@class='card-header ' and contains(strong, 'Details')]")
        print(colorama.Fore.GREEN + f"Test Data No.{value['SN']} is Passed")
        print(colorama.Style.RESET_ALL)
    except NoSuchElementException:
        try:
            element = driver.find_element(By.XPATH, "//div[contains(@class,'border-for-error') and .//h3[contains(text(),'Invalid Request')]]")
            print(colorama.Fore.RED + f"Test Data No.{value['SN']} is Failed")
            print(colorama.Style.RESET_ALL)
        except NoSuchElementException:
            print("No xpath found ")
    driver.back()
    print("\n")

# Close the browser
driver.quit()
