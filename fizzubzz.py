#!/usr/bin/env python3

x = 0

num = 19

#def input(num):
for i in range(1,20):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0: 
        print('Fizz')
    elif i%5 == 0:
        print('Buzz') 
    else:   
        print(i)


