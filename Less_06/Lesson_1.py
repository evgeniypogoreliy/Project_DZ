# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in range(3):
            print(f'Светофор горит: {TrafficLight.__color[i]}')
            if TrafficLight.__color[i] == 'Красный':
                time.sleep(7)
            elif TrafficLight.__color[i] == 'Желтый':
                time.sleep(2)
            elif TrafficLight.__color[i] == 'Зеленный':
                time.sleep(5)

a = TrafficLight()
a.running()