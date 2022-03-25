from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/wait1.html')
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()

message = browser.find_element_by_id("verify_message")
assert message.text == "Verification was successful!"
# или так: assert "successful" in message.text