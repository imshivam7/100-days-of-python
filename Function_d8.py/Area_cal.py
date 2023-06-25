# We have used import math function to round the number > used math.ceil function.

import math

def paint_calc(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    
    print(f"You will need {no_of_cans} to paint the wall ")
    


test_h = int(input("Height of wall:  "))
test_w = int(input("Width of wall:  "))

coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)