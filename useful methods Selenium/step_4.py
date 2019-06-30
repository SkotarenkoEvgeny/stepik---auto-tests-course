from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'


browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)


elements = browser.find_elements_by_xpath('//input')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()

browser.close()
time.sleep(1)
browser.quit()