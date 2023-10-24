def time(text):
    data, time = text.split(" ")
    month, day, year = data.split("/")
    hour, minute, second = time.split(":")
    time_of_day = "AM"
    year = year[2:4]
    if int(month) > 12 or int(day) > 31 or int(hour) > 23 or int(minute) > 59 or int(second) > 59:
        print("Неверные данные")
    else:
        if int(hour) > 12:
            hour = int(hour) - 12
            time_of_day = "PM"
            return(day + "." + month + "." + year + " " + str(hour) + ":" + minute + ":" + second + " " + time_of_day)

text = input()
print(time(text))
