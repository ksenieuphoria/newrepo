# Создать переменную
# Написать пароль
# Проверить цикл while

password = '' # есть поле для ввода/получаем условие
while password != 'qwerty':
    print('enter your password:')
    password = str(input())
print('You may enter..')

# случайные числа
import random

rand_number = random.randint(1,100) # как генирировать случайное число
# импорт всегда вверху
# угадать число это input. for или while
import random

rand_number = random.randint(1,100)
x = input()
while x != 'rand_number':
    print('try once again')
    if x == rand_number:
        print('YOU WIN!')
    else:
        print('LOOSE ')
        print('TRY AGAIN?')



