#!/usr/bin/env python
#-*- coding: utf-8 -*-

km = 0
miles = 0


print("Hello. You can convert km to miles here :)")

while True:
    km = raw_input("Please enter km: ")

    try:
        km = float(km.replace(",", "."))

        conv_fac = 0.621371
        miles = km * conv_fac

        print " {0} kilometers is {1} miles." .format(km, miles)

    except Exception as e:
        print "Please enter only a number!"

    new_enter = raw_input("Would you like to enter another conversion? (Y/N): ")

    if new_enter.upper() != "Y" and new_enter.upper() != "YES":
        break













