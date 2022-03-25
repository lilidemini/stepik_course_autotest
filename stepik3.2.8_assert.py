from selenium import webdriver

# Через запятую написать информативное сообщение, которое будет выведено в случае ошибки проверки результата
assert abs(-42) == 42, "Should be absolute value of a number"


# после падения автотеста сравниваем actual_result и expected_result, старый способ:
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# современный способ использовать f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

# Задание 3.2.8
def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"
