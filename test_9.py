def how_month(month):
    if month == 2:
        return 31
    elif month == 3:
        return 28 + how_month(month-1)
    elif month == 4:
        return 31 + how_month(month - 1)
    elif month == 5:
        return 30 + how_month(month - 1)
    elif month == 6:
        return 31 + how_month(month - 1)
    elif month == 7:
        return 30 + how_month(month - 1)
    elif month == 8:
        return 31 + how_month(month - 1)
    elif month == 9:
        return 31 + how_month(month - 1)
    elif month == 10:
        return 30 + how_month(month - 1)
    elif month == 11:
        return 31 + how_month(month - 1)
    elif month == 12:
        return 30 + how_month(month - 1)

def time(text):
    data, time = text.split(" ")
    month, day, year = map(int,data.split("/"))
    hour, minute, second = map(int,time.split(":"))
    if month == 1:
        return second + minute*60 + hour*60*60 + (day-1)*24*60*60
    else:
        return second + minute * 60 + hour * 60 * 60 + (day - 1) * 24 * 60 * 60 + how_month(month)*24*60*60

text = input()
print(time(text))