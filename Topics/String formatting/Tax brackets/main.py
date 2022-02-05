income = int(input())
percent = 0


def calculate_tax(var, procent):
    calculated_tax = round(var * (procent / 100))
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
    return calculated_tax


if income <= 15527:
    calculate_tax(income, percent)

elif 15528 <= income <= 42707:
    percent = 15
    calculate_tax(income, percent)
elif 42708 <= income <= 132406:

    percent = 25
    calculate_tax(income, percent)
else:
    percent = 28
    calculate_tax(income, percent)
