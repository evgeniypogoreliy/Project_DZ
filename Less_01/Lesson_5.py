# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.

rev = int(input('Введите знаечение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if rev > costs:
    print('Прибыль!')
elif costs > rev:
    print('Убыток...')

    # 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
    # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = rev - costs
profitability = 0
if profit > 0:
    profitability = (profit / rev)*100
    size = int(input('Введите количество сотрудников вашей фирмы: '))
    prof_size = profitability / size
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {prof_size}')
print('Программа завершена.')