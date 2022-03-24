from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Вытаскивает текст из значений по ID, преобразуем его из str в int
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    # Посчитать сумму заданных чисел, вернем снова в str для дальнейших действий
    sum = str(num1 + num2)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(sum)

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()