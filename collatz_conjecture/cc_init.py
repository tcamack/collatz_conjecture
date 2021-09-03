#MAIN

import os
import sys
import cc_ns
import cc_rs

invalid_selection = False
invalid_restart = False

def clear(): #CLEAR FUNCTION
    os.system("cls")

def main(): #FUNCTION TO SELECT TEST
    global invalid_selection

    print("Collatz Conjecture")
    print("")
    print("Please choose from the options below:")
    print("")
    print("1: Numerical Solver")
    print("For this solver you choose a specific number to test")
    print("")
    print("2: Randomized Solver")
    print("For this solver you choose how many tests to run with a random number from 1 to googol")
    print("")
    if invalid_selection == True:
        print("INVALID INPUT DETECTED - PLEASE ENTER A NUMBER THAT MATCHES AN OPTION")
    elif invalid_selection == False:
        print("Enter the number of the option you would like:")
    
    str_selection = str(input())

    if str_selection.isnumeric():
        selection = int(str_selection)

        if selection == 1:
            invalid_selection = False #invalid_selection IS SET TO FALSE AFTER A CORRECT INPUT FOR CONTINUITY, IT'S NOT ACTUALLY NEEDED FOR FUNCTIONALITY
            clear()
            cc_ns.ns_launch()
        elif selection == 2:
            invalid_selection = False #invalid_selection IS SET TO FALSE AFTER A CORRECT INPUT FOR CONTINUITY, IT'S NOT ACTUALLY NEEDED FOR FUNCTIONALITY
            clear()
            cc_rs.rs_launch()
        else:
            invalid_selection = True
            clear()
            main()
    else:
        invalid_selection = True
        clear()
        main()

def cc_restart():
    global invalid_restart

    print("Would you like to restart the program?")
    if invalid_restart == True:
        print("")
        print("Please enter 'yes' or 'no'")
    
    str_restart = str(input()).lower()

    if str_restart == "yes":
        invalid_restart = False
        clear()
        main()
    elif str_restart == "no":
        return
    else: #ERROR MESSAGE IF INPUT NOT RECOGNIZED
        invalid_restart = True
        clear()
        print("ERROR: INPUT NOT RECOGNIZED")
        print("")
        cc_restart()