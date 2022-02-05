# read sample.txt and print the number of lines
number_of_lines = 0
with open("sample.txt", "r") as my_file:
    for _ in my_file:
        number_of_lines += 1

print(number_of_lines)