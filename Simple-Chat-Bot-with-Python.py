print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print(f"What a great name you have, {name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")

# read a number and count to it here
number = int(input())
counter = 0
while counter <= number:
    print(str(counter) + "!")
    counter += 1

# test user's programming knowledge
question = "Why do we use methods?"
answer_option = """1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program."""
print(answer_option)


def answer_user(option1, option2, option3, option4):
    user_input = int(input())
    print(user_input)
    if user_input == option2:
        print("Congratulations, have a nice day!")
    else:
        print("Please try again.")
        answer_user(option1, option2, option3, option4)


answer_user(1, 2, 3, 4)
