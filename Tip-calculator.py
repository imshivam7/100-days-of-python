print("Welcome to the tip calculatror.")
bill=float(input("What was the total bill?" ))
tip=int(input("what percentage of tip would you like to give? 10, 12, or 15?"))
people=int(input("How many people to split the bill"))
total_bill = tip / 100 * bill + bill
bill_per_person=(total_bill / people)
final_amount=round(bill_per_person, 2)
print(f"Each person should pay {final_amount}")