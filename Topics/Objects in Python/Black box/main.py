# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3, 4, 5]

new_list = blackbox(my_list)

if id(my_list) == id(new_list):
    print("same")
else:
    print("new")
