row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) #2
Vertical = int(position[1]) #3

# We are using Vertical -1 because if user will enter 23 and program starts count with 0 so we are substracting -1 the input no.

selected_row = map[Vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
