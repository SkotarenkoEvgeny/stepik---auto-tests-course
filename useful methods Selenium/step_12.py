from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
start_time = time.time()


link = "http://suninjuly.github.io/alert_accept.html"


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

try:

    browser.find_element_by_xpath('/html/body/form/div/div/button').click()

    alert = browser.switch_to.alert
    alert.accept()


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