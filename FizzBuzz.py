#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = "FizzBuzz"
print text.lower()


while True:
    n = raw_input("Please enter a number between 1 and 100: ")

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

    except Exception as e:
            print "Please enter a number!"

    new_enter = raw_input("Would you like to enter another number? (y/n): ")

    if new_enter == "y" or "yes:
        continue
    elif new_enter == "n" or "no:
        break




