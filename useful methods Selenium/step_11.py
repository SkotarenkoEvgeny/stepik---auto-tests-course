from selenium import webdriver
import time

import os


start_time = time.time()


link = "http://suninjuly.github.io/file_input.html"


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

try:
    # fill the data in form
    x_path = ('//input[@placeholder="{}"]')
    registration_data = (("Введите имя", "Ivan"),
                         ("Введите фамилию", "Petrov"),
                         ("Введите Email", "1@1.com.ru"),
                         )
    for data in registration_data:
        browser.find_element_by_xpath(x_path.format(data[0])).send_keys(data[1])

    # create path to temp.txt-file
    current_dir = os.path.abspath(os.path.dirname('temp.txt'))
    file_path = os.path.join(current_dir, 'temp.txt')
    print(file_path)

    #put the file
    element = browser.find_element_by_xpath('//input[@id="file"]')
    element.send_keys(file_path)

    #click on Submint button
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(30)
finally:
    browser.quit()

    exicution_time = time.time() - start_time
    print('exicution_time = ', exicution_time)