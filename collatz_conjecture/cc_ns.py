#COLLATZ CONJECTURE NUMERICAL SOLVER

import random
import os
import os.path


from os import path

baseNum = 0
m_list = []
m_str = ""
log_enabled = False
invalid_number = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def space(): #FUNCTION TO SAVE LINES
    print("")
    print("------------------------------------------------------------------------------------------")
    print("")

def ns_launch(): #includes checking for integer
    global baseNum
    global invalid_number

    print("Collatz Conjecture Solver")
    print("")
    if invalid_number == True:
        print("INVALID INPUT DETECTED")
        print("")
    print("Enter value to test:")
    str_baseNum = str(input())

    if str_baseNum.isnumeric():
        invalid_number = False
        baseNum = int(str_baseNum)
        logging()
    else:
        invalid_number = True
        clear()
        ns_launch()

def logging(): #OPTION TO ENABLE LOGGING
    global log_enabled

    print("")
    print("Would you like to log the test in an external file?")
    m_log = str(input()).lower()
    if m_log == "yes":
        log_enabled = True
        space()
        collatz()
    elif m_log == "no":
        log_enabled = False
        space()
        collatz()
    else: #ERROR MESSAGE IF INPUT NOT RECOGNIZED
        clear()
        print("")
        print("ERROR: INPUT NOT RECOGNIZED")
        print("")
        print("Please enter 'yes' or 'no' as a selection")
        print("")
        logging()

def output(): #OUTPUT IF LOGGING IS ENABLED
    global m_str

    m_str = "\n".join(str(z) for z in m_list)

    if path.exists("01_int_results.txt"):
        os.remove("01_int_results.txt")
        f = open("01_int_results.txt","w+")
    else:
        f = open("01_int_results.txt","w+")

    f.write("BASE: " + str(baseNum))
    f.write("\n" + m_str)

    f.close()

def collatz(): #MAIN MATHS
    global tCount
    global m_list

    i = baseNum
    cycle = 0
    max = baseNum

    while i != 1:
        cycle += 1

        if i > max:
            max = i
        if (i % 2) == 0: #DIVIDED BY TWO IF EVEN
            i = i // 2
            if log_enabled == True:
                str_cycle = str(cycle)
                str_cycle_zfill = str_cycle.zfill(4)
                m_list.append(str_cycle_zfill + ": "  + str(i))
        else: #MULTIPLIED BY THREE PLUS ONE IF ODD
            i = (3 * i) + 1
            if log_enabled == True:
                str_cycle = str(cycle)
                str_cycle_zfill = str_cycle.zfill(4)
                m_list.append(str_cycle_zfill + ": "  + str(i))

    clear()
    print("RESULTS")
    print("")
    print("Base Value:")
    print(baseNum)
    print("")
    print("Cycles:")
    print(int(cycle))
    print("")
    print("Largest value derived from base value:")
    print(int(max))
    print("")

    if log_enabled == True: #LOG DATA IF LOGGING IS ENABLED
        output()

    input("Press Enter to continue...") #CLOSE FILE AFTER HITTING ENTER KEY
    clear()
    import cc_init
    cc_init.cc_restart()