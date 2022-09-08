#I used the leap year calculation(because time is valuable) from one I found online, everything else I coded.


import re
selector = re.compile(r'([0-3][0-9])/([0-1][1-2])/([1-2][0-9]{3})') 
mo = selector.search('27/02/2020')
date = mo.group(1)
month = mo.group(2)
year = int(mo.group(3))

def isleapyear(years):
    if (years % 400 == 0) and (years % 100 == 0):
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (years % 4 ==0) and (years % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False

print(date, month, year)
if month == '04' or month == '06' or month == '09' or month == '11' and int(date) < 31:
    print(True)
if month ==  '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12' and int(date) < 32:
    print(True)
if month == '02' and int(date) < 29:
    print(True)
if month == '02' and int(date) < 30 and isleapyear(year) == True:
    print(True)
else:
    print(False)
