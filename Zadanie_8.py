#Запросить у пользователя 3 числа.
	#a.Найти сумму первого и третьего числа.
	#b.Найти произведение суммы, которая получилась в пункте 'a' , на второе число
    #с. Найти среднее арифметическое 3 чисел
		#Вывести 3 числа. Вывести сумму. Вывести произведение. Вывести среднее арифметическое 3 чисел.
	    #p.s. вывод выполнить в одном print - е
firstNumber = int(input('Введите первое число : '))
secondNumber = int(input('Введите второе число : '))
thirdNumber = int(input('Введите третье число : '))
sumFirstAndThird = firstNumber + thirdNumber
proizvedenie = sumFirstAndThird * secondNumber
average = (firstNumber + secondNumber + thirdNumber)/3
print('Первое число:',firstNumber,'Второе число:',secondNumber,'Третье число:',thirdNumber,'\nСумма первого и третьего числа: ',sumFirstAndThird,'\nПроизведение: ',proizvedenie,'\nСреднее арифметическое:',average)
input('Press Enter to continue ...')