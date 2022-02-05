# read animals.txt
# and write animals_new.txt
with open('animals.txt', 'r', encoding='utf-8') as my_animals:
    list_animals = my_animals.readlines()
    # print(list_animals)

with open('animals_new.txt', 'w', encoding='utf-8') as new_animals:
    for animal in list_animals:
        new_animals.write(animal.replace('\n', ' '))
