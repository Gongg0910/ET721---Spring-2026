"""
Gonzalo Guerra
Feb 5, 2026
Lab 5, function

"""
import math
from lab5_function_Guerra import *
from lab5_function_Guerra import generate_random, guessing_match

print("\n----- Example 1: user-defined function -----")
w = 8
length = 3
a = area_rectangle(w,length)
print_area_result(w,length,a)  


print("\n----- Example 2: calculate  -----")
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
# print(f"({x1}, {y1}) ({x2, y2})")

# testing 
# print(f"distance = {calculate_distance(x1, x2, y1, y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2, distance)






print("\n----- EXERCISE 2: -----")

while True:
    GUESS_NUMBER = int(input("Enter a number between 1 to 10: "))

    MIN_NUM = 1
    MAX_NUM = 10

    randoms = generate_random(MIN_NUM, MAX_NUM)

    if guessing_match(GUESS_NUMBER, randoms):
        break 

   





