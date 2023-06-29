alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# Create a function called encrypt that takes the text and shift as inputs 

# inside the encrypt function shift each letter of the text forward in the alphabets by the shift amount and print the encrypted text 
        
# def encrypt(plain_text, shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
        
#     print(f"The encoded message is {cypher_text}")    
    
    
    
# def decrypt(cypher_text, shift_amount):
#     for letter in cypher_text:
#         plain_text = ""
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text = alphabet[new_position]
#     #print(f"The decoded text is {plain_text}")    
    
        
    
#     # Call the encrypt function and pass the user text.




# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cypher_text=text, shift_amount=shift)


def caser(start_text, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        # below syntax is for keeping character at their place aprt from alphabets.
        
        if char in alphabet:
            
            position = alphabet.index(char)
       
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
                
    print(f"The {cypher_direction}d text is {end_text}") 

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")

    text = input("Type your message\n").lower()

    shift = int(input("Type the shift number: \n"))

    shift = shift % 26
        
    caser(start_text=text, shift_amount=shift, cypher_direction=direction)
      
    result = input("Type 'yes' if you want to go again, otherwie type 'No'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!!")