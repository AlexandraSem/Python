# Кости 3.0
# Демонстрируем рандомную генерацию чисел


import random

while True:
    
    ## Делаем ставку
    S = int(input('Введите вашу ставку - от 2 до 12: '))


    # генерируем числа рандомно 1 - 6
    a = random.randint(1, 6)
    b = random.randrange(6) + 1
    total = a + b
    print("Первая кость:", a, "Вторая кость:", b, "В сумме:", total)



    # Выводим результат
    if total == S:
             print ('Ура, вы просто БОЛЬШОЙ везунчик!!!')
             break
    else:
             print ('Пробуем еще раз...\n\n')
             continue

input("\n\nPress the enter key to exit...")

