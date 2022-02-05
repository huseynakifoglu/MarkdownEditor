user_input = input().split()

if len(user_input) == 1:
    print(user_input[0].lower())
else:
    output = user_input[0].lower()
    for index in range(1, len(user_input)):
        user_input[index] = user_input[index].capitalize()
        output += user_input[index]
    print(output)
