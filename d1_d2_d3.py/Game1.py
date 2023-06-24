print('''              _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
''')
# Used above image from ascii.co.uk/art
print("Welcome to treasure Island\n")
print("Your mission is to find tresure\n")

choice1 = input(' you\'re Please choose which direction to go? Type "Left" or "Right" .\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to the lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n').lower()
    #Player can continue the game.
    if choice2 == "wait":
        choice3 = input('You\'ve arrived at the island unharmed. There is a house with three doors one red, one yellow and one blue. Which colur do you choose? \n').lower()
        if choice3 == "red":
            print("YOu are in the room of fire.Game Over!")
            
        elif choice3 == "yellow":
            print("Congratulations! You have won the game.")
            
        elif choice3 == "blue":
            print("its a room full of scorpions. Game Over!")
        else:                   
            print("You chose the door that does not exist. Game Over!")
        #Game will continue
    else:
        print("You are chased by an allegator. Game Over!!!")
else:
    print("You are etten by an allegator. Game Over!!!")  
    


