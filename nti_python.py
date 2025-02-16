98% of storage used … If you run out, you can't create, edit, and upload files. Get 100 GB of storage for EGP 14.99 EGP 3.69/month for 3 months.
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

