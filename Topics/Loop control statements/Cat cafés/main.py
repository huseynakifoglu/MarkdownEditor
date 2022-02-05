names = []
nums = []

while True:
    u_input = input()
    if u_input == "MEOW":
        break
    cafe, cats = u_input.split()
    names.append(cafe)
    nums.append(int(cats))
# finding max num in the list
max_num = max(nums)

# finding the index of max num in the list and getting the same index of cafe name
result = names[nums.index(max_num)]
print(result)

# cafe, cats = input().split()
# print(cafe)
# print(cats)
