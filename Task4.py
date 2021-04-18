print('Введите Ваш Логин:')
login = str(input())
def decorator(account):
    def admin(*args, **kwargs):
        if args[0] == 'administrator':
            account()
        else:
            print('У Вас нет прав доступа!')
    return admin

@decorator
def account(*args, **kwargs):
    print('На счете .... денег')

account(login)