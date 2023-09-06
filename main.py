import random
import string


def generate_password(min_len, numbers = True, special_characters =True):
    digits = string.digits
    alphabets = string.ascii_letters
    special_chars = string.punctuation

    characters = alphabets
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria =  meets_criteria and has_special

    return pwd


min_len = int(input("Enter the Minimum length: "))
has_number = input("Do you want to have numbers (y,n)").lower() == "y"
has_special = input("Do you want to have special characters (y,n)").lower() == "y"
pwd = generate_password(min_len,has_number,has_special)
print("The Generated Password is : ", pwd)