#Вычислить зарплату рабочего за Х дней работ, если он получает фиксированный заработок за 1 день. Заработок за 1 день описать как константу, значение переменной к ввести с клавиатуры.
ZarplataFirstDay = 17
K = int(input('Введите количество рабочих дней : '))
ZarplataMonth = ZarplataFirstDay * K
print("Зарплата рабочего составляет",ZarplataMonth,"рублей")
input('Press Enter to continue ...')