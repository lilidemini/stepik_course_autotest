from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button1 = browser.find_element(By.ID, 'book').click()

    # Проскроллить страницу вниз на 100 пикселей
    browser.execute_script("window.scrollBy(0, 100);")

        # Высчитываем пример в функции
    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log((abs(12 * math.sin(int(x))))))
    y = calc(x)

        # Вводим ответ в поле
    input = browser.find_element(By.ID, 'answer').send_keys(y)

        # Нажимаем кнопку
    button2 = browser.find_element(By.ID, 'solve').click()

 # Выводим текст кодового числа из алерта
    print(browser.switch_to.alert.text)

    # Подтверждаем алерт, модальное окно закрывается
    alert = browser.switch_to.alert.accept()
finally:
    time.sleep(20)
    browser.quit()