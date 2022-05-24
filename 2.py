
import random

rand_number = random.randint(1, 100)
x = input()
while x != rand_number:
    print('try once again')
    break
if x == rand_number:
    print('YOU WIN!')
