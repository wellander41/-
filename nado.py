import time
import datetime

# делаем функцию которая обратку считает
def countdown(h, m, s):
    # вычисляем количество секунд
    total_seconds = h * 3600 + m * 60 + s

    # проверка равно ли количество секунд 0
    # если не 0 то отнимаем 1
    while total_seconds > 0:
        # таймер думает сколько осталось посчитать
        timer = datetime.timedelta(seconds=total_seconds)

        # выводит сколько осталось
        print(timer, end="\r")

        # шаг 1 секунда
        time.sleep(1)

        # отнимает по 1 секунде
        total_seconds -= 1

    print(x)


# ввод часов минут и секунд а так же че хотим
h = input("пиши часы: ")
m = input("давай минуты: ")
s = input("го секунды: ")
x = input("че хотел то?")
countdown(int(h), int(m), int(s))

