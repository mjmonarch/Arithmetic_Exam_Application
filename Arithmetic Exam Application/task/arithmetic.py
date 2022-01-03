# _______________________________________STAGE 1_____________________________________________________
# action = input()
# try:
#     lst = action.split()
#     var_1 = int(lst[0])
#     var_2 = int(lst[2])
#     operand_1 = lst[1]
#     if operand_1 == '+':
#         result = var_1 + var_2
#     elif operand_1 == '-':
#         result = var_1 - var_2
#     elif operand_1 == '*':
#         result = var_1 * var_2
#     else:
#         raise Exception
#         # create own exception class and print to user that there is no such operand
# except Exception:
#     print("Something went wrong...")
# finally:
#     print(result)

# _______________________________________STAGE 2_____________________________________________________
import random

operations = ['+', '-', '*']

var_1 = random.randint(2, 9)
var_2 = random.randint(2, 9)
operand_1 = random.choice(operations)

if operand_1 == '+':
    result = var_1 + var_2
elif operand_1 == '-':
    result = var_1 - var_2
elif operand_1 == '*':
    result = var_1 * var_2
else:
    raise Exception("Incorrect operand")

print(var_1, operand_1, var_2)
user_result = input()
try:
    if int(user_result) == result:
        print("Right!")
    else:
        print("Wrong!")
except ValueError:
    print("You should enter number!!!")
