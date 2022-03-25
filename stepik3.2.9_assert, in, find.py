from selenium import webdriver


# s = 'My Name is Julia'

# поиск с ключевым словом in
# if 'Name' in s:
#     print('Substring found')

# поиск с помощью функции find
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

# Задание 3.2.9
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
