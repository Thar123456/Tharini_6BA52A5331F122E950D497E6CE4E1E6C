# program to determine whether the given year is leap year or not

def isLeapYear(year):
  if(year%4==0 and year%10!=0) or year%400==0:
     return True
  else:
     return False
year=2024
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))