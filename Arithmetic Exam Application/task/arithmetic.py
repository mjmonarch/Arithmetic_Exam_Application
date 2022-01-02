# _______________________________________STAGE 1_____________________________________________________
action = input()
try:
    lst = action.split()
    var_1 = int(lst[0])
    var_2 = int(lst[2])
    operand_1 = lst[1]
    if operand_1 == '+':
        result = var_1 + var_2
    elif operand_1 == '-':
        result = var_1 - var_2
    elif operand_1 == '*':
        result = var_1 * var_2
    else:
        raise Exception
        # create own exception class and print to user that there is no such operand
except Exception:
    print("Something went wrong...")
finally:
    print(result)
