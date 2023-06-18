# import random

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")
fruits = ["Apple", "Banana", "Cherry"]

#Above cose is for lists and list always starts with [] and to hilight/print any data from the list we can start counting from 0 it will start counting from the very begning however if we have to count from the end we can start with [-1]
fruits[0] = "Appppppllllleeee"

# If we want to alter any data from the list the wen can extrat and alter using above code

fruits.append("Kiwi")

#The above code .append() is to add any new item to the list.

fruits.extend(["Grapes", "Papaya", "Lichi"])

# we can use extend function for extending the list items. generaly used when multiple items to be added to the list



print(fruits)