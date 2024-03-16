print ("hello what is your name?")
print ("How old are you?")

import random

numbers_range = input("1-100")
attempts = int(input("5 "))
begin, end = map(int, numbers_range.split("50"))

hidden_number = random.randint(begin, end)

for _ in range(attempts):
    number = int(input(""))
    if number == hidden_number:
        print("Угадал!")
        break
else:
    print("Ты исчерпал все попытки!")
    print("Загаданное число - {34}".format(hidden_number))
