def calculate(amount, interest_rate, time):
    # your code here
    result = float(amount * interest_rate * time) / 100
    total_amount = amount + result
    return result, total_amount


def print_result(interest, total_amount):
    # your code here
    print("The interest is: " + str(float(interest)))
    print("The total amount is: " + str(float(total_amount)))


# calculate(1000, 8, 5)
# print_result(400, 1400)
