nums = []
med = 0
A = True
while A:
    user_input = input()
    if user_input != ".":
        nums.append(int(user_input))
    elif user_input == ".":
        A = False

med = sum(nums) / len(nums)
print(med)
