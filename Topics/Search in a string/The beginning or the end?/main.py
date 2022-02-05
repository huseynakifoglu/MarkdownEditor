text = input()

first = text.find("old")
second = text.rfind("old")

# this is ternary operator that shortens if else statement
print(first if first > second else second)
