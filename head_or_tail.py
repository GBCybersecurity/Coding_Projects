# Programmer: Brian Ibarra
# Date: 10/25/2023
# Description: Read first or last lines of a file
# with options to modify the amount of lines read
# and copy the results to a file

import os

current_dir = os.getcwd()

MENU = """
1. First ten lines of file
2. Last ten lines of file
3. First lines of file (custom lines)
4. Last lines of file (custom lines)
5. Copy first ten lines to a new file
6. Copy last ten lines to a new file
7. Copy first lines to a new file (custom lines)
8. Copy last lines to a new file (custom lines)
"""

def read_file(read_file):
  with open(f"{current_dir}/{read_file}", "r") as file:
    text = file.read()
    return text


def head_or_tail(first_or_last, lines=10):
  file_to_open = input("Name of file to open: ")
  text = read_file(file_to_open).split('\n')
  complete_text = ""
  if first_or_last == 1:
    for line in text[:lines]:
      complete_text += f"{line}\n"
    return complete_text
  elif first_or_last == 2:
    for line in text[-lines:]:
      complete_text += f"{line}\n"
    return complete_text


def write_file(content):
  file_dir = "MYFILES"
  if file_dir not in os.listdir():
    os.mkdir(file_dir)
  new_file = input("Name of file to write to: ")
  with open(f"{current_dir}/{file_dir}/{new_file}", "w") as file:
    file.write(content)


def menu_choice(choice):
  if choice == 1:
    result = head_or_tail(1)
    return result
  elif choice == 2:
    result = head_or_tail(2)
    return result
  elif choice == 3:
    lines = int(input("How many of the first lines would you like to read: "))
    result = head_or_tail(1, lines)
    return result
  elif choice == 4:
    lines = int(input("How many of the last lines would you like to read: "))
    result = head_or_tail(2, lines)
    return result
  elif choice == 5:
    result = head_or_tail(1)
    write_file(result)
    return result
  elif choice == 6:
    result = head_or_tail(2)
    write_file(result)
    return result
  elif choice == 7:
    lines = int(input("How many of the first lines would you like to read: "))
    result = head_or_tail(1, lines)
    write_file(result)
    return result
  elif choice == 8:
    lines = int(input("How many of the last lines would you like to read: "))
    result = head_or_tail(2, lines)
    write_file(result)
    return result


def main():
  while True:
    print(MENU)
    choice = int(input("What is your choice: "))
    while int(choice) < 1 or int(choice) > 8:
      print("Please choose a number from 1 to 8!")
      choice = int(input("What is your choice: "))
    outcome = menu_choice(choice)
    print(outcome)
    go_again = input(
        "Run again (Y or y), any other key to terminate the program: ")
    if go_again.lower() != "y":
      break
  print("Thanks for using my program\nGoodbye!")


main()
