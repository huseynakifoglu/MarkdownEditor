# put your python code here
num_list = []
while True:
    num = int(input())
    if num < 10:
        continue
    if 10 <= num <= 100:
        num_list.append(num)
        continue
    elif num > 100:
        break
# print(num_list)
for nums in num_list:
    print(nums)