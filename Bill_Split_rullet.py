import random

name_string = input("Give me everybody's name saperated by comma. \n")

names = name_string.split(",")

name_items = len(names)

random_choice = random.randint(0, name_items -1)

print(random_choice)

person_who_pay_the_bill = names[random_choice]

print(person_who_pay_the_bill + " is going to buy the meal today")



count = [1 2 3 4 5 6 7 8 9 ]

print(count)