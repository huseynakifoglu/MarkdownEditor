text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

length = int(input())

new_list = []

for i in text:
    for j in i:
        if len(j) <= length:
            new_list.append(j)

print(new_list)
