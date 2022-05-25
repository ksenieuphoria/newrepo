
# Задача: Программа будет генерировать случайное число, пользователь должен угадать это число.
# Если угадал - дать понять, что выиграл, иначе вывести информацию о том, что проиграл

import random

rand_number = random.randint(1, 100)
x = input()
while x != 'rand_number':
    print('wrong')
    x = input()
print ('right')