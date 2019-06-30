from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
start_time = time.time()


link = "http://suninjuly.github.io/math.html"


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

try:
    number = browser.find_element_by_xpath('//span[@id="input_value"]').text
    print(number)
    calc_data = calc(number)
    # input the number to fild
    browser.find_element_by_xpath('//input[@class="form-control"]').send_keys(calc_data)
    #check the radio-button
    browser.find_element_by_xpath('//input[@id="robotsRule"]').click()
    #check the robotCheckbox
    browser.find_element_by_xpath('//label[@for="robotCheckbox"]').click()
    #click on Submint button
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(30)
finally:
    browser.quit()

    exicution_time = time.time() - start_time
    print('exicution_time = ', exicution_time)