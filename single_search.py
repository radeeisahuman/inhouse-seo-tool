from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import take_cred
import time
import pandas as pd

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
    this_dict = {
        "name": [],
        "search_volume": []
    }
    while i == "y":
        keyword = input("Enter the name of the things you want to search")
        input_field.send_keys(keyword + Keys.ENTER)
        time.sleep(2)
        rows = modal.find_elements(By.XPATH, ".//tbody/tr")
        for row in rows:
            try:
                name_of_keyword = row.find_elements(By.TAG_NAME, "td")[0].text.strip()
                search_volume_td = row.find_elements(By.TAG_NAME, "td")[1]
                search_volume = search_volume_td.text.strip()
                this_dict["name"].append(name_of_keyword)
                this_dict["search_volume"].append(search_volume)
            except Exception as e:
                print("Error extracting search volume from a row:", str(e))
        print("Do you want to continue(y/n)")
        i = input()
        input_field.clear()

    df = pd.DataFrame(this_dict)
    df.to_csv("Previous Search.csv")
    time.sleep(2)

    driver.quit()