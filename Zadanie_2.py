#2. Напишите программу-игру. Компьютер загадывает случайное число, пользователь
#пытается его угадать. Пользователь вводит число до тех пор, пока не угадает или не
#введет слово «Выход». Компьютер сравнивает число с введенным и сообщает
#пользователю больше оно или меньше загаданного.
import random
secretNumber = (random.randint(0,10))
userNumber = int(input("Игра угадайка.Введите число:\n"))
while userNumber != secretNumber:
    if userNumber > secretNumber:
        userNumber = int(input("Меньше.Попробуй ещё\n"))
    else:
        userNumber = int(input("Больше.Попробуй ещё\n"))
input("Угадал\nPress Enter to continue")