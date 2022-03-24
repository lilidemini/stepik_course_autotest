from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    # Считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    print(x)

    # Посчитать математическую функцию от x
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, 'answer').send_keys(y)

    # Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()

    # Проскроллить страницу вниз на 100 пикселей
    browser.execute_script("window.scrollBy(0, 100);")

    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, 'robotsRule').click()

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.TAG_NAME, 'button').click()
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) скролл к кнопке

finally:
    time.sleep(10)
    browser.quit()