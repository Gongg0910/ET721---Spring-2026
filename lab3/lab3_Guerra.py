"""

Gonzalo Guerra
Feb 3,2026
Lab 3, conditional statement and loop is python

"""
print("\n----- example 1: set-up of condiitonal statement -----")
#conditional statement state s the flow the program

age = 4
if(age >= 21 and age <= 100):
    print("You are an adult")
elif(age < 21 and age >= 12):
    print("You are a teen")
elif(age < 12 and age > 0):
    print("You are a kid")
else:
    print("Unable to read age")

print("\n----- exampe 2: for loop -----")
# for loop as a counter to print from 9 to 1, step 1
for n in range(9, 0, -1):
    print(n)

# for loop in a list
print("\n----- exampe 3: for loop in a list -----")
numbers = [3,6,1,-8,9,-5]
count_negative = 0
for m in numbers:
    if m < 0:
        count_negative += 1
else:
    print(f"There is/are {count_negative} negative numbers")
# for-else, the else statement will run only after the completion of all iteration in the for loop
print('\nEND OF PROGRAM')


print("\n----- example 4: while loop as a coutner -----")
# while loop to print from -3 to 5, inclusive, step of 2, output --> -3 -1 1 3 5
x = -3 
while x <= 5:
    print(x)
    x += 2

print("\n----- example 5: while loop to validate an input -----")
# program collect a number from the user and print if the number is even or odd
# after it, the program will ask the use if another number will be tested
# if te user type 'y' or 'Y' the then program will run again
# if the user types any other characters that is not 'y' or 'Y', the program will stop

decision_user = 'y'
user_number = 0

while True:
    user_number = int(input("Enter a number between 1 and 9: "))
    
    while True:   # You mean this one for exercise one?
        if(user_number > 0 and user_number < 10):
            print("Number you enter is between 1 and 9")
            break
        else:
            print("Number you enter is not between 1 and 9")
            break
    if user_number%2 == 0 and user_number != 0:
        print(f"{user_number} is EVEN")
    elif user_number == 0:
        print("The number is zero")
    else:
        print(f"{user_number} is ODD")

    decision_user = input("\nDo you want another run? y or Y for yes | n or N for no: ")
    if decision_user == 'y' and decision_user == 'Y':
        break
    elif decision_user == 'n' and decision_user == 'N':
        break


print("\n----- EXERCISE 1: validate a number between 1 and 9 -----")


print("\n----- EXERCISE 2: guess a number with 3 attempts -----")

# number = 3
# attempt = 3
# while True:
#     print(f"You have {attempt} attempts!\n")
#     user_input = int(input("Enter a number to guess: "))
#     if(number == user_input):
#         print(f"You guess the right number! {number}\n") 
#         break
#     elif(number != user_input):
#         attempt -= 1
#         print(f"The number you enter '{user_input}' is wrong\n")
#         if(attempt == 0):
#             break

        
        




    
