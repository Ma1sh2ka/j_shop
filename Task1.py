string = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. \
А у нас управдом — друг человека!'
print('Задание 1 -', len(string))
print('Задание 2 -', string[::-1])
print('Задание 3 -', string.title())
print('Задание 4 -', string.upper())
print('Задание 5 -', 'нд -', string.count('нд'), 'ам -', string.count('ам'), \
      'о -', string.count('о'))
print('Задание 6 -', string.replace('друг', 'ФАНАТ'))
print('', (string[::4]), 'ХА-ХА!!!!!')
print(string.count('д') * 3)
print(string.endswith('!'))
print(string.endswith('а'))
print('Задание 7 -', string)
'''
Необходимо:
1. Посчитать       соличество     символов
2. Развернуть    строку
3. Сделать каждое слово с большой буквы
4. Сделать весь текст прописными буквами
5. Найти число вхождений "нд", "ам", "о" в строку
6. Собственные упражнения
7. Вывести в консоль исходную строку
Вывести в консоль результат каждого шага: Например: Шаг1 - Количество символов - 4
'''
