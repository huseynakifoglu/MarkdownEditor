# write your code here
available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code",
                        "new-line", "ordered-list", "unordered-list"]
only_text_input = ["plain", "bold", "italic", "inline-code", "ordered-list", "unordered-list"]
special_commands = ["!help", "!done"]

global history
history = []


def ask_input():
    user_input = input("Choose a formatter: ")
    return user_input


def print_error():
    print("Unknown formatting type or command")


def print_help():
    print(f"""Available formatters: {available_formatters}
Special commands: {special_commands}""")


def print_plain():
    text = input("Text: ")
    history.append(text)
    print_history(history)
    return


def print_bold():
    text = input("Text: ")
    result = f"**{text}**"
    history.append(result)
    print_history(history)
    return


def print_italic():
    text = input("Text: ")
    result = f"*{text}*"
    history.append(result)
    print_history(history)
    return


def print_link():
    label = input("Label: ")
    url = input("URL: ")
    result = f"[{label}]({url})"
    history.append(result)
    print_history(history)


def print_history(_history):
    # print(*history)
    for element in _history:
        if element != "":
            print(element, end='')
    print()


def print_inline():
    text = input("Text: ")
    result = f"`{text}`"
    history.append(result)
    print_history(history)


def print_header():
    while True:
        level_input = int(input("Level: "))
        if 0 <= level_input <= 6:
            text = input("Text: ")
            result = level_input * "#" + " " + text + "\n"
            history.append(result)
            print_history(history)
            # print(history)
            # print()
            return
        else:
            print("The level should be within the range of 1 to 6")
        # this continue will make the function start to check from beginning if the level is not in the given range
        # after continue the program will start asking for input for level
        continue


def print_newline():
    history.append("\n")
    print_history(history)
    return


def save_to_file():
    # print(history)
    with open('output.md', 'w+', encoding='utf-8') as final_result:
        final_result.write("".join(history))


def print_list(choice=None):
    elements = []
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows > 0:
            for i in range(1, number_of_rows + 1):
                elements.append(input(f"Row #{i}: "))
            if choice == "ordered-list":
                for i, value in enumerate(elements):
                    result = f"{i + 1}." + f" {value}\n"
                    history.append(result)
            elif choice == "unordered-list":
                for i, value in enumerate(elements):
                    result = f"*" + f" {value}\n"
                    history.append(result)
            print_history(history)
            # print(history)
            break
        else:
            print("The number of rows should be greater than zero")
        continue


while True:
    u_input = ask_input()
    match 
    if u_input not in (available_formatters + special_commands):
        print_error()
    elif u_input == special_commands[0]:
        print_help()
    elif u_input == special_commands[1]:
        save_to_file()
        break
    elif u_input == "header":
        print_header()
    elif u_input == "plain":
        print_plain()
    elif u_input == "bold":
        print_bold()
    elif u_input == "italic":
        print_italic()
    elif u_input == "new-line":
        print_newline()
    elif u_input == "link":
        print_link()
    elif u_input == "inline-code":
        print_inline()
    elif u_input == "ordered-list":
        print_list("ordered-list")
    elif u_input == "unordered-list":
        print_list("unordered-list")
