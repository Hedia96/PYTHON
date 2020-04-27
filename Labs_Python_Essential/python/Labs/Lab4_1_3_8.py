
##############################
def isYearLeap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True #return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(isYearLeap(2020))


    
def daysInMonth(year, month):
    list_days_per_mounth=[31,28,31,30,31,30,31,31,30,31,30,31]
    days=0
    if(isYearLeap(year)==True and month==2):
        days=list_days_per_mounth[1]+1
    elif(isYearLeap(year)==False and month==2):
        days=list_days_per_mounth[1]
    else:
        days=list_days_per_mounth[month-1]
    return days    
    

def dayOfYear(year, month, day):
    dayofyr=0
    if(year>1582 and (month<=12 and month>=1)\
    and (day<=31 and day>=1)):
      # print("Ddddddddddddd")
       #add all days of previous months then add the day of date
       for index in range(1,month):
           dayofyr+=daysInMonth(year,index)
        #   print("for",dayofyr)
       dayofyr+=day
       #print("infunnnnn",dayofyr)
       return dayofyr
    else:
        return
#return None if there is any error in inputs    
print(daysInMonth(2000,12))
print(dayOfYear(2000,12,31))
print(dayOfYear(2020,4,9))
