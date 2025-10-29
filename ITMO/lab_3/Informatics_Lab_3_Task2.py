# Author = Dzhun Alexandra Vasilievna
# Group = P3106
# Date = 09.10.2025

import re


def f(x):
    return 5 * (x**3) - 13

def encrypt_text(text):
    def num(match):
        return str(f(int(match.group(0))))

    return re.sub(r'(?<!\d)\d+(?!\d)', num, text)


print('Тест №1\n')
text = "Студент Вася очень любит курс «Компьютерная безопасность». Однажды Васе задали домашнее задание зашифровать данные, переданные в сообщении. Недолго думая, Вася решил заменить все целые числа на функцию от этого числа. Функцию он придумал не сложную 5x^3–13 ,где x – исходное число . Помогите Васе с его домашним заданием."
print(text, '\n')
print(encrypt_text(text),'\n')

print('Тест №2\n')
text_with_symbols = "Тест с числами 123 и символами !@#$ 45,67 и 89."
print(text_with_symbols, '\n')
print(encrypt_text(text_with_symbols),'\n')

print('Тест №3\n')
test_negative = "Температура сегодня -10 градусов."
print(test_negative,'\n')
print(encrypt_text(test_negative),'\n')

print('Тест №4\n')
test_multiple = "В этой строке 1 число, а тут уже 2 и 3 подряд!"
print(test_multiple,'\n')
print(encrypt_text(test_multiple),'\n')

print('Тест №5\n')
test_mixed = "Итого: 10 яблок, 20 груш и 30 апельсинов. А всего 60!"
print(test_mixed,'\n')
print(encrypt_text(test_mixed))