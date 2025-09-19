# This is about to calculate the typing speed a person

from time import *
import random as r

def mistake(partest, usertest):

    error = 0

    for i in range (len(partest)):

        try:
            if partest[i] != usertest[i]:

                error += 1
        except:
            error += 1

    return error

def speed_time (time_s, time_e, userinput):

    time_delay = time_e - time_s
    time_ro = round(time_delay, 2)

    speed = (len(userinput))/time_ro

    return round(speed,2)

    


test = ["A paragrapgh is a self-contained unit of discourse in wirint.",
        "My name is muhammad Abdullah.",
        "Welcome to this typing apeed challenge."
        ]

test1 = r.choice(test)

print("********** Typing Speed Challeng **********")
print()
print(test1)
print()
print()

time1 = time()
test_input = input("Enter :  ")
time2 = time()

print()
print(f"Speed: {speed_time(time1,time2,test_input)} words per second" )
print()
print(f"Error: {mistake(test1,test_input)} errors")