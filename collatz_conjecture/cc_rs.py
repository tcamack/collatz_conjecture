#COLLATZ CONJECTURE RANDOMIZED SOLVER

import random
import os
import os.path

from os import path

tCount = 0
m_test = 0
m_baseNum = 0
m_max = 0
m_cycle = 0
m_list = []
log_enabled = False
invalid_number = False

def clear(): #CLEAR FUNCTION
    os.system("cls")

def space(): #FUNCTION TO SAVE LINES
    print("")
    print("------------------------------------------------------------------------------------------")
    print("")

def results(): #RESULTS PRINTED AFTER EVERY TEST IS FINISHED, SHOWS THE TEST WITH THE MOST CYCLES
    print("------------------------------------------------------------------------------------------")
    print("")
    print("RESULTS")
    print("")
    print("Test:")
    print(int(m_test))
    print("")
    print("Maximum cycles:")
    print(int(m_cycle))
    print("")
    print("Base value with maximum cycles:")
    print(float(m_baseNum))
    print("")
    print("Largest value derived from base value:")
    print(float(m_max))
    print("")

def rs_launch(): #INCLUDES INTEGER CHECK FOR NUMBER OF TESTS TO CONDUCT
    global tests
    global invalid_number

    print("Collatz Conjecture Random Value Solver")
    print("")
    print("LOGGING IS AVAILABLE WHEN CONDUCTING ONE TEST")
    print("")
    if invalid_number == True:
        print("INVALID INPUT DETECTED")
        print("")
    print("Enter desired tests:")
    str_tests = str(input())

    if str_tests.isnumeric(): 
        tests = int(str_tests)

        if tests == 1:
            invalid_number = False
            print("")
            logging()
        else:
            invalid_number = False
            print("")
            collatz()
    else:
        invalid_number = True
        clear()
        rs_launch()

def logging(): #OPTION TO ENABLE LOGGING TO EXTERNAL FILE, WILL ONLY DISPLAY IF CONDUCTING ONE TEST IN ORDER TO NOT DESTROY DRIVES
    global log_enabled

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
    else:
        clear()
        print("")
        print("ERROR: INPUT NOT RECOGNIZED")
        print("")
        print("Please enter 'yes' or 'no' as a selection")
        print("")
        logging()

def output(): #OUTPUT IF LOGGING IS ENABLED

    m_str = "\n".join(str(z) for z in m_list)

    if path.exists("02_rand_results.txt"):
        os.remove("02_rand_results.txt")
        f = open("02_rand_results.txt","w+")
    else:
        f = open("02_rand_results.txt","w+")

    f.write("BASE: " + str(m_baseNum))
    f.write("\n" + m_str)

    f.close()

def collatz(): #MAIN MATH
    global tCount
    global m_test
    global m_baseNum
    global m_max
    global m_cycle
    global m_list

    while tCount < tests:
        baseNum = random.randrange(1, 1.8 * (10 ** 300)) #RANDOM RANGE FROM 1 TO JUST SHY OF MAX FLOAT (JUST SHY TO ACCOUNT FOR NUMBER GETTING LARGER)
        i = baseNum
        max = baseNum
        cycle = 0
        tCount += 1

        while i != 1:
            cycle += 1

            if i > max:
                max = i
            if (i % 2) == 0:
                i = i // 2
                if log_enabled == True:
                    str_cycle = str(cycle)
                    str_cycle_zfill = str_cycle.zfill(4)
                    m_list.append(str_cycle_zfill + ": "  + str(i))
            else:
                i = (3 * i) + 1
                if log_enabled == True:
                    str_cycle = str(cycle)
                    str_cycle_zfill = str_cycle.zfill(4)
                    m_list.append(str_cycle_zfill + ": "  + str(i))

        if cycle > m_cycle:
            m_test = tCount
            m_baseNum = baseNum
            m_max = max
            m_cycle = cycle

        print("Test:           " + str(int(tCount)))
        print("Base Number:    " + str(float(baseNum)))
        print("Maximum Number: " + str(float(max)))
        print("Cycles:         " + str(int(cycle)))
        space()
    results()

    if log_enabled == True: #LOG DATA IF LOGGING IS ENABLED
        output()

    input("Press Enter to continue...") #CLOSE FILE AFTER HITTING ENTER KEY
    clear()
    import cc_start
    cc_start.cc_restart()