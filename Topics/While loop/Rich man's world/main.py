deposit = int(input())
return_limit = 700000
interest_rate = 7.1
years = 0

while deposit < return_limit:
    deposit = deposit + deposit * (interest_rate / 100)
    years += 1
if deposit > return_limit:
    print(years)
