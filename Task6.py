while True:
    import datetime
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    hour1 = datetime.datetime.now().hour
    minute1 = datetime.datetime.now().minute
    second1 = datetime.datetime.now().second
    print(current_time)
'''
    if numb == 0:
        a[0] = (' ', '\u2B1B', ' ')
        a[1] = ('\u2B1B', ' ', '\u2B1B')
        a[2] = ('\u2B1B', ' ', '\u2B1B')
        a[3] = ('\u2B1B', ' ', '\u2B1B')
        a[4] = (' ', '\u2B1B', ' ')

    if numb == 1:
        a[0] = (' ', '\u2B1B', ' ')
        a[1] = ('\u2B1B', '\u2B1B', ' ')
        a[2] = (' ', '\u2B1B', ' ')
        a[3] = (' ', '\u2B1B', ' ')
        a[4] = (' ', '\u2B1B', ' ')

    if numb == 2:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = ('\u2B1B', ' ', '\u2B1B')
        a[2] = (' ', ' ', '\u2B1B')
        a[3] = (' ', '\u2B1B', ' ')
        a[4] = ('\u2B1B', '\u2B1B', '\u2B1B')

    if numb == 3:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = (' ', ' ', '\u2B1B')
        a[2] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[3] = (' ', ' ', '\u2B1B')
        a[4] = ('\u2B1B', '\u2B1B', '\u2B1B')

    if numb == 4:
        a[0] = ('\u2B1B', ' ', '\u2B1B')
        a[1] = ('\u2B1B', ' ', '\u2B1B')
        a[2] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[3] = (' ', ' ', '\u2B1B')
        a[4] = (' ', ' ', '\u2B1B')

    if numb == 5:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = ('\u2B1B', ' ', ' ')
        a[2] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[3] = (' ', ' ', '\u2B1B')
        a[4] = ('\u2B1B', '\u2B1B', '\u2B1B')

    if numb == 6:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = ('\u2B1B', ' ', ' ')
        a[2] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[3] = ('\u2B1B', ' ', '\u2B1B')
        a[4] = ('\u2B1B', '\u2B1B', '\u2B1B')

    if numb == 7:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = (' ', ' ', '\u2B1B')
        a[2] = (' ', '\u2B1B', ' ')
        a[3] = ('\u2B1B', ' ', ' ')
        a[4] = ('\u2B1B', ' ', ' ')

    if numb == 8:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = ('\u2B1B', ' ', '\u2B1B')
        a[2] = (' ', '\u2B1B', ' ')
        a[3] = ('\u2B1B', ' ', 'u2B1B')
        a[4] = ('\u2B1B', 'u2B1B', 'u2B1B')

    if numb == 9:
        a[0] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[1] = ('\u2B1B', ' ', '\u2B1B')
        a[2] = ('\u2B1B', '\u2B1B', '\u2B1B')
        a[3] = (' ', ' ', 'u2B1B')
        a[4] = ('\u2B1B', 'u2B1B', 'u2B1B')
        
    clock = [[], [], [], [], [], [], [], []]
'''
    print(hour, '\u2B1B', minute, '\u2B1B', second)

    import time
    time.sleep(0.3)

    import os
    clear = lambda: os.system('cls')
    clear()
