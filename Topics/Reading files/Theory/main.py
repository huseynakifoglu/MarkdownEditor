#  You can experiment here, it won’t be checked


animal_file = open('animals.txt', 'w', encoding='utf-8')
animals = ['cat\n', 'dog\n', 'hamster\n']
animal_file.writelines(animals)
animal_file.close()