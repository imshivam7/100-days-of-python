alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")

text = input("Type your message\n").lower()

shift = int(input("Type the shift number: \n"))

#Create a function called encrypt that takes the text and shift as inputs 

        # inside the encrypt function shift each letter of the text forward in the alphabets by the shift amount and print the encrypted text 
        
def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cypher_text += new_letter
        
    print(f"The encoded message is {cypher_text}")    
    
    
    
def decrypt(cypher_text, shift_amount):
    for letter in cypher_text:
        plain_text = ""
        position = alphabet.index(letter)
        new_position = cypher_text - shift_amount
        plain_text = alphabet[new_position]
    print(f"The decoded text is {plain_text}")    
    
        
    
    # Call the encrypt function and pass the user text.




if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cypher_text=text, shift_amount=shift)




def caser(start_text, shift_amount, cypher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cypher_direction == "decode":
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cypher_direction}d text is {end_text}")        

    