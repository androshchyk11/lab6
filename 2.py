import enum


class converter(enum.Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('amount of money:'))
            break
        except ValueError as e:
            print(e)
    p = converter[input('currency:')]
    if p == converter.USD:
        print("in usd = ", x / 24.57)
    elif p == converter.EUR:
        print("in eur = ", x / 26.9)
    elif p == converter.CZK:
        print("in czk = ", x / 1.08)
    elif p == converter.PLN:
        print("in pol=", x / 6.31)
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
