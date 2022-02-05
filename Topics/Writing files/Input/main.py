# write the code here
u_input = input()

file = open("input.txt", 'w', encoding='utf-8')
file.write(u_input)
file.close()