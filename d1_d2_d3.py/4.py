print("Welcome to the love calculator")
name_1 = input("What is your name ? \n")
name_2 = input("WHat is their name ? \n")
combined_string = name_1 + name_2
lower_case_string = combined_string.lower()
T = lower_case_string.count("t")
R = lower_case_string.count("r")
U = lower_case_string.count("u")
E = lower_case_string.count("e")
true = T + R + U + E
L = lower_case_string.count("l")
O = lower_case_string.count("o")
V = lower_case_string.count("v")
E = lower_case_string.count("e")
love = L + O + V + E
love_score =int(str(true) + str(love))
if (love_score <= 10) or (love_score >= 90):
    print(f"Yor love score is {love_score}, you go together like coke and mentos.")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Yore love score is {love_score}, You are all right together")
else:
    print(f"Your score is {love_score}")
