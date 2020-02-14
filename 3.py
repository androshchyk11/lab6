import enum


class month(enum.Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class season(enum.Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


while True:
    s = month[input('month:')]
    if s == month.January or s == month.February or s == month.December:
        print(season.Winter.name)
    elif s == month.March or s == month.April or s == month.May:
        print(season.Spring.name)
    elif s == month.June or s == month.July or s == month.August:
        print(season.Summer.name)
    elif s == month.September or s == month.October or s == month.November:
        print(season.Autumn.name)
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