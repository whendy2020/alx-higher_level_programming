#!/usr/bin/python3

def fizzbuzz():

    for num in range(1, 101):
        result = ""
        if num % 3 == 0:
            result = "Fizz"
        if num % 5 == 0:
            result = "Buzz"
        if num % 15 == 0:
            result = "FizzBuzz"
        if num % 5 != 0 and num % 3 != 0:
            result = result + str(num)
        print(result, "", end="")
