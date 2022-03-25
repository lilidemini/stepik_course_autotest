from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link='http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст примера, котрый нужно рассчитать
    #x_element = browser.find_element(By.CSS_SELECTOR, 'label > span.nowrap')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    print(x)
    # Функция для расчета и возврата значения
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # Вводим ответ в текстовое поле
    input = browser.find_element(By.ID,'answer').send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, 'robotsRule').click()

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()