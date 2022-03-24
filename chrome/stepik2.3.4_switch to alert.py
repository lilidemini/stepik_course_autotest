from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    # Нажать на кнопку
    button = browser.find_element(By.TAG_NAME, 'button').click()

    # Подтвердить в модальном окне
    confirm = browser.switch_to.alert
    confirm.accept()

    # Высчитываем пример в функции
    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log((abs(12*math.sin(int(x))))))
    y = calc(x)

    # Вводим ответ в поле
    input = browser.find_element(By.ID, 'answer').send_keys(y)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    # Выводим текст кодового числа из алерта
    print(browser.switch_to.alert.text)

    # Подтверждаем алерт, модальное окно закрывается
    alert = browser.switch_to.alert.accept()


finally:
    time.sleep(10)
    browser.quit()