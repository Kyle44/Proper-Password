# File:         lab6.py
# Written by:   Kyle Fritz
# Date:         October 8, 2013
# Section:      10
# Email:        fritzk1@umbc.edu
# Description:  lab 6, Validation
############### USE WITH PYTHON 3 ###########
### scl enable python33 bash


def main():
    flag = True
    passw = (input("Please enter a password that is at least 5 characters in length, at least one is a number, and mustn't include '.' , '!' , '?': "))
    

    numbers = "0123456789"
    q = "?"
    e = "!"
    period = '.'
    while(flag):    
        if period in passw:
            print("Error: Password can't contain '.'")
        if len(passw) < len("hello"):
            print("Error: Must be 5 or more characters")
        if q in passw:
            print("Error: password can't contain '?'")
        if e in passw:
            print("Error: password can't contain '!'")
#        if numbers not in passw:
 #           print("Error: password must contain at least 1 number")

        if period in passw or q in passw or e in passw or len(passw) < len("hello"):
            passw = input("Please try again: ")
        else:
            flag = False
            print("Your password is", passw)
main()
