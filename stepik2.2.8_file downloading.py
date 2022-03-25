from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    # Заполнить текстовые поля: имя, фамилия, email
    input_name = browser.find_element(By.NAME, 'firstname').send_keys('Lili')
    input_surname = browser.find_element(By.NAME, 'lastname').send_keys('Demini')
    input_email = browser.find_element(By.NAME, 'email').send_keys('popp@mail.ru')

    # указать путь к файлу, который нужно загрузить
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    with open("test1.txt", "w") as file:
        content = file.write("automationbypython")  # создаем test.txt file

    # указываем к кнопке загрузки путь загружаемого файла
    download = browser.find_element(By.ID, 'file').send_keys(os.path.join(os.path.dirname(__file__), 'test1.txt'))

    os.remove("test1.txt")  # удаляем ранее созданный .txt файл

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()