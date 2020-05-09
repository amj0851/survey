dictList=[]
x = 0
import time
while x == 0:
    print("welcome to the survey. if you want to stop survey type 'stop' at anytime.")
    a = input ("How old are you?????")
    while True:
        if a.isdigit():
            print(a)
            break
        elif a == "stop":
            x = 1
        else:
            print("Please enter a number /:")
            a = input ("How old are you?????")
    b = input ("Do you live in the United States of America????")
    placelist= ["yes", "no"]
    while True:
        if b in placelist:
            print (b)
            break
        elif b == "stop":
            x = 1
        else:
            print("Choose an actual answer :/")
            b = input ("Do you live in the United States of America????")
    c = input ("Do you have a pet???")
    petlist = ["yes", "no"]
    while True:
        if c in petlist:
            print (c)
            break
        elif c == "stop":
            x = 1
        else:
            print("Choose an actual answer :/")
            c = input ("Do you have a pet???")
    d = input ("How many people are in your family??")
    while True:
        if d.isdigit():
            print(d)
            break
        elif d == "stop":
            x = 1
        else:
            print("Please enter a number /:")
            d = input ("How many people are in your family??")

    e = input ("Is the sky blue?")
    skylist = ["yes", "no"]
    while True:
        if e in skylist:
            print (e)
            break
        elif e == "stop":
            x = 1
        else:
            print("Choose an actual answer :/")
            e = input ("Is the sky blue?")
    print("The survey will start over in 3 seconds, thank you for your time.")
    question = {
        'age' : a,
        'place' : b,
        'pet' : c,
        'family' : d,
        'sky' : e,
        }
    dictList.append(question)
    time.sleep(3)
    print (dictList)
