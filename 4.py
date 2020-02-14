while True:
    while True:
        try:
            t = float(input("Input t:"))
            if (t > 0):
                break
            else:
                print("t shold be more that 0!")
        except ValueError as e:
            print(e)
    minutes = t % 6
    if (minutes == 0):
        print("Changing light from red to green")
    elif minutes < 3:
        print("Green light is shining!")
    elif minutes == 3:
        print("Changing light from green to yellow")
    elif minutes > 3 and minutes < 5:
        print("Yellow light is shining!")
    elif minutes == 5:
        print("Changing light from yellow to red!")
    elif minutes > 5:
        print("Red light is shining!")
    while True:
        try:
            print("if you want to check again press - 1, if you want to stop press - 2")
            flag = int(input())
            if flag != 1 and flag != 2:
                print("press 1 or 2!!!")
            else:
                break
        except ValueError as e:
            print(e)
    if flag == 1:
        continue
    else:
        break