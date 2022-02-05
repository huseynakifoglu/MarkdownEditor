def check_email(string):
    if (" " in string) or (("@" or ".") not in string):
        # print("False")
        return False
    elif ("@." in string) or "." not in string[string.find("@") + 1:]:
        return False
    else:
        return True
