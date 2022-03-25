import unittest # 1.Импортировать unittest в файл

class TestAbs(unittest.TestCase) # 2. Создать класс, который должен наследоваться от класса TestCase


    def test_abs1(self): #Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции
    self.assertEqual(abs(-42) == 42, "Should be absolute value of a number") #Изменить assert на self.assertEqual()

if __name__ == "__main__":
    unittest.main()

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time


