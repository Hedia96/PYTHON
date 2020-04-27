##3.1.1.11:
'''
word=input()
if(word=="Spathiphyllum"):
    print("Yes -",word,"is the best plant ever!")
elif(word=="spathiphyllum"):
    print("Spathiphyllum! Not",word)
'''
######################################################
'''
If tax is less than or equal to 85,528 tax is 18% of income - 556.0 IF tax is more than 85,528, tax is 14,839.02 plus 32% of surplus above 85,528.

http://if-statement21.blogspot.com/2018/01/how-to-calculate-tax-with-variable.html

'''

'''
income = float(input("Enter the annual income: "))
if income <= 85528:
       
        tax=(income*.18)-556.02
        # Brackets are to make it do those sums first
else:
      tax = (income-85528)*0.32 + 14839.02
    #  tax=
        # Brackets are to make it do those sums first
tax = round(tax,0)
print("The tax is:", tax)
'''
########################################################
'''
year = int(input("Enter a year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("common year")
    else:
        print("leap year")
else:
    print("Common year")
'''
###########################################################
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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    result = daysInMonth(yr, mo)
    print(yr, mo, "->",result)    
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")


