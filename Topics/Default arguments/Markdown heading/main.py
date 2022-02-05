def heading(text, level=1):
    if level <= 1:
        level = 1
        # print("#" * level + " " + text)
        return "#" * level + " " + text

    elif level >= 6:
        level = 6
        # print("#" * level + " " + text)
        return "#" * level + " " + text

    return "#" * level + " " + text


# code under this line was just for testing purpose
# heading("A")
#
# heading("A", 0)
# heading("A", 2)
# heading("A", 6)
# heading("A", 10)
