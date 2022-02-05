# work with these variables
eugene = set(input().split())
rose = set(input().split())

print(eugene.union(rose) - eugene.intersection(rose))
