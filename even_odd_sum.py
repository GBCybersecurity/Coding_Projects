# Name: Brian Ibarra
# Data: 9/28/2023
# Description: Takes an integer (1-100) and adds
# the even or odd numbers up to that integer
even_odd = ["even", "odd"]
while True:
  sum = 0
  num_range = int(input("Enter number range(1-100): "))
  if num_range < 1 or num_range > 100:
    print("Input a valid range.")
    continue
  even_odd_choice = input("Enter 'even' or 'odd': ")
  if even_odd_choice.lower() not in even_odd:
    print("Enter either 'even' or 'odd'.")
    continue
  for nums in range(num_range + 1):
    if even_odd_choice == 'even':
      if nums % 2 == 0:
        sum += nums
    else:
      if nums % 2 != 0:
        sum += nums
  break
print(sum)
