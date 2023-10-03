#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    
    print("Happy New Year!")

# Call the function
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_list = [x ** 2 for x in int_list]
    return squared_list

""" # Test run
integers = [1, 2, 3, 4, 5]
squared_integers = square_integers(integers)
print(squared_integers)  # Output: [1, 4, 9, 16, 25]
 """

def fizzbuzz():
    # code goes here!:
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function for the print FizzBuzz sequence
fizzbuzz()

