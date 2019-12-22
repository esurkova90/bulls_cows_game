# -*- coding: utf-8 -*-
import random
# TODO - Чтобы сделать секретное число приватным, пиши с нижним подчеркиванием: _computer_number
computer_number = []


def make_the_number():
    global computer_number
    list_numbers = list(range(0, 10))
    computer_number = (random.sample(list_numbers, 4))
    if computer_number[0] == 0:
        x = random.randint(1, 3)
        computer_number[0] = computer_number[x]
        computer_number[x] = 0
    # for place, number in enumerate(computer_number):
    #     computer_number[place] = str(number)
    # TODO - Так тоже можно
    computer_number = list(map(str, computer_number))
    # print("Номер компьютера", computer_number)


def check_the_number(gamer_number):
    animals = {"bulls": 0, "cows": 0}
    for position in range(0, 4):
        if gamer_number[position] == computer_number[position]:
            animals["bulls"] += 1
        elif gamer_number[position] in computer_number:
            animals["cows"] += 1
    return animals["bulls"], animals["cows"]
