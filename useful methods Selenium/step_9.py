from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time



def calc(x, y):
    return str(int(x) + int(y))

start_time = time.time()


link = "http://suninjuly.github.io/selects1.html"


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

try:
    x = browser.find_element_by_xpath('//span[@id="num1"]').text
    y = browser.find_element_by_xpath('//span[@id="num2"]').text
    print(x, y)
    select = Select(browser.find_element_by_xpath('//select[@class="custom-select"]'))
    select.select_by_value(calc(x, y))
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(30)
finally:
    browser.quit()

    exicution_time = time.time() - start_time
    print('exicution_time = ', exicution_time)