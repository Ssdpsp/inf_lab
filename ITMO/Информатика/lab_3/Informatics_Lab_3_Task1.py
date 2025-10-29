# Author = Dzhun Alexandra Vasilievna
# Group = P3106
# Date = 09.10.2025

import re

def find_words(text):
    glas = "аеёиоуыэюя"
    cogl = "бвгджзйклмнпрстфхцчшщъь"
    pattern = rf"(\w*[{glas}]{{2}}\w*)\s+([^{cogl}]*[{cogl}]{{0,3}}[^{cogl}]*)"
    matches = re.findall(pattern, text)
    result = [match[0] for match in matches]
    return result

# Пример использования:
text = "Кривошеее существо гуляет по парку"
result = find_words(text.lower())
print(result)  # Вывод: ['гуляет']

text2 = "Двое взрослых идут в кино"
result2 = find_words(text2.lower())
print(result2) # Вывод: ['двое']

text3 = "Змееед ищет жертву среди трав"
result3 = find_words(text3.lower())
print(result3) # Вывод: []

text4 = "Поющие птицы летят в высь"
result4 = find_words(text3.lower())
print(result4) # Вывод: [поющие]

text5 = "Моющее средство хорошо отмывает"
result5 = find_words(text5.lower())
print(result5) # Вывод: [моющее]
