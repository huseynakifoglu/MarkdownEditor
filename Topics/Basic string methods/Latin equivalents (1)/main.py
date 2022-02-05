name = input()


def normalize(fullname):
    # put your code here
    return fullname.replace("é", "e").replace("ë", "e").replace("á", "a").replace("å", "a").replace("œ", "oe").replace(
        "æ", "ae")


print(normalize(name))
