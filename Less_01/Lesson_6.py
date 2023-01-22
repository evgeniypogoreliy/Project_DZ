# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров
# a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

sec_res = int(input('Введите результат первого дня: '))
final_res = int(input('Введите желаемый результат: '))
day = 1
while sec_res < final_res:
    sec_res = sec_res + (sec_res/100*10)
    day += 1
print(f'На {day} день спотрсмен достигнет не менее {final_res} км')