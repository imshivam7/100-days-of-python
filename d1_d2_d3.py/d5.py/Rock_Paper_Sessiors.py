import random

rock =  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock 1 for Paper and 2 for Scissors.\n "))

print(game_image[user_choice])

computer_choice = random.randint(0, 2)

print("computer chose")
print(game_image[computer_choice])

if user_choice > 2 and user_choice < 0: #this line will work as same mentioned on line 60 however getting this line on the top so copmuter will check this statement first to go ahead 
    print("You choose an invalid number you loose!!! try again")

elif user_choice == 0 and computer_choice == 2:
    print("You Win !!!")

elif computer_choice == 0 and user_choice == 2:
    print("You loose!!!")
    
elif computer_choice == user_choice:
    print("Its a draw")

elif computer_choice > user_choice:
    print("You Loose!!!")
    
elif user_choice > computer_choice:
    print("You Win!!!")   
    
#else:
  #print("You typed and invalid number you loose!!!")    