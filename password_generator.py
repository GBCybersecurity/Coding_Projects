# Name: Brian Ibarra
# Date: 10/4/2023
# Description: Generates a random password (up to 50 characters in length)
# from a list of letters (uppercase and lowercase), numbers, and special characters
from random import randint

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '~`!@#$%^&*_-+=?'
password_symbols_list = [characters,numbers,special_characters]


def password_gen():
    password = ''
    while True:
        password_length = input("Enter the length of the password(8-50): ")
        if password_length in characters or password_length in special_characters:
            print("Please input a valid number.")
            continue
        if password_length == '':
            password_length = int(8)
            break
        password_length = int(password_length)
        if password_length < 8 or password_length > 50:
            print("Please input a valid number.")
            continue
        break
    for count in range(password_length):
        chosen_symbol = password_symbols_list[randint(0,2)]
        password += chosen_symbol[randint(0,len(chosen_symbol)-1)]
    print(f"Your generated password is {password}")

password_gen()
