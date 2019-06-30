from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
start_time = time.time()


link = "http://suninjuly.github.io/explicit_wait2.html"


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

try:

    #waiting where price down to 10000/ After click the button
    term = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
    button = browser.find_element_by_xpath('//button[@id="book"]')
    button.click()
    

    number = browser.find_element_by_xpath('//span[@id="input_value"]').text
    print(number)
    calc_data = calc(number)

    browser.find_element_by_xpath('//input[@class="form-control"]').send_keys(calc_data)
    

    #click on Submint button
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(30)
finally:
    browser.quit()

    exicution_time = time.time() - start_time
    print('exicution_time = ', exicution_time)