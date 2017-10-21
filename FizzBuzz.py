#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = "FizzBuzz"
print text.lower()


while True:
    n = raw_input("Please enter the number between 1 and 100: ")

    try:
        n = int(n)
        for n in range(1, n + 1):
            if n % 3 == 0 and n % 5 == 0:
                print ("fizzbuzz")
            elif n % 3 == 0:
                print ("fizz")
            elif n % 5 == 0:
                print("buzz")
            else:
                print (n)
            n = n + 1

    except Exception as e:
            print "Please enter only a number!"

    new_enter = raw_input("Would you like to enter another number? (y/n): ")

    if new_enter == "y":
        continue
    elif new_enter == "n":
        break




