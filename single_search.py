from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import take_cred
import time

def single_search():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.reed.co.uk/courses/providers/account/signin")

    time.sleep(5)

    button_element = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button_element.click()

    time.sleep(2)

    input_elements = driver.find_elements(By.CLASS_NAME, "form-control")
    data = take_cred.get_credentials()
    username = data['name']
    password = data['password']
    input_elements[0].send_keys(username)
    input_elements[1].send_keys(password + Keys.ENTER)

    time.sleep(3)

    driver.get("https://www.reed.co.uk/courses/providers/sponsored/503150")
    table_header = driver.find_element(By.CLASS_NAME, "table-header")
    table_button = table_header.find_element(By.CLASS_NAME, "btn-primary")
    table_button.click()

    time.sleep(2)

    modal = driver.find_element(By.CLASS_NAME, "modal-content")
    input_field = modal.find_element(By.CLASS_NAME, "form-control")

    i = "y"
    while i == "y":
        keyword = input("Enter the name of the things you want to search")
        input_field.send_keys(keyword + Keys.ENTER)
        print("Do you want to continue(y/n)")
        i = input()
        input_field.clear()

    time.sleep(2)

    driver.quit()