# read sums.txt
with open("sums.txt", "r") as my_file:
    for line in my_file:
        nums = line.split()
        print(int(nums[0]) + int(nums[1]))
