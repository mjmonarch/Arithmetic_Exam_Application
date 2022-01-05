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

# # _______________________________________STAGE 2_____________________________________________________
# import random
#
# operations = ['+', '-', '*']
#
# var_1 = random.randint(2, 9)
# var_2 = random.randint(2, 9)
# operand_1 = random.choice(operations)
#
# if operand_1 == '+':
#     result = var_1 + var_2
# elif operand_1 == '-':
#     result = var_1 - var_2
# elif operand_1 == '*':
#     result = var_1 * var_2
# else:
#     raise Exception("Incorrect operand")
#
# print(var_1, operand_1, var_2)
# user_result = input()
# try:
#     if int(user_result) == result:
#         print("Right!")
#     else:
#         print("Wrong!")
# except ValueError:
#     print("You should enter number!!!")

# # _______________________________________STAGE 3_____________________________________________________
# import random
#
# OPERATIONS = ['+', '-', '*']
# NUM_OF_ATTEMPTS = 5
# score = 0
#
# for i in range(5):
#     var_1 = random.randint(2, 9)
#     var_2 = random.randint(2, 9)
#     operand_1 = random.choice(OPERATIONS)
#
#     if operand_1 == '+':
#         result = var_1 + var_2
#     elif operand_1 == '-':
#         result = var_1 - var_2
#     elif operand_1 == '*':
#         result = var_1 * var_2
#     else:
#         raise Exception("Incorrect operand")
#
#     print(var_1, operand_1, var_2)
#     while True:
#         user_result = input()
#         try:
#             if int(user_result) == result:
#                 print("Right!")
#                 score += 1
#                 break
#             else:
#                 print("Wrong!")
#                 break
#         except ValueError:
#             print("Incorrect format.")
#
# print(f"Your mark is {score}/{NUM_OF_ATTEMPTS}.")

# _______________________________________STAGE 4_____________________________________________________
import random
import time

OPERATIONS = ['+', '-', '*']
POSITIVE_ANSWERS = ['Yes', 'YES', 'yes', 'y', 'Y']
NUM_OF_ATTEMPTS = 5
LEVEL_DESCRIPTION = {1: 'simple operations with numbers 2-9', 2: 'integral squares of 11-29'}


def play_level_one():
    _score = 0
    for i in range(NUM_OF_ATTEMPTS):
        var_1 = random.randint(2, 9)
        var_2 = random.randint(2, 9)
        operand_1 = random.choice(OPERATIONS)

        if operand_1 == '+':
            result = var_1 + var_2
        elif operand_1 == '-':
            result = var_1 - var_2
        elif operand_1 == '*':
            result = var_1 * var_2
        else:
            raise Exception("Incorrect operand")

        print(var_1, operand_1, var_2)
        while True:
            user_result = input()
            try:
                if int(user_result) == result:
                    print("Right!")
                    _score += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Wrong format! Try again.")
    return _score


def play_level_two():
    _score = 0
    for i in range(NUM_OF_ATTEMPTS):
        var_1 = random.randint(11, 29)
        result = var_1 ** 2
        print(var_1)
        while True:
            user_result = input()
            try:
                if int(user_result) == result:
                    print("Right!")
                    _score += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Wrong format! Try again.")
    return _score


# starting point of the program
print("Which level do you want? Enter a number:\n"
      "1 - simple operations with numbers 2-9\n"
      "2 - integral squares of 11-29\n")
while True:
    answer = input()
    if answer == '1':
        start = time.perf_counter()
        level = 1
        score = play_level_one()
        finish = time.perf_counter()
        break
    elif answer == '2':
        start = time.perf_counter()
        level = 2
        score = play_level_two()
        finish = time.perf_counter()
        break
    else:
        print("Incorrect format.")
        continue

print(f"Your mark is {score}/{NUM_OF_ATTEMPTS}. Would you like to save the result?"
      f"Enter yes or no.")
answer = input()
if answer in POSITIVE_ANSWERS:
    print("What is your name?")
    name = input()
    with open('results.txt', 'a', encoding='utf-8') as writer:
        writer.write(f"\n{name}: {score}/{NUM_OF_ATTEMPTS} in level {level} ({LEVEL_DESCRIPTION[level]})."
                     f"\nTime spent: {finish - start}")
    print('The results are saved in "results.txt".')
