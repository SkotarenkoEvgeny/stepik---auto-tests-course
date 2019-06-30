from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get(link)

# Ваш код, который заполняет обязательные поля

x_path = ('//input[@placeholder="{}"]')

registration_data = (("Введите имя", "Ivan"),
                     ("Введите фамилию", "Petrov"),
                     ("Введите Email", "1@1.com.ru"),
                     ("Введите телефон:", "095-255-55-55"),
                     ("Введите адрес:", "Russia, Moskow"))

for data in registration_data:
    browser.find_element_by_xpath(x_path.format(data[0])).send_keys(data[1])

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
browser.close()
browser.quit()