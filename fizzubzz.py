#!/usr/bin/env python3

x = 0
num = 19

def input(num):
    while x <= num:
        if x%3 == 0 and x%5 == 0:
            print(FizzBuzz)
        if x%3 == 0:
            print(Fizz)
        if x%5 == 0:
            print(Buzz) 
        else:
            print(x)
        x += 1


