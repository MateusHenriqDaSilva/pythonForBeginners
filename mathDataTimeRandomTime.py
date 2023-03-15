import math

math.sqrt()
math.sin()
math.cos(45)
math.log(1000, 10)
math.log(32, 2)
math.log(1000)
math.e
math.pi

import datetime

datetime.date.today()
datetime.date(2020, 7,7)
datetime.datetime.now()
datetime.datetime(2020,7,7,15,57,29,736883)
data = datetime.date(2020, 7, 10)
data
data.day
data.month
data.year
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
horario.hour
horario.minute
horario.second

import random

random.random()
random.randint(1,10)
random.randrange(0, 10, 2)
random.randrange(0, 10, 3)
x = ['K',9,'B',10]
random.choice(x)

import time as tm
tm.time()
antes = tm.time()
lista = []
for i in range(0,1000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes
print(f'tempo: {intervalo} segundos' )
print('finalizando ')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a proxima')
