

#Add
def add(n1 , n2):
    return n1 + n2

#substract

def substract(n1 , n2):
    return n1 - n2

#multiply

def multiply(n1 , n2):
    return n1 * n2

#divide
def divide(n1 , n2):
    return n1 / n2
Operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():

    num1 = float(input("What's the first number:   "))

    for symbol in Operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
            

        operation_symbol = input("pick an operation :   " )
        num2 = float(input("What's the next number:   "))
        calculation_function = Operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # operation_symbol = input("Pick another operation:   ")
        # num3 = int(input("What's the next number:   "))
        # calculation_function = Operations[operation_symbol]
        # second_answer = calculation_function(first_answer, num2)

        # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        
        if input(f"Type 'y' to start calculation with the prevoius {answer} or type 'n' to start a new calculation:  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()
