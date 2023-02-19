from random import *
import json
films = []

def save():
    with open("films.json","w", encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    with open("films.json","r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена!")
try:
    with open("films.json","r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена!")
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара")

while True:
    command = input("введите команду ")
    if command == "start":
        print("Бот-фильмотека начал свою работу ")
    elif command =="/stop":
        save()
        print("Бот остановил свою работу. Заходите ещё, будем рады! ")
        break
    elif command =="/all":
        print("Вот текущий список фильмов: ")
        print(films)
    elif command == "/add":
        f=input("Введите название фильма ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command == "/help":
        print("здесь какой-то мануал")
    elif command == "/delete":
        f=input("Введите название фильма, который нужно удалить ")
        # if f in films:
        #     films.remove(f)
        #     print("Фильм был успешно удален из списка!")
        # else:
        #     print("Такого фильма нет в фильмотеке!")
        try:
            films.remove(f)
            print("Фильм был успешно удален из списка!")
        except:
            print("Такого фильма нет в фильмотеке!")
    elif command == "/random":
        # rnd = randint(0, len(films)-1)
        # print("Слепой жребий показал вам фильм- "+ films[rnd])
        print("Слепой жребий показал вам фильм- "+ choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        with open("films.json","r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена!")
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")
 