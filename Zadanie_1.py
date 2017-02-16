#1.Посчитать четные и нечетные цифры числа
number = 0
countCh = 0
countNch = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        countCh +=1
    else :
        countNch +=1
print("Четных чисел всего: ",countCh,"Нечетных чисел всего: ",countNch)
input("Press Enter to continue")