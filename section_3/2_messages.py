# Форматирование строк с помощью конкатенации
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")

# Форматирование строк с помощью str.format
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# Форматирование строк с помощью f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# когда вы работаете с текстом элементов на странице или любым другим контентом,
# который может измениться, всегда записывайте его в отдельную переменную для сравнения.
catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"


# составные сообщения об ошибках
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result,\
        f"expected {expected_result}, got {actual_result}"


# составные сообщения об ошибках и поиск подстроки
s = 'My Name is Julia'
if 'Name' in s:
    print('Substring found')
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# Пример
def test_substring(full_string, substring):
    assert substring in full_string,\
        f"expected '{substring}' to be substring of '{full_string}'"

