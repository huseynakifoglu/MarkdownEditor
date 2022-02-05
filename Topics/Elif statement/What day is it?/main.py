offset = input()
weekdays = ["Monday", "Tuesday", "Wednesday"]
if int(offset) == 0 or 13 >= int(offset) > -11:
    print(weekdays[1])
elif int(offset) == 14:
    print(weekdays[2])
elif int(offset) <= -11:
    print(weekdays[0])
