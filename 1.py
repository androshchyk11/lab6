days = range(1, 32)
mounths = range(1, 13)
years = range(1901, 2020)

while True:
    while True:
        try:
            d = int(input("day: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            m = int(input("month: "))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            y = int(input("year: "))
            break
        except ValueError as e:
            print(e)

    if (d in days and m in mounths and y in years):
        if y % 4 == 0:
            if (m == 2):
                if (d == 29):
                    print(f"1.03.{y}")
                    print(f"{d-1}.{m}.{y}")
                elif (d > 29):
                    print("wrong data!!!")
                elif (d == 1):
                    print(f"31.{m-1}.{y}")
                    print(f"{d+1}.{m}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
                    print(f"{d-1}.{m}.{y}")
            if (m == 3 or m == 5 or m == 7 or m == 8 or m == 10):
                if (d == 31):
                    print(f"{d-1}.{m}.{y}")
                    print(f"1.{m+1}.{y}")
                elif (d == 1):
                    print(f"{d+1}.{m}.{y}")
                    print(f"30.{m-1}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
                    print(f"{d-1}.{m}.{y}")
            if (m == 1):
                if (d == 1):
                    print(f"31.12.{y-1}")
                    print(f"{d+1}.{m+1}.{y+1}")
                elif (d == 31):
                    print(f"{d-1}.{m}.{y}")
                    print(f"1.{m+1}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
                    print(f"{d-1}.{m}.{y}")
            elif (m == 12):
                if (d == 31):
                    print(f"1.01.{y+1}")
                    print(f"{d-1}.{m}.{y}")
                elif (d == 1):
                    print(f"{d+1}.{m}.{y}")
                    print(f"{30}.{m-1}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
                    print(f"{d-1}.{m}.{y}")
            elif (m == 4 or m == 6 or m == 9 or m == 11):
                if (d == 30):
                    print(f"1.{m+1}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
        else:
            if (m == 2):
                if (d == 28):
                    print(f"1.03.{y}")
                    print(f"{d-1}.{m}.{y}")
                elif (d > 28):
                    print("wrong data!!!")
                elif d == 1:
                    print(f"{d+1}.{m}.{y}")
                    print(f"31.{m-1}.{y}")
                else:
                    print(f"{d+1}.{m}.{y}")
                    print(f"{d-1}.{m}.{y}")
            if (m == 3 or m == 5 or m == 7 or m == 8 or m == 10):
                if (d == 31):
                    print(f"1.{m+1}.{y}")
                    print(f"{d-1}.{m}.{y}")
                elif d==1:
                    print(f"{d+1}.{m}.{y}")
                    print(f"30.{m}.{y}")
                else:
                    print(f"{d-1}.{m}.{y}")
                    print(f"{d+1}.{m}.{y}")
            elif m==1:
                if (d == 31):
                    print(f"1.{m+1}.{y}")
                    print(f"{d-1}.{m}.{y}")
                elif d==1:
                    print(f"{d+1}.{m}.{y}")
                    print(f"31.12.{y-1}")
                else:
                    print(f"{d-1}.{m}.{y}")
                    print(f"{d+1}.{m}.{y}")
            elif (m == 12):
                if (d == 31):
                    print(f"1.01.{y+1}")
                    print(f"{d-1}.{m}.{y}")
                elif d==1:
                    print(f"{d+1}.{m}.{y}")
                    print(f"30.{m-1}.{y}")
            elif (m == 4 or m == 6 or m == 9 or m == 111):
                if (d == 30):
                    print(f"1.{m+1}.{y}")
                    print(f"{d-1}.{m}.{y}")
                elif d==1:
                    print(f"{d+1}.{m}.{y}")
                    print(f"31.{m}.{y}")
                else:
                    print(f"{d-1}.{m}.{y}")
                    print(f"{d+1}.{m}.{y}")
    else:
        print("wrong data!")
    while True:
        try:
            print("if you want to check again press - 1, if you want to stop press - 2")
            flag = input()
            if flag != '1' and flag != '2':
                print("press 1 or 2!!!")
            else:
                break
    if flag == 1:
        continue
    else:
        break
