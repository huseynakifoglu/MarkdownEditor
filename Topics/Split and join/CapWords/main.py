u_input = input().split("_")
# print(u_input)
for _ in range(len(u_input)):
    u_input[_] = u_input[_].lower()
    u_input[_] = u_input[_].capitalize()
result = "".join(u_input)
print(result)
