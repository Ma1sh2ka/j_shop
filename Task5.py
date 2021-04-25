user_data = {}

def all_user_data():
    global user_data
    pass

def show_user():
    global user_data
    print('Введите пользователя, которого хотите удалить.')
    login = input()
    if login in user_data.keys():
        for key, value in user_data[login].items():
            print(key + ":", value)
    else:
        print('Нет такого пользователя.')

def change_user():
    global user_data
    print('Введите пользователя, которого хотите удалить.')
    login = input()
    if login in user_data.keys():
        print('Введите Ваш вес в килограммах')
        m = int(input())
        print('Введите Ваш рост в сантиметрах')
        h = int(input())
        print('Введите Ваш пол: м или ж')
        sex = str(input())
        user_data[login] = {'Вес': m, 'Рост': h, 'Пол': sex}
    else:
        print('Нет такого пользователя.')        

def delete_user():
    global user_data
    print('Введите пользователя, которого хотите удалить.')
    login = input()
    if login in user_data.keys():
        del user_data[login]
        print('Ваши данные удалены.')
    else:
        print('Нет такого пользователя.')

def create_user(*args, **kwargs):
    global user_data
    while True:
        print('Введите логин.')
        login = input()
        if login in user_data.keys():
            print('Такой пользователь уже есть.')
        else:
            break
    print('Введите Ваш вес в килограммах')
    m = int(input())
    print('Введите Ваш рост в сантиметрах')
    h = int(input())
    print('Введите Ваш пол: м или ж')
    sex = str(input())
    user_data[login] = {'Вес': m, 'Рост': h, 'Пол': sex}
    
    BMI = int(m*10000/h**2)
    print('Ваш индекс массы тела составляет', BMI)
    scale =[20, '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', 50]
    scale.insert(BMI-20, '||')
    print("".join(map(str, scale)))
    if sex == 'м':
        if BMI <= 25:
            print('Ну что же, Вы можете и дальше валяться на диване ))', 'Ваш индекс массы \
    тела в норме.', sep = '\n')
        elif BMI > 25 and BMI <= 29:
            print('Эй, тебе стоит задуматься.', 'У тебя избыточный вес!!', sep = '\n')
        else:
            print('КАРАУЛ.', 'Тебя постигло ожирение.', 'Надо что-то делать...', sep = '\n')
    elif sex == 'ж':
        if BMI <= 23:
            print('Ну что же, Вы можете и дальше валяться на диване ))', 'Ваш индекс массы \
    тела в норме.', sep = '\n')
        elif BMI > 23 and BMI <= 27:
            print('Эй, тебе стоит задуматься.', 'У тебя избыточный вес!!', sep = '\n')
        else:
            print('КАРАУЛ.', 'Тебя постигло ожирение.', 'Надо что-то делать...', sep = '\n')

def exit_program():
    print('До свидания!')

while True:
    print('Введите 1 для отображения списка пользователей.')
    print('Введите 2 для просмотра информации о пользователе.')
    print('Введите 3 для изменения информации о пользователе.')
    print('Введите 4 для удаления выбранного пользователя.')
    print('Введите 5 для добавления пользователя.')
    print('Введите 6 для выхода из программы.')
    answer = input()
    if answer == '1':
        all_user_data()
    elif answer == '2':
        show_user()
    elif answer == '3':
        change_user()
    elif answer == '4':
        delete_user()
    elif answer == '5':
        create_user()
    elif answer == '6':
        exit_program()
        break
    else:
        print('Введите значение от 1 до 6.')