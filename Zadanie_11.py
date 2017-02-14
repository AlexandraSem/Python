#N человек снимают квартиры на лето. 50% из них живет неделю, 40% - 15 дней, а остальные по 20 дней. Оплата проживания за 1 день равна х руб. Сколько налогов заплатят хозяева, если они составляют 13% от всей выручки.
firstPeopleProcent = 50
secondPeopleProcent = 40
lastPeopleProcent = 100-(firstPeople+SecondPeople)
nalog = 13
day = int(input('Введите стоимость одного дня проживания:'))
people = int(input('Введите сколько людей снимают квартиры:'))
firstPeople =(people * firstPeopleProcent)/100
firstCost = firstPeople*(day*7)
secondPeople =(people * secondPeopleProcent)/100
secondCost = secondPeople*(day*15)
lastPeople =(people * lastPeopleProcent)/100
lastCost = lastPeople*(day*20)
allSummNalog = int((firstCost+secondCost+lastCost)/13)
print('Налог составит ',allSummNalog,' руб')
input('Press Enter to continue ...')
