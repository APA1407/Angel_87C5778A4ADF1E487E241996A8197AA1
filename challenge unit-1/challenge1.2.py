def leapyear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year=int(input("Enter a year:"))
if leapyear(year):
  print(year," is a leap year.")
else:
  print(year," is not a leap year.")