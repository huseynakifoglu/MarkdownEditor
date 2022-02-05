# first lets take inputs from user
number_of_halls = int(input())
capacity = int(input())
num_of_viewers = int(input())


# check if number of viewers is less than capacity multiplied number of halls


def check_capacity(viewers, halls, a_capacity):
    if viewers <= halls * a_capacity:
        print("True")
    else:
        print("False")


check_capacity(num_of_viewers, number_of_halls, capacity)
