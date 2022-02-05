# put your python code here
nums = []
num_sum = None


def calculate_sum(num_list):
    return sum(num_list)


def squarer(x):
    return x * x


def print_zero():
    return 0


def sum_squares(u_list):
    for i, value in enumerate(u_list):
        u_list[i] = squarer(value)
    return sum(u_list)


while num_sum != 0:
    u_input = int(input())
    nums.append(u_input)
    if nums[0] == 0:
        print(print_zero())
    else:
        pass
    num_sum = calculate_sum(nums)


if nums[0] != 0:
    print(sum_squares(nums), end="")
