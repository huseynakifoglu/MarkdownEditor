x = int(input())
y = int(input())
result = 0


if (x == 1 and y == 1) or (x == 8 and y == 8):
    result = 3
elif (x == 1 and y == 8) or (x == 8 and y == 1):
    result = 3
elif (x != 1 or x != 8) and y in (1, 8):
    result = 5
elif (y != 1 or y != 8) and x in (1, 8):
    result = 5
else:
    result = 8
print(result)
