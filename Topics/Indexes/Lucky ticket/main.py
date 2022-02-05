# Save the input in this variable
ticket = list(input())
# print(ticket)

for i in range(0, len(ticket)):
    ticket[i] = int(ticket[i])

# Add up the digits for each half
half1 = sum(ticket[:3])
half2 = sum(ticket[-3:])
# print(half1)
# print(half2)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")