# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

year = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
choice = int(input('Введите номер месяца: '))
if choice in year[0]:
    print('Выбранный месяц относится к зиме.')
if choice in year[1]:
    print('Выбранный месяц относится к весне.')
if choice in year[2]:
    print('Выбранный месяц относится к лету.')
if choice in year[3]:
    print('Выбранный месяц относится к осени.')