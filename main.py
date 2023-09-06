# import modules
import random
import string


# function to generate password.
def generate_password(min_len, numbers = True, special_characters =True):
    # to stored  all the numbers in digits variable.
    digits = string.digits
    # to stored the  all alphabetic letters in alphabets variable.
    alphabets = string.ascii_letters
    # to stored the all special characters in special_chars variable.
    special_chars = string.punctuation

    #assign the aphabets in characters variables.
    characters = alphabets
    # check  the number is true if its true assing the append the digits in to characters.
    if numbers:
        characters += digits
    # check  the special_characters is true if its true assing the append the special Characters in to characters.
    if special_characters:
        characters += special_chars

    # declare the variables for generate password.
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    #check the conditon to loop
    while not meets_criteria or len(pwd) < min_len:
        # pick the random element in characters variable
        new_char = random.choice(characters)
        # append the random element
        pwd += new_char

        # check the random element in digits variable if it's there assign true to  has_number
        if new_char in digits:
            has_number = True
        # check the random element in special_chars variable if it's there assign true to  has_special
        elif new_char in special_chars:
            has_special = True

        # then assing true to meets_criteria variable.
        meets_criteria = True


        if numbers:
            # check  the number is true if its true assing the value to meets_criteria variable.
            meets_criteria = has_number
        if special_characters:
            # check  the special_characters is true if its true assing the value to meets_criteria variable.
            meets_criteria =  meets_criteria and has_special

    #finally return the pwd variable.
    return pwd


# get the inputs from user.
min_len = int(input("Enter the Minimum length: "))
has_number = input("Do you want to have numbers (y,n)").lower() == "y"
has_special = input("Do you want to have special characters (y,n)").lower() == "y"
pwd = generate_password(min_len,has_number,has_special)
print("The Generated Password is : ", pwd)