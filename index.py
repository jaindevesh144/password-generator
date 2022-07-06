import string
import random


def exit_program(code=0):
    input("Press enter to exit the program")
    exit(code)


if __name__ == "__main__":
    letter_set = list(string.ascii_letters)
    digit_set = list(string.digits)
    punc_set = list(string.punctuation)

    custom_set = []

    letter_required = input("Should your password contain letters [Y,n] ")
    digits_required = input("Should your password contain digits [Y,n] ")
    punc_required = input("Should your password contain punctuations [Y,n] ")

    if letter_required == "Y" or letter_required == "y" or letter_required == "":
        custom_set += letter_set
    if digits_required == "Y" or digits_required == "y" or digits_required == "":
        custom_set += digit_set
    if punc_required == "Y" or punc_required == "y" or punc_required == "":
        custom_set += punc_set

    pass_length = int(input("What should be the length of password\n"))

    password = ""

    for i in range(pass_length):
        char = random.choice(custom_set)
        password += char

    print(password)
    exit_program()
