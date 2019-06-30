"""
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным кодом.
Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения для поиска вместо слов value1,
value2 и т.д. Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.
"""

from selenium import webdriver

import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"


webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)



value1 = '//input[@name="first_name"]'
input1 = browser.find_element(By.XPATH, value1)
input1.send_keys("Ivan")
value2 = '//input[@name="last_name"]'
input2 = browser.find_element(By.XPATH, value2)
input2.send_keys("Petrov")
value3 = '//input[@name="firstname"]'
input3 = browser.find_element(By.XPATH, value3)
input3.send_keys("Smolensk")
value4 = '//*[@id="country"]'
input4 = browser.find_element(By.XPATH, value4)
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

# except Exception:
#     time.sleep(3)


# finally:
browser.close()
time.sleep(1)
browser.quit()