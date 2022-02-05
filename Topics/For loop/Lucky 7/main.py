n = int(input())
divisible = []
for _ in range(n):
    num = int(input())
    if not num % 7:
        divisible.append(num)

for i, _ in enumerate(divisible):
    print(divisible[i] * divisible[i])
