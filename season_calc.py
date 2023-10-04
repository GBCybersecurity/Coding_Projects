months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]

thirty_day_months = ["April", "June", "September", "November"]

spring = ["April", "May"]
summer = [
    "July",
    "August",
]
fall = ["October", "November"]
winter = ["January", "February"]

season_overlap = ["March", "June", "September", "December"]

user_month = input("Enter a month: ")

if user_month.title() not in months:
  print(f"{user_month} is not a month.")
else:
  user_day = int(input("Enter a day: "))
  if user_day < 0 or user_day > 31:
    print(f"{user_day} is not a valid day in the month.")
  elif user_month.title() in thirty_day_months and user_day == 31:
    print(f"{user_month} only has 30 days.")
  elif user_month.title() == "February" and user_day > 28:
    print("February doesn't have more than 28 days.")
  else:
    if user_month.title() in season_overlap:
      if (user_month.title() == "March" and user_day > 19) \
      or (user_month.title() == "June" and user_day < 21):
        season = "Spring"
      elif (user_month.title() == "June" and user_day > 20) \
      or (user_month.title() == "September" and user_day < 23):
        season = "Summer"
      elif (user_month.title() == "September" and user_day > 22) \
      or (user_month.title() == "December" and user_day < 21):
        season = "Fall"
      elif (user_month.title() == "December" and user_day > 20) \
      or (user_month.title() == "March" and user_day < 20):
        season = "Winter"
    else:
      if user_month.title() in spring:
        season = "Spring"
      elif user_month.title() in summer:
        season = "Summer"
      elif user_month.title() in fall:
        season = "Fall"
      else:
        season = "Winter"
    print(f"Today is {user_month} {user_day} and the season is {season}.")
