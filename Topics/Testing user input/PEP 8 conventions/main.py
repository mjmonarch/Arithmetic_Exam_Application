def check_name(var):
    non_appropriate_list = ['l', '0', 'I']
    if len(var) == 1 and var in non_appropriate_list:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
        return
    if var.islower():
        print("It is a common variable")
        return
    elif var.isupper():
        print("It is a constant")
        return
    else:
        print("You shouldn't use mixedCase")
