from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

link = 'http://suninjuly.github.io/find_link_text'

webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)



data = str(math.ceil(math.pow(math.pi, math.e)*10000))
print("data=", data)

data_link = browser.find_element_by_link_text(data).get_attribute('href')
print("data_link=", data_link)
print(type(data_link))

browser.close()
browser.quit()


def registrarion_script(link):

    webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    browser.get(link)


    values = ('//input[@name="first_name"]',
              '//input[@name="last_name"]',
              '//input[@name="firstname"]',
              '//*[@id="country"]'
              )
    registration_data = ("Ivan", "Petrov", "Smolensk", "Russia")

    for data in zip(values, registration_data):
        browser.find_element(By.XPATH, data[0]).send_keys(data[1])

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    browser.close()
    time.sleep(1)
    browser.quit()

registrarion_script(data_link)