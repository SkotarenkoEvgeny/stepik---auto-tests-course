from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

link = 'http://suninjuly.github.io/find_xpath_form'




def registrarion_script(link):

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

    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
    button.click()
    browser.close()
    time.sleep(1)
    browser.quit()

registrarion_script(link)