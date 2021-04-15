print('Привет. Введите 3 числа:')
a = int(input())
b = int(input())
c = int(input())
print((not(a != 0 or b != 0 or c != 0) and 'Введены все нули') or (not a or \
not b or not c or 'Нет нулевых значениий!!!'))
if a > (b + c):
    print(a - b - c)
if a < (b + c):
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print('Вася')
if a > 5 or (b == 7 and c == 7):
    print('Петя')