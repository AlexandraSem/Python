#Автобус провозит 50 пассажиров. Из них 10 едут до первой остановки, 20 - до второй, а остальные до конечной. Стоимость билетов до каждой станции соответственно равно a, b, c. Определите сколько рейсов должен делать автобус, чтобы выручка составила К руб.
bus = 50
firstStop = 10
secondStop = 20
lastStop = bus-(firstStop+secondStop)
a = int(input("Введите стоимость проезда до первой остановки: "))
b = int(input("Введите стоимость проезда до второй остановки: "))
c = int(input("Введите стоимость проезда до последней остановки: "))
k = int(input("Введите выручку: "))
number = int((10 * a + 20 * (b + c))/k)
print('Автобус должен совершить ',number,'рейсов')
input('Press Enter to continue ...')
