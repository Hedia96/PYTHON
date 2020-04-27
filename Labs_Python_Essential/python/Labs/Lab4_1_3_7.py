#module4.lab2

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
    

print(daysInMonth(2020,4))