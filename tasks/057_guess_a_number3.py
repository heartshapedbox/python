# Выберите случайное целое число в диапазоне от
# 1 до 10. Предложите пользователю ввести число
# и проверьте, совпадает ли оно с загаданным. Продолжайте запрашивать числа до тех пор, пока пользователь не введет случайно выбранное число. Сообщайте
# пользователю, является ли его предположение больше или
# меньше загаданного
# числа.

import random

randomNumber = random.randrange(1, 10)
guess = int(input("Hello! Guess a number from 1 to 10: "))
if guess > 10:
    print("Error.")
else:
    while randomNumber != guess:
        if randomNumber < guess:
            guess = int(input("You guessed wrong, it doesn't match. Your number is highter. Try again! Enter a number: "))
        else:
            guess = int(input("You guessed wrong, it doesn't match. Your number is lower. Try again! Enter a number: "))
    print("Here we go! The nubmer is", randomNumber)
