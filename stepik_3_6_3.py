import pytest
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

# фикстура браузера, далее перенесли ее в файл conftest.py
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('unit', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
class TestAnswer:
    def test_answer(self, browser, unit):
        link = f"https://stepik.org/lesson/{unit}/step/1"
        browser.get(link)

        #высчитываем время с погрешностью на данном компьютере
        answer = str(math.log(int(time.time() + 0.8)))

        # вставляем в поле ответ
        input1 = browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)

        # нажимаем
        button1 = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()

        # сравниваем фактический текст с ожидаемым в черном поле
        expected_result = 'Correct!'
        actual_result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert actual_result == expected_result, f"expected '{expected_result}', got '{actual_result}'"
