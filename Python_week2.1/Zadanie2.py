#1.Запросить у пользователя зарплату.Если зарплата от меньше 100, налог - 3.Если зарплата от 100 до 600, налог - 10 .
# Если зарплата от 600 до 2000, налог - 18.Если зарпата более 2000, налог - 22.Вывести'чистую зарплату', налог, и 'глязную зарплату'
zarplata = int(input("Введите зарплату: "))
if zarplata < 100:
    nalog = 0.3
elif zarplata > 100 and zarplata < 600:
    nalog = 0.10
elif zarplata > 600 and zarplata < 2000:
    nalog = 0.18
elif zarplata > 2000 :
    nalog = 0.22
dirtyZarplata = int(zarplata*nalog)
print("Ваша 'чистая зарплата': ",zarplata,"\nНалог: ",nalog,"\nВаша 'грязная зарплата': ",dirtyZarplata)

