# animal_list = [["chicken", "23"], ["goat", "678"], ["pig", "1296"], ["cow", "3848"], ["sheep", "6769"]]
animals = [[" chicken", " chickens", 23], [" goat", " goat", 678],
           [" pig", " pigs", 1296], [" cow", " cows", 3848],
           [" sheep", " sheep", 6769]]

users_money = int(input())
if users_money >= animals[4][2]:
    result = users_money // animals[4][2]
    if result > 1:
        print(str(result) + animals[4][1])
    else:
        print(str(result) + animals[4][0])

elif users_money >= animals[3][2]:
    result = users_money // animals[3][2]
    if result > 1:
        print(str(result) + animals[3][1])
    else:
        print(str(result) + animals[3][0])

elif users_money >= animals[2][2]:
    result = users_money // animals[2][2]
    if result > 1:
        print(str(result) + animals[2][1])
    else:
        print(str(result) + animals[2][0])

elif users_money >= animals[1][2]:
    result = users_money // animals[1][2]
    if result > 1:
        print(str(result) + animals[1][1])
    else:
        print(str(result) + animals[1][0])

elif users_money >= animals[0][2]:
    result = users_money // animals[0][2]
    if result > 1:
        print(str(result) + animals[0][1])
    else:
        print(str(result) + animals[0][0])
else:
    print("None")
