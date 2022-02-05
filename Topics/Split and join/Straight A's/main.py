# put your python code here

grades = input().split()
# print(grades)
# print("A count: " + str(grades.count('A')))
# print("Number of elements: " + str(len(grades)))
print(round(grades.count('A') / len(grades), 2))
