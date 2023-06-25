

def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        #print (x)
        if number % x == 0:
            is_prime = False
            #break
    if is_prime:
        print("Its a prime number. ")
    else:
        print("It is not a prime number. ")    
                



n = int(input("Check this number: "))
prime_checker(number=n)